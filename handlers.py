import os
import string

from dciphrd.sc2remix.models import SC2Replay
from dciphrd.sc2remix.sc2remix import SC2Remix
from dciphrd.sc2remix.utils import int_to_base62

REPLAY_PATH = "/home/django/static/files/replays/"

def handle_uploaded_replay(f):
    filename = f.name
    r = SC2Replay(filename=filename)
    r.save()
    id_str = int_to_base62(r.id)
    save_path = REPLAY_PATH+id_str
    os.mkdir(save_path)
    file_path = save_path+'/'+filename
    save_file = open(file_path, 'wb+')
    for chunk in f.chunks():
        save_file.write(chunk)
    save_file.close()
    SC2Remix(file_path).zip()
    return r.id
