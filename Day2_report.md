# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: Приходько Андрей Александрович
- Group: IB-23-5b
- Token: D1-IB-23-5b-16-10AF
- Repo: https://github.com/andrejprihodko123-oss/devnet-day1-IB-23-5b-prikhodko
- PR link (day2): https://github.com/andrejprihodko123-oss/devnet-day1-IB-23-5b-prikhodko/pull/1
(also in artifacts/day2/pr_link.txt)

## 2) NetAcad progress
- Module 2.2 done: Yes + screenshot
- Module 3.1–3.6 done: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6 + screenshot

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: Yes
- File `artifacts/day2/conflict_log.txt` exists: Yes
- Conflict note: Конфликт возник в README.md — ветки feature/day2-readme-A и feature/day2-readme-B изменили одну и ту же область файла. Конфликт был разрешён вручную: оставлены обе строки, после чего выполнен merge commit Resolve README conflict (Day2).

## 4) Generated artifacts (Day2)
- normalized.json: Yes
- normalized.yaml: Yes
- normalized.xml: Yes
- normalized.csv: Yes
- summary.json: Yes

## 5) Commands output (paste EXACT output)
### 5.1 Generator
```text
$ python src/day2_data_formats.py --input artifacts/day1/response.json
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-11T16:00:49.966454+00:00",
  "student": {
    "token": "D1-IB-23-5b-16-10AF",
    "token_hash8": "327c260e",
    "name": "Приходько Андрей Александрович",
    "group": "IB-23-5b"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "a3bd32875edeb144eb7b3bf662230e8f6292a4c56fe8d88b8e1df4f3d8b07972",
    "normalized_yaml_sha256": "54155ec5c5c11f50d904f8dd4d99ee294b44c19fc1105b3656ef7b51465de507",
    "normalized_xml_sha256": "8d7aa23ee4682fbbfdd4961c37113972b5b3b667e6b07af639f382a35aaf1165",
    "normalized_csv_sha256": "2ecf49f1634461f28823e9f012100974b877fd165f1322e84b9b28a58000a74d"
  },
  "computed": {
    "title_len": 18
  }
}
```
### 5.2 Tests
```text
$ pytest -q
.......                                                                  [100%]
7 passed in 0.15s
```

### 5.3 Git Log
```text
*   c200654 (HEAD -> master) Resolve README conflict (Day2)
|\  
| * 0f29d2f (feature/day2-readme-A) Day2 readme A
* | 907f185 Day2 readme B
* | aaeb9cf Day2 readme A
* |   8bbe906 (origin/master) Merge branch 'feature/day2-dataformats'
|\ \  
| * | 2461a10 (origin/feature/day2-dataformats, feature/day2-dataformats) Add PR link
| * | 7646910 Day 2: data formats, tests, schemas, artifacts
| * | 4be8833 Day 2: data formats, tests, schemas
| |/  
* / d9b1ed1 Day 2: artifacts, git log, conflict log, pr link
|/  
| * 3ea0e28 (feature/day2-readme-B) Day2 readme B
|/  
* 9e887b7 Day 1: Hello API — setup, venv, tests, artifacts
```

### 5.4 Conflict log
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        artifacts/day2/conflict_log.txt

no changes added to commit (use "git add" and/or "git commit -a")

### 6. What I learned
Как работают форматы данных JSON, YAML, XML, CSV и как конвертировать между ними на Python
Что такое детерминированный JSON (sort_keys=True) и зачем он нужен для SHA256
Как создавать ветки в Git, делать PR и сливать изменения
Как возникают merge conflicts и как их разрешать вручную
Как использовать token_hash8 для уникальной идентификации артефактов студента
Как валидировать JSON по схеме с помощью jsonschema

### 7. Problems & fixes
Problem 1: TypeError: 'type' object is not subscriptable при запуске скрипта на Python 3.8 — аннотации типов tuple[...] не поддерживаются.
Fix: Добавил from __future__ import annotations в начало файла.
Proof:
```text
$ head -1 src/day2_data_formats.py
```
```text
from __future__ import annotations
```
Problem 2: Скрипт не читал переменные из .env — переменные окружения не устанавливались автоматически.
Fix: Использовал export $(cat .env | xargs) перед запуском скрипта.
Proof:
```text
$ export STUDENT_TOKEN=D1-IB-23-5b-16-10AF
$ python src/day2_data_formats.py --input artifacts/day1/response.json
```
# вывод успешный (см. 5.1)
