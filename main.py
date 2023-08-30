import webview
from src.api import api
from src.window import win

_api = api()
_win = win()

window = webview.create_window('Soundcloud', 'https://soundcloud.com', js_api=_api, min_size=(1220, 780))
webview.start(_win.worker, window, private_mode=False, debug=False)
