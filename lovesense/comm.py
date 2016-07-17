from .base import LovesenseBase
from .errors import LovesenseIOError


class LovesenseSerialSync(LovesenseBase):
    def __init__(self, port):
        super(LovesenseSerialSync, self).__init__()
        # Allow derived classes to set up a port to mock serial ports for
        # tests. There are cleaner ways to mock this, but this will do for now.
        if not hasattr(self, "port"):
            # Check argument validity
            import serial
            if not port or type(port) is not str:
                raise LovesenseIOError("Serial port name is missing or is not string!")

            # Just create the port. It's bluetooth so options don't really
            # matter.
            self.port = serial.Serial(port)

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
