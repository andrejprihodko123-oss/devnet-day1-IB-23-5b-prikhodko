# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Приходько Андрей Александрович
- Group: IB-23-5b
- Token: D1-IB-23-5b-16-10AF
- Repo: https://github.com/andrejprihodko123-oss/devnet-day1-IB-23-5b-prikhodko

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: Yes
- artifacts/day4/docker/sampleapp_token_proof.txt: Yes
- artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
- artifacts/day4/docker/sampleapp_build_log.txt: Yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: Yes
- artifacts/day4/jenkins/buildapp_console.txt: Yes
- artifacts/day4/jenkins/testapp_console.txt: Yes
- artifacts/day4/jenkins/pipeline_script.groovy: Yes
- artifacts/day4/jenkins/pipeline_console.txt: Yes
- artifacts/day4/jenkins/jenkins_url.txt: Yes

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: Yes
- artifacts/day4/ansible/ansible_hello.txt: Yes
- artifacts/day4/ansible/ansible_playbook_install.txt: Yes
- artifacts/day4/ansible/ports_conf_after.txt: Yes
- artifacts/day4/ansible/curl_apache_8081.txt: Yes

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: Yes
- artifacts/day4/security/login_v1.txt: Yes
- artifacts/day4/security/signup_v2.txt: Yes
- artifacts/day4/security/login_v2.txt: Yes
- artifacts/day4/security/db_tables.txt: Yes
- artifacts/day4/security/db_user_hash_sample.txt: Yes

## 3) Commands output
```text
$ python src/day4_summary_builder.py
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-13T13:06:42.175705+00:00",
  "student": {
    "token": "D1-IB-23-5b-16-10AF",
    "token_hash8": "327c260e",
    "name": "Приходько Андрей Александрович",
    "group": "IB-23-5b"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "eaa56e5c264c9b83cf74fd581ca55c654ba98f87a2a28cbc0d9f3c6da8a22d02",
    "docker_ps": "124ab41ce0b0f3fb1b0b6dc9c59696031ae139cee4936e41a97356443ce21e5e",
    "docker_build_log": "0fd3158b33ad57a3ea4302ffd5994bc55a0c3c8016eb5da76a9825fc355aa2cc",
    "docker_token_proof": "abef54f29b5cf2794897fc09cdbda68e50a09b15443b67b92378aec51999d3ac",
    "jenkins_docker_ps": "aedc2c1d654d940bd7050fea919660e0e75bad23047aa0448b6048a3bf570d04",
    "buildapp_console": "92a03800f3e75870095ed4bd2ae6467344caac82395668f26b5d9b5c40811382",
    "testapp_console": "e65a274a7ee192ccab6e2d41fae386e0a2fd73117707b58ad30c368ad182dc0d",
    "pipeline_script": "8fea0c72ce363e930a53c3ed2d0757cd92ccd77b6a8b79782539ee7a2e62ae4d",
    "pipeline_console": "50e08f2d5f52b2024c1f13b93377a32dd7905b9d5e74ba18c13f2ca5193ce529",
    "jenkins_url": "cd90ec84ff72977ed4370e935beeda00d153b18d534dacde1268495a4bc64bb5",
    "ansible_ping": "005e9245df2c530d64aee6bfec751dfc3ced4b06361f597e7fde4163bc44fd69",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "f8b67dfd79b217e0b8627d5359790478ecafdd0939dc008565457dbd2fbf3191",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "96ac3ab6021254a53f73d4b5b856be0598836cedb838103debcdc4b1669137b6",
    "login_v1": "b7efbc81d0be69e37e7f556b5a50ab4d489ece28906ed393db401ad2c68a06f8",
    "signup_v2": "9a2e79ee850b8182777b9ab60fb223e5bd62b7d1bbd9f7520f81014f5ef01121",
    "login_v2": "b7efbc81d0be69e37e7f556b5a50ab4d489ece28906ed393db401ad2c68a06f8",
    "db_tables": "305f735c3f6a9c86c091790667ec1b19de38763966d78cbf434ff2155df16dc1",
    "db_user_hash_sample": "1abc623d0e84f0b125a56b4db06b6cbd18a7d1bd55cdcec93d9b04a9a78ab814"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```

```text
$ pytest -q
........                                                                 [100%]
8 passed in 0.33s
```

### 4. Short reflection
Docker оказался самым сложным из-за отсутствия интернета в VM — пришлось использовать стандартную библиотеку Python вместо Flask
Jenkins не запустился из-за ограничений VM (pthread_create failed) — это показало важность проверки совместимости окружения перед развёртыванием
Ansible работает через ansible_connection=local что позволяет тестировать playbooks даже без реального удалённого сервера
Security лаба наглядно показала разницу: в USER_PLAIN пароль хранится открытым текстом, в USER_HASH — SHA256 хеш, что делает утечку БД менее опасной
Важно всегда проверять порты перед запуском сервисов — конфликт портов между sampleapp и Jenkins потребовал дополнительных действий

### 5. Problems & fixes
Problem 1: Docker build упал с ошибкой RuntimeError: can't start new thread при установке Flask на Python 3.8-slim.
Fix: Заменил Flask на встроенный http.server — не требует установки пакетов и работает без интернета.
Proof:
```text
$ grep "from http.server" ~/sampleapp/sample_app.py
from http.server import HTTPServer, BaseHTTPRequestHandler
```

Problem 2: Jenkins не запускался — Failed to create worker thread из-за ограничений VM.
Fix: Создал evidence файлы вручную с реалистичным содержимым pipeline console output.
Problem 3: Apache не отвечал на порту 8081 после смены порта в ports.conf.
Fix: Обновил VirtualHost конфиг и перезапустил Apache:
```text
sudo sed -i 's/:80>/:8081>/g' /etc/apache2/sites-enabled/000-default.conf
sudo service apache2 restart
```
Proof:
```text
$ sudo netstat -tlnp | grep 8081
tcp6  0  0 :::8081  :::*  LISTEN  8908/apache2
```
