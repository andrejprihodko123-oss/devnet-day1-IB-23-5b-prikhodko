# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Приходько Андрей Александрович
- Group: IB-23-5b
- Token: D1-IB-23-5b-16-10AF
- Repo: https://github.com/andrejprihodko123-oss/devnet-day1-IB-23-5b-prikhodko

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots: Yes
- Postman screenshots: Yes
- Python run screenshot: Yes

## 3) Artifacts checklist
- artifacts/day3/books_before.json: Yes
- artifacts/day3/books_sorted_isbn.json: Yes
- artifacts/day3/mybook_post.json: Yes
- artifacts/day3/books_by_me.json: Yes
- artifacts/day3/add100_report.json: Yes
- artifacts/day3/postman_collection.json: Yes
- artifacts/day3/postman_environment.json: Yes
- artifacts/day3/curl_get_books.txt: Yes
- artifacts/day3/curl_get_books_isbn.txt: Yes
- artifacts/day3/curl_get_books_sorted.txt: Yes
- artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
$ python src/day3_library_lab.py --offline
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-12T16:42:57.899570+00:00",
  "student": {
    "token": "D1-IB-23-5b-16-10AF",
    "token_hash8": "327c260e",
    "name": "Приходько Андрей Александрович",
    "group": "IB-23-5b"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "eee48f0e2f5ad8266366e6453719a60c4826863df5c1433dabefac8cb7773258",
    "books_sorted_isbn": "349d7f271f8d28f760f7f85d7f8a363e2fdfdf3738e889cdd83281e487c535d2",
    "mybook_post": "a2d538224930550c5a61f3e52ace3b388d14b83ec494b7b36182ac6713f18623",
    "books_by_me": "4285f89c21b4796a84c0625bbd98c46178c3da1dfabc4851838c8fa070e2d448",
    "add100_report": "bbdddf3417414dd8a4211ac8d1239ccd7288d1c97f82932ee470116a47341182",
    "postman_collection": "5c580a1e77d79823ffdb631f6077cd487375147e8e286eb709647abb24e5b29f",
    "postman_environment": "f5132bfdef5a8debba952fd84690614536afc482fce769f7b4738af263c1a741",
    "curl_get_books": "de64bae22fde03848fbeb14e2a6c661cf7e9eed12f29b574d596224bf5bf6bf9",
    "curl_get_books_isbn": "ee1093008a5d89a75d9aaf8a2c8a7987c8841bce0c4028d02d32e78f083fb227",
    "curl_get_books_sorted": "6e87e9da9e47b139ee6633b979ddefac161bd7ee3006a66118067b2b866bcef5"
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}
```

### 4.2 Tests
```text
$ pytest -q
........                                                                 [100%]
8 passed in 0.35s
```

### 4.3 add100_report.json
```text
{
  "added_fail": 0,
  "added_ok": 100,
  "api_key_sha256": "cba3fc677861f91cf530088af40985fd6934154f98f09dfb8d1c86ec3458c1b5",
  "author_used": "Приходько Андрей Александрович",
  "count_requested": 100,
  "generated_utc": "2026-03-12T16:16:03.960115+00:00",
  "id_range": [9200, 9299],
  "sample_books": [
    {"author": "Приходько Андрей Александрович", "id": 9200, "isbn": "978-0-398-32750-7", "title": "Multi-layered systematic application [327c260e]"},
    {"author": "Приходько Андрей Александрович", "id": 9201, "isbn": "978-0-08-674523-1",  "title": "Secured 5thgeneration challenge [327c260e]"},
    {"author": "Приходько Андрей Александрович", "id": 9202, "isbn": "978-0-375-00038-6", "title": "Advanced contextually-based policy [327c260e]"},
    {"author": "Приходько Андрей Александрович", "id": 9203, "isbn": "978-0-292-23628-8", "title": "Proactive local standardization [327c260e]"},
    {"author": "Приходько Андрей Александрович", "id": 9204, "isbn": "978-0-304-81942-3", "title": "Synergistic fault-tolerant concept [327c260e]"}
  ],
  "tag": "327c260e"
}
```

### 5. Problems & fixes
Problem 1: Postman экспортировал файлы в /home/devasc/artifacts/day3/ вместо папки проекта.
Fix: Нашёл файлы через find и скопировал в нужное место:
```text
cp /home/devasc/artifacts/day3/postman_collection.json artifacts/day3/postman_collection.json
cp /home/devasc/artifacts/day3/postman_environment.json artifacts/day3/postman_environment.json
```

Problem 2: git push отклонён — remote содержал изменения которых не было локально.
Fix:
```text
git pull origin master --rebase
git push origin master
```
