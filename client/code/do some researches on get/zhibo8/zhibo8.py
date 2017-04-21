import time
import requests
from collections import defaultdict

def current_live(room_id):
    response = requests.get('http://dingshi4pc.qiumibao.com/livetext/data/cache/max_sid/{room_id}/0.htm?'.format(room_id=room_id))
    live_id = int(response.text)
    response = requests.get('http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/{room_id}/0/lit_page_2/{live_id}.htm'.format(
        room_id = room_id,
        live_id = live_id,
    ))
    if response.status_code == 404:
        live_id -= 1
        response = requests.get('http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/{room_id}/0/lit_page_2/{live_id}.htm'.format(
            room_id = room_id,
            live_id = live_id,
        ))
    data = response.json()
    live = {}
    for d in data:
        live[d['user_chn']] = d['live_text']
    return live, live_id

def current_comment(room_id):
    t = time.localtime()
    response = requests.get('http://dan.zhibo8.cc/data/{year}/nba/{month}{day}{room_id}_count.htm'.format(
        year    = t.tm_year,
        month   = '0' + str(t.tm_mon) if t.tm_mon < 10 else t.tm_mon,
        day     = t.tm_mday,
        room_id = room_id,
    ))
    data = response.json()
    num = data['num']/data['per_page']
    response = requests.get('http://dan.zhibo8.cc/data/{year}/nba/{month}{day}{room_id}_{num}.htm'.format(
        year    = t.tm_year,
        month   = '0' + str(t.tm_mon) if t.tm_mon < 10 else t.tm_mon,
        day     = t.tm_mday,
        room_id = room_id,
        num     = num,
    ))
    data = response.json()
    comment = defaultdict(list)
    for d in data:
        comment[d['room']].append(d['content'])
    return comment, num

if __name__ == '__main__':
    room_id = 96254
    live, live_id = current_live(room_id)
    for k, v in live.items():
        print k + ': ' + v
    comment, num = current_comment(room_id)
    for k, v in comment.items():
        for c in v:
            print k + ': ' + c