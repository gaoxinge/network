import time
from zhibo8 import current_live

room_id = 96254
live_oid = 0
while True:
    live, live_nid = current_live(room_id)
    if live_nid == live_oid:
        continue
    live_oid = live_nid
    for k, v in live.items():
        print k + ': ' + v
    time.sleep(2)