#!/usr/bin/env python3

from __future__ import annotations
import hashlib, json, os, sys
from pathlib import Path
import requests

WEBEX_BASE = "https://webexapis.com/v1"
ART_WEBEX = Path("artifacts/day5/webex")

def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()[:8]

def dump_json(obj, path: Path) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def webex_get(token: str, endpoint: str, params=None):
    r = requests.get(f"{WEBEX_BASE}/{endpoint}",
                     headers={"Authorization": f"Bearer {token}"},
                     params=params or {}, timeout=10)
    return r.status_code, r.json()

def webex_post(token: str, endpoint: str, body: dict):
    r = requests.post(f"{WEBEX_BASE}/{endpoint}",
                      headers={"Authorization": f"Bearer {token}",
                               "Content-Type": "application/json"},
                      json=body, timeout=10)
    return r.status_code, r.json()

def run_webex(token: str, th8: str, name: str) -> bool:
    ART_WEBEX.mkdir(parents=True, exist_ok=True)

    # 1. Me

    sc, me = webex_get(token, "people/me")
    dump_json(me, ART_WEBEX / "me.json")
    print(f"  me: {sc} {me.get('displayName','?')}")

    # 2. Rooms list

    sc, rooms = webex_get(token, "rooms", {"max": 10})
    dump_json(rooms, ART_WEBEX / "rooms_list.json")
    print(f"  rooms list: {sc} count={len(rooms.get('items',[]))}")

    # 3. Create room

    room_title = f"DevNet Day5 {th8} - {name}"
    sc, room = webex_post(token, "rooms", {"title": room_title})
    dump_json(room, ART_WEBEX / "room_create.json")
    room_id = room.get("id", "")
    print(f"  room create: {sc} id={room_id[:20]}...")

    # 4. Post message

    msg_text = f"Hello from DevNet Day5! token_hash8={th8} student={name}"
    sc, msg = webex_post(token, "messages",
                         {"roomId": room_id, "text": msg_text})
    dump_json(msg, ART_WEBEX / "message_post.json")
    print(f"  message post: {sc}")

    # 5. List messages

    sc, msgs = webex_get(token, "messages", {"roomId": room_id, "max": 5})
    dump_json(msgs, ART_WEBEX / "messages_list.json")
    print(f"  messages list: {sc} count={len(msgs.get('items',[]))}")

    return th8 in room_title

def main() -> int:
    st_token = os.getenv("STUDENT_TOKEN", "").strip()
    st_name  = os.getenv("STUDENT_NAME",  "").strip()
    st_group = os.getenv("STUDENT_GROUP", "").strip()
    webex_token = os.getenv("WEBEX_TOKEN", "").strip()

    if not st_token or not st_name or not st_group:
        print("ERROR: set STUDENT_TOKEN, STUDENT_NAME, STUDENT_GROUP", file=sys.stderr)
        return 3

    th8 = token_hash8(st_token)
    print(f"token_hash8={th8}")

    if webex_token:
        print("Running Webex...")
        try:
            run_webex(webex_token, th8, st_name)
        except Exception as e:
            print(f"Webex error: {e}")
    else:
        print("WEBEX_TOKEN not set — skipping Webex")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
