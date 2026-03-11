from __future__ import annotations
import json
import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from day1_api_hello import fetch_online, sha256_text, validate_payload

MOCK_RESPONSE = {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}

def make_mock():
    m = MagicMock()
    m.status_code = 200
    m.json.return_value = MOCK_RESPONSE
    return m

# Тест 1: API возвращает правильную структуру (mock)
def test_fetch_structure():
    with patch("requests.get", return_value=make_mock()):
        status, data = fetch_online("https://jsonplaceholder.typicode.com/todos/1")
    assert status == 200
    assert "userId" in data and "id" in data and "title" in data and "completed" in data

# Тест 2: Конкретные значения (mock)
def test_fetch_values():
    with patch("requests.get", return_value=make_mock()):
        status, data = fetch_online("https://jsonplaceholder.typicode.com/todos/1")
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] == "delectus aut autem"
    assert data["completed"] == False

# Тест 3: SHA256 детерминирован
def test_sha256_deterministic():
    sha1 = sha256_text("test string")
    sha2 = sha256_text("test string")
    assert sha1 == sha2
    assert len(sha1) == 64

# Тест 4: Валидация проходит для правильного payload
def test_validation_passes():
    good = {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
    ok, errors = validate_payload(good)
    assert ok == True
    assert errors == []

# Тест 5: Артефакты существуют
def test_artifacts_exist():
    assert os.path.exists("artifacts/day1/response.json")
    assert os.path.exists("artifacts/day1/summary.json")

# Тест 6: summary.json содержит токен студента
def test_summary_has_token():
    with open("artifacts/day1/summary.json", encoding="utf-8") as f:
        summary = json.load(f)
    token = summary["student"]["token"]
    assert token.startswith("D1-")
