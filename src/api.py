import time
from src.rpc import rpc

class api:

    def __init__(self):

        self.song_data = {
            "is_paused":    None,
            "img":          None,
            "title":        None,
            "author":       None,
            "song_url":     None,
            "curr_time":    {
                "minutes":  None,
                "seconds":  None
            },
            "ttal_time":    {
                "minutes":  None,
                "seconds":  None
            }
        }

        
        self._rpc = rpc()
        self._rpc.run()

    def set_song_data(self, data):
        # i dont know what im even doing at this point alr?
        
        self.song_data["is_paused"] = data["is_paused"]

        self.song_data["ttal_time"]['minutes'] = int(data['ttal_time']['minutes']) - int(data['curr_time']['minutes'])
        self.song_data["ttal_time"]['seconds'] = int(data['ttal_time']['seconds']) - int(data['curr_time']['seconds'])
        
        
        if self.song_data['title'] is None or self.song_data['title'] != data['title']:
            

            self.song_data["img"]                   = data["img"]
            self.song_data["title"]                 = data["title"]
            self.song_data["author"]                = data["author"]
            self.song_data["song_url"]              = data["song_url"]
            
            self.song_data["curr_time"]['minutes']  = int(data['curr_time']['minutes']) 
            self.song_data["curr_time"]['seconds']  = int(data['curr_time']['seconds'])          
            
        self._rpc.update(self.song_data)
