import webview
from src.api import Api
from src.client import Client

if __name__ == '__main__':
    api = Api()
    client = Client()

    window = webview.create_window('Soundcloud', 'https://soundcloud.com', js_api=api, min_size=(1220, 780))
    webview.start(client.windowWorker, window, private_mode=False, debug=False)
