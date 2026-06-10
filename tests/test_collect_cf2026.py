import tempfile
import unittest
from pathlib import Path

from scripts import collect_cf2026 as cf


REAL_MECH = Path(
    r"E:\mech_collection\combustion_and_flame_2026_mechanisms\ammonia_dimethoxyethane"
    r"\chunlan_qin_2026_114555_kinetic_study_of_high_temperature_co_oxidatio"
    r"\extracted\s0010218025005929_mmc2\Liu-SMM3_12DME_mech.inp"
)
REAL_THERMO = Path(
    r"E:\mech_collection\combustion_and_flame_2026_mechanisms\ammonia_dimethoxyethane"
    r"\chunlan_qin_2026_114555_kinetic_study_of_high_temperature_co_oxidatio"
    r"\extracted\s0010218025005929_mmc3\Liu-SMM4_12DME_therm.dat"
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


if __name__ == "__main__":
    unittest.main()
