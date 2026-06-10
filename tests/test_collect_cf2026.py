import tempfile
import unittest
import zipfile
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

    def test_cleanup_active_paper_folder_keeps_only_summary_and_mechanisms(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for name in ["mechanism_summary.md", "chem.inp", "therm.dat", "tran.dat", "mechanism.yaml", "cantera_conversion.log"]:
                (folder / name).write_text(name, encoding="utf-8")
            (folder / "extracted").mkdir()
            (folder / "extracted" / "old.txt").write_text("old", encoding="utf-8")

            cf.cleanup_active_paper_folder(folder)

            self.assertEqual(
                sorted(path.name for path in folder.iterdir()),
                ["chem.inp", "mechanism.yaml", "mechanism_summary.md", "therm.dat", "tran.dat"],
            )

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
