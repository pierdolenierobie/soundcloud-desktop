from src.rpc import RPC

class Api:

    def __init__(self):
        self.rpc = RPC()
        pass

    def setData(self, data):
        self.rpc.update(data)
        pass
