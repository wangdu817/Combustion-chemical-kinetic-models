import tempfile
import unittest
import zipfile
import json
from pathlib import Path

from scripts import collect_cf2026 as cf


REAL_MECH = Path(
    r"E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethoxyethane"
    r"\2026\qin_2026_ammonia_dimethoxyethane_114555\chem.inp"
)
REAL_THERMO = Path(
    r"E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethoxyethane"
    r"\2026\qin_2026_ammonia_dimethoxyethane_114555\therm.dat"
)


class CollectCf2026Tests(unittest.TestCase):
    def test_ckinterp_report_is_not_classified_as_chemkin_mechanism(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "chem.out"
            path.write_text(
                "SPECIES CONSIDERED\n 1. H2\nREACTIONS CONSIDERED\n 1. H2+O2=2OH\n",
                encoding="utf-8",
            )
            self.assertNotIn("chemkin_mechanism", cf.classify_file(path))

    def test_cantera_processing_standardizes_files_and_counts(self):
        if not REAL_MECH.exists() or not REAL_THERMO.exists():
            self.skipTest("local downloaded 12DME mechanism fixture is not available")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dest = root / "paper"

            result = cf.process_with_cantera(REAL_MECH, REAL_THERMO, None, dest)

            self.assertEqual(result.status, "ok")
            self.assertEqual(result.species, "672")
            self.assertEqual(result.reactions, "3798")
            self.assertTrue((dest / "chem.inp").exists())
            self.assertTrue((dest / "therm.dat").exists())
            self.assertTrue((dest / "mechanism.yaml").exists())

    def test_reaction_kinetics_screen_excludes_physical_mechanism_titles(self):
        false_positive = {
            "title": "Thermoacoustic feedback mechanisms for premixed burners with a reacting hydrogen-methane jet in cross-flow",
            "abstract": "",
        }
        self.assertFalse(cf.is_reaction_kinetics_candidate(false_positive))

    def test_reaction_kinetics_screen_keeps_chemical_kinetics_titles(self):
        titles = [
            "Understanding the formation of nitrogen-containing products in pyrrole pyrolysis",
            "Experimental and kinetic modeling study of ethyl acetate pyrolysis and oxidation in a shock tube",
            "Measurements of the laminar burning velocities and an improved low-to-high temperature kinetic model of 2-butanone",
        ]
        for title in titles:
            with self.subTest(title=title):
                self.assertTrue(cf.is_reaction_kinetics_candidate({"title": title, "abstract": ""}))

    def test_detect_fuel_uses_title_and_avoids_substring_overmatches(self):
        record = {
            "title": "Kinetic study of high-temperature co-oxidation of ammonia and 1,2-dimethoxyethane",
            "abstract": "The abstract mentions hydrogen, methane, ethane, N2O and many intermediates in the mechanism.",
        }

        self.assertEqual(cf.detect_fuel(record), "ammonia_dimethoxyethane")

    def test_detect_fuel_distinguishes_dodecane_from_decane(self):
        record = {
            "title": "Revealing the oxidation kinetics of n-dodecane, ethylcyclohexane and n-butylbenzene blended fuels",
            "abstract": "",
        }

        self.assertEqual(cf.detect_fuel(record), "n_dodecane_ethylcyclohexane_n_butylbenzene")

    def test_detect_fuel_adds_2025_specific_fuels(self):
        cases = {
            "An experimental and kinetic study of quadricyclane autoignition at high temperatures": "quadricyclane",
            "Part A: 1-Butene": "1_butene",
            "Part B: n-Butane": "n_butane",
            "cyclopentene autoignition mechanism": "cyclopentene",
            "alternative gas to liquid jet fuel": "gtl_jet_fuel",
        }
        for title, expected in cases.items():
            with self.subTest(title=title):
                self.assertEqual(cf.detect_fuel({"title": title, "abstract": ""}), expected)

    def test_detect_fuel_does_not_infer_method_paper_fuel_from_abstract_side_terms(self):
        record = {
            "title": "Bayesian sequential experimental design for combustion kinetic models",
            "abstract": "An ammonia model is used as one example case in a general method paper.",
        }

        self.assertEqual(cf.detect_fuel(record), "unknown_fuel")

    def test_parse_cantera_yaml_counts_without_successful_solution_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            yaml_path = Path(tmp) / "mechanism.yaml"
            yaml_path.write_text(
                """
phases:
- name: gas
  species: [H2, O2, OH]
  reactions: all
species:
- name: H2
- name: O2
- name: OH
reactions:
- equation: H2 + O2 <=> 2 OH
- equation: OH + H2 <=> H2O + H
""",
                encoding="utf-8",
            )

            self.assertEqual(cf.parse_cantera_yaml_counts(yaml_path), ("3", "2"))

    def test_parse_cantera_yaml_counts_from_phase_species_when_yaml_is_partial(self):
        with tempfile.TemporaryDirectory() as tmp:
            yaml_path = Path(tmp) / "partial.yaml"
            yaml_path.write_text(
                """
phases:
- name: gas
  species: [H2, O2,
    OH, H2O]
  reactions: all
""",
                encoding="utf-8",
            )

            self.assertEqual(cf.parse_cantera_yaml_counts(yaml_path), ("4", ""))

    def test_cleanup_inactive_paper_folders_removes_ignored_payloads(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            active = root / "fuel" / "2026" / "active_paper"
            inactive = root / "methane_ethane" / "2026" / "inactive_paper"
            inactive_extracted = inactive / "extracted"
            active.mkdir(parents=True)
            inactive_extracted.mkdir(parents=True)
            (active / "mechanism_summary.md").write_text("active", encoding="utf-8")
            (inactive / "mechanism_summary.md").write_text("stale", encoding="utf-8")
            (inactive_extracted / "old.txt").write_text("old payload", encoding="utf-8")

            cf.cleanup_inactive_paper_folders(root, {active.resolve()})

            self.assertTrue(active.exists())
            self.assertFalse(inactive.exists())
            self.assertFalse((root / "methane_ethane").exists())

    def test_record_folder_uses_fuel_year_surname_layout(self):
        record = {
            "authors": ["Chunlan Qin", "Second Author"],
            "fuelType": "ammonia_dimethoxyethane",
            "articleNumber": "114555",
            "title": "Kinetic study",
        }

        folder = cf.record_folder(record)

        self.assertEqual(folder.parts[-3:], ("ammonia_dimethoxyethane", "2026", "qin_2026_ammonia_dimethoxyethane_114555"))

    def test_record_folder_uses_explicit_year(self):
        record = {
            "authors": ["Xuan Ren"],
            "fuelType": "methylhydrazine",
            "articleNumber": "114478",
            "year": "2025",
        }

        folder = cf.record_folder(record)

        self.assertEqual(folder.parts[-3:], ("methylhydrazine", "2025", "ren_2025_methylhydrazine_114478"))

    def test_cleanup_active_paper_folder_keeps_only_summary_and_mechanisms(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for name in ["mechanism_summary.md", "chem.inp", "therm.dat", "tran.dat", "mechanism.yaml", "cantera_conversion.log"]:
                (folder / name).write_text(name, encoding="utf-8")
            (folder / "_processing").mkdir()
            (folder / "_processing" / "cantera_conversion.log").write_text("log", encoding="utf-8")
            (folder / "extracted").mkdir()
            (folder / "extracted" / "old.txt").write_text("old", encoding="utf-8")

            cf.cleanup_active_paper_folder(folder)

            self.assertEqual(
                sorted(path.name for path in folder.iterdir()),
                ["_processing", "chem.inp", "mechanism.yaml", "mechanism_summary.md", "therm.dat", "tran.dat"],
            )
            self.assertTrue((folder / "_processing" / "cantera_conversion.log").exists())

    def test_classify_thermo_file_with_utf_bom(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "thermo.txt"
            path.write_text("\ufeffTHERMO\n   298.000 1000.000 5000.000\nH2 G 300.0 5000.0 1000.0 1\nEND\n", encoding="utf-8")

            self.assertIn("thermo", cf.classify_file(path))

    def test_classify_transport_table_without_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tran.txt"
            path.write_text(
                "\n".join(
                    [
                        "AR                 0   136.500     3.330     0.000     0.000     0.000",
                        "H2                 1    38.000     2.920     0.000     0.790   280.000",
                        "O2                 1   107.400     3.458     0.000     1.600     3.800",
                        "H2O                2   572.400     2.605     1.844     0.000     4.000",
                        "CO2                1   244.000     3.763     0.000     2.650     2.100",
                        "ENDDIFF",
                    ]
                ),
                encoding="utf-8",
            )

            self.assertIn("transport", cf.classify_file(path))

    def test_detect_plasma_case_from_title_or_mechanism_text(self):
        record = {"title": "Direct NO removal driven by dielectric barrier discharge", "abstract": ""}

        self.assertEqual(cf.detect_plasma_case(record), "yes")

    def test_detect_plasma_case_ignores_analytical_electron_ionization(self):
        record = {
            "title": "Oxidation chemistry in a jet-stirred reactor",
            "abstract": "Products were measured by gas chromatography mass spectroscopy combined with electron ionization.",
        }

        self.assertEqual(cf.detect_plasma_case(record), "no")

    def test_gb_t_7714_uses_ascii_et_al_for_many_authors(self):
        record = {
            "authors": ["A", "B", "C", "D", "E", "F", "G"],
            "title": "Test title",
            "volume": "1",
            "doi": "10.1/example",
            "articleNumber": "114000",
        }

        citation = cf.gb_t_7714(record)

        self.assertIn("A, B, C, D, E, F, et al.", citation)
        self.assertNotIn("绛", citation)

    def test_gb_t_7714_uses_record_year(self):
        record = {
            "authors": ["A"],
            "title": "Test title",
            "volume": "271",
            "year": "2025",
            "doi": "10.1/example",
            "articleNumber": "113870",
        }

        self.assertIn("Combustion and Flame, 2025, 271: 113870", cf.gb_t_7714(record))

    def test_import_sciencedirect_volume_metadata_adds_years(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "volumes"
            source.mkdir()
            (source / "volume_271.json").write_text(
                json.dumps(
                    [
                        {
                            "year": "2025",
                            "volume": "271",
                            "month": "January",
                            "title": "Shock tube kinetic modeling study",
                            "pii": "S0010218024000012",
                            "articleNumber": "113900",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            old_root, old_raw, old_downloads, old_extracted, old_metadata = (
                cf.ROOT,
                cf.RAW,
                cf.DOWNLOADS,
                cf.EXTRACTED,
                cf.METADATA_JSON,
            )
            try:
                cf.ROOT = root / "collection"
                cf.RAW = cf.ROOT / "_raw"
                cf.DOWNLOADS = cf.RAW / "downloads"
                cf.EXTRACTED = cf.RAW / "extracted"
                cf.METADATA_JSON = cf.RAW / "article_metadata.json"
                cf.write_metadata([{"pii": "S0010218025000001", "title": "Existing 2026"}])

                cf.import_sciencedirect_volume_metadata(source, "2025")
                records = cf.read_metadata()
            finally:
                cf.ROOT, cf.RAW, cf.DOWNLOADS, cf.EXTRACTED, cf.METADATA_JSON = (
                    old_root,
                    old_raw,
                    old_downloads,
                    old_extracted,
                    old_metadata,
                )

            years = {record["pii"]: record["year"] for record in records}
            self.assertEqual(years["S0010218025000001"], "2026")
            self.assertEqual(years["S0010218024000012"], "2025")

    def test_restore_openalex_abstract_inverted_index(self):
        inverted = {"Combustion": [0], "and": [1], "Flame": [2], "abstract.": [3]}

        self.assertEqual(cf.restore_openalex_abstract(inverted), "Combustion and Flame abstract.")

    def test_extract_archives_recurses_and_uses_file_signature(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inner_zip = root / "inner_payload.dat"
            with zipfile.ZipFile(inner_zip, "w") as zf:
                zf.writestr("mechanism.inp", "ELEMENTS\nH O\nEND\nSPECIES\nH2 O2\nEND\nREACTIONS\nH2+O2=2OH 1 0 0\nEND\n")
            outer_zip = root / "outer.zip"
            with zipfile.ZipFile(outer_zip, "w") as zf:
                zf.write(inner_zip, "nested/inner_payload.dat")

            dest = root / "out"
            notes = cf.extract_archives([outer_zip], dest)
            extracted = list(dest.rglob("mechanism.inp"))

            self.assertTrue(any("extracted" in note for note in notes))
            self.assertEqual(len(extracted), 1)
            self.assertIn("chemkin_mechanism", cf.classify_file(extracted[0]))


if __name__ == "__main__":
    unittest.main()
