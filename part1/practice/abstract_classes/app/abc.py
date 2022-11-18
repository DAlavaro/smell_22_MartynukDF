from abc import ABC


class Transport(ABC):
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def move(self):
        pass

    def stop(self):
        pass
