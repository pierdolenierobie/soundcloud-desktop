import time, threading
from pypresence import Presence 

class rpc:

    def __init__(self):
        self.RPC = Presence("1146454000795910215")
        pass

    def update(self, data):
 
        if data['is_paused']:

            self.RPC.update(
                large_image = 'logo', 
                state='Discovering...'
            ) 

        else:

            start_t = time.time() + data['curr_time']['minutes']  * 60 + data['curr_time']['seconds']
            end_t = time.time() + data['ttal_time']['minutes'] * 60 + data['ttal_time']['seconds']

            if len(data['title']) < 2:
                data['title'] += "⠀⠀⠀"

            if len(data['author']) < 2:
                data['author'] += "⠀⠀⠀"

            self.RPC.update(
                large_image     = data['img'], 
                state           = data['title'], 
                details         = data['author'],
                buttons         = [{"label": "Listen along", "url": data['song_url']}],
                start           = start_t,
                end             = end_t
            )  

    def run(self):
        self.RPC.connect()
