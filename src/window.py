import time

class win:

    def __init__(self):
        pass
    
    def worker(self, window):

        while True:
            window.evaluate_js('''

                var playControl =   document.querySelector(".playControl");
                var is_paused = playControl.className.includes('playing') ? false : true

                var img =           document.querySelector(".sc-artwork-4x").style.backgroundImage.slice(4, -1).replace(/"/g, "").replaceAll("50", "500");

                var author =        document.querySelector(".playbackSoundBadge__lightLink").innerHTML;

                var song_url =     document.querySelector(".playbackSoundBadge__titleLink").href;
                var title =         document.querySelector(".playbackSoundBadge__titleLink > span:nth-child(2)").innerHTML;

                var curr_time =     document.querySelector(".playbackTimeline__timePassed > span:nth-child(2)").innerHTML.split(":");
                var ttal_time =     document.querySelector(".playbackTimeline__duration > span:nth-child(2)").innerHTML.split(":");

                var data = {
                    is_paused: is_paused,
                    song_url: song_url,
                    author: author,
                    title: title, 
                    img: img, 
                    curr_time: {
                        minutes: curr_time[0],
                        seconds: curr_time[1]
                    },
                    ttal_time:{
                        minutes: ttal_time[0],
                        seconds: ttal_time[1]
                    },
                };
              
                pywebview.api.set_song_data(data)

            ''')
            time.sleep(1)
