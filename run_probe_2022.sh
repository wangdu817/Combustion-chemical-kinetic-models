export MECH_COLLECTION_WORKSPACE=/home/icaurs/Combustion-chemical-kinetic-models
cd /home/icaurs/Combustion-chemical-kinetic-models
.venv/bin/python scripts/collect_cf2026.py probe-supplements --year 2022 --max-mmc 12 --serial >> probe_2022.log 2>&1
echo probe done
