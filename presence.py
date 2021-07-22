from parse import *
from pypresence import Presence
import psutil

client_id = "866670296051613716"
# client_id = "866599322175012894" pepega
RPC = Presence(client_id)
RPC.connect()
print('connected')
time.sleep(15) # wait a bit for game to launch

# get pids of celeste
pids = []
for proc in psutil.process_iter():
    if "Celeste" in proc.name():
        pids.append(proc.pid)

while (True):
    print('updating')
    for pid in pids:
        if not psutil.pid_exists(pid):
            pids.remove(pid)
    if len(pids) == 0:
        quit()

    soup = get_soup()
    RPC.update(large_image="madeline",
               large_text=get_stats(soup),
               state=get_mode(soup),
               details=get_chapter(soup),
               start=get_time())
    print('updated')
    time.sleep(60)
