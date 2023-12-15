import time, pypresence

class RPC:

    def __init__(self):      
        try:
            self.RPC = pypresence.Presence('1146454000795910215')
            self.RPC.connect()
            print('[py] ~> rpc running')
        except:
            self.RPC = None
            print('[py] ~> rpc not running')

    def update(self, data: dict):
        print('[py] ~> updated rpc')
        
        if self.RPC != None:

            if data['isPlaying']:
                start_t = time.time() + data['currentTime']['minutes']  * 60 + data['currentTime']['seconds']
                end_t   = time.time() + data['duration']['minutes'] * 60 + data['duration']['seconds']

                if len(data['title']) < 2:
                    data['title'] += "⠀⠀⠀"

                if len(data['author']) < 2:
                    data['author'] += "⠀⠀⠀"

                self.RPC.update(
                    large_image         = data['cover'], 
                    large_text          = 'github.com/payratted',
                    state               = data['title'], 
                    details             = data['author'],
                    buttons             = [{"label": "Listen along", "url": data['url']}],
                    start               = start_t,
                    end                 = end_t
                )  

            else:
                self.RPC.update(
                    large_image         = 'logo', 
                    large_text          = 'github.com/payratted',
                    state               = 'Discovering...'
                ) 
