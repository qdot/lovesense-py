from .base import LovesenseBase
from serial import Serial


class LovesenseSyncSerial(LovesenseBase):
    def __init__(self):
        super(LovesenseBase, self).__init__()
        self.port = None

    def open(self, com_port):
        self.port = Serial(com_port)

    def close(self):
        if not self.port:
            return
        self.port.close()
        self.port = None

    def readCharacter(self):
        if not self.port:
            raise RuntimeError("How did we get here?")
        return self.port.read()

    def writeCommand(self, command):
        if not self.port:
            raise RuntimeError("How did we get here?")
        return self.port.write(command)
