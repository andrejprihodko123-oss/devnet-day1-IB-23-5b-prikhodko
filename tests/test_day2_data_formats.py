from __future__ import annotations
import json, os, subprocess, csv, yaml
import xml.etree.ElementTree as ET
from pathlib import Path
import jsonschema

ROOT   = Path(__file__).resolve().parents[1]
DAY2   = ROOT / "artifacts" / "day2"
SCHEMA = ROOT / "schemas" / "day2_summary.schema.json"

def load_json(p):
    return json.loads(p.read_text(encoding="utf-8"))

def test_day2_generate_and_validate():
    env = os.environ.copy()
    assert env.get("STUDENT_TOKEN"), "STUDENT_TOKEN must be set"
    assert env.get("STUDENT_NAME"),  "STUDENT_NAME must be set"
    assert env.get("STUDENT_GROUP"), "STUDENT_GROUP must be set"

    r = subprocess.run(
        ["python", "src/day2_data_formats.py", "--input", "artifacts/day1/response.json"],
        cwd=str(ROOT), env=env, capture_output=True, text=True
    )
    assert r.returncode == 0, f"script failed:\n{r.stderr}"

    for fn in ["normalized.json","normalized.yaml","normalized.xml","normalized.csv","summary.json"]:
        assert (DAY2 / fn).exists(), f"missing {fn}"

    jsonschema.validate(instance=load_json(DAY2/"summary.json"), schema=load_json(SCHEMA))

    assert load_json(DAY2/"normalized.json") == yaml.safe_load((DAY2/"normalized.yaml").read_text(encoding="utf-8"))

    root = ET.parse(DAY2/"normalized.xml").getroot()
    assert root.tag == "devnet_day2"
    th8 = root.findtext("./student/token_hash8")
    assert th8 and len(th8) == 8

    with (DAY2/"normalized.csv").open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1
    assert "token_hash8" in rows[0]
    assert rows[0]["completed"] in ("true","false")
