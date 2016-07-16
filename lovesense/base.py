class LovesenseCommandBuilder:

    START_ACCELEROMETER_STREAM_COMMAND = "StartMove:1;"
    STOP_ACCELEROMETER_STREAM_COMMAND = "StopMove:1;"
    CHANGE_ROTATION_DIRECTION_COMMAND = "RotateChange;"
    POWER_OFF_COMMAND = "PowerOff;"
    BATTERY_LEVEL_COMMAND = "BatteryLevel;"
    DEVICE_TYPE_COMMAND = "DeviceType;"
    DEVICE_STATUS_COMMAND = "DeviceStatus:1;"
    OK_STATUS = "OK;"
    ERROR_STATUS = "ER;"

    def setVibrateCommand(self, level):
        if level > 255 or level < 0:
            return None
        return "Vibrate:%s;" % (level)

    def setRotateCommand(self, level):
        if level > 255 or level < 0:
            return None
        return "Rotate:%s;" % (level)

    def setAirLevelCommand(self, level):
        return "Air:Level:%s" % (level)

    def inflateCommand(self, level):
        return "Air:In:%s" % (level)

    def deflateCommand(self, level):
        return "Air:Out:%s" % (level)


class LovesenseBase(LovesenseCommandBuilder):
    def __init__(self):
        pass

    def open(self, com_port):
        raise RuntimeError("IMPLEMENT ME")

    def close(self):
        raise RuntimeError("IMPLEMENT ME")

    def writeCommand(self, command):
        raise RuntimeError("IMPLEMENT ME")

    def readCharacter(self):
        raise RuntimeError("IMPLEMENT ME")

    def readStatus(self):
        out = ""
        while True:
            ch = self.readCharacter()
            if not ch:
                continue
            out += ch
            if ch == ';':
                return out

    def setVibrate(self, level):
        cmd = self.setVibrateCommand(level)
        if not cmd:
            return
        self.writeCommand(cmd)

    def setRotate(self, level):
        cmd = self.setRotateCommand(level)
        if not cmd:
            return
        self.writeCommand(cmd)

    def startAccelerometerStream(self):
        self.writeCommand(self.START_ACCELEROMETER_STREAM_COMMAND)

    def stopAccelerometerStream(self):
        self.writeCommand(self.STOP_ACCELEROMETER_STREAM_COMMAND)

    def changeRotationDirection(self):
        self.writeCommand(self.CHANGE_ROTATION_DIRECTION_COMMAND)

    def powerOff(self):
        self.writeCommand(self.POWER_OFF_COMMAND)

    def batteryLevel(self):
        self.writeCommand(self.BATTERY_LEVEL_COMMAND)

    def deviceType(self):
        self.writeCommand(self.DEVICE_TYPE_COMMAND)

    def deviceStatus(self):
        self.writeCommand(self.DEVICE_STATUS_COMMAND)

    def setAirLevel(self, level):
        self.writeCommand("Air:Level:%s" % (level))

    def inflate(self, level):
        self.writeCommand("Air:In:%s" % (level))

    def deflate(self, level):
        self.writeCommand("Air:Out:%s" % (level))
