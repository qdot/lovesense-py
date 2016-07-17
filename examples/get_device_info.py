from lovesense.comm import LovenseSyncSerial


def main():
    s = LovenseSyncSerial()
    s.open("/dev/tty.LVS-C011-SPPDev")
    s.deviceType()
    status = s.readStatus()
    print("Device Type: {}".format(status))
    s.deviceStatus()
    status = s.readStatus()
    print("Device Status: {}".format(status))
    s.batteryLevel()
    status = s.readStatus()
    print("Battery Level: {}".format(status))
    return 0

if __name__ == "__main__":
    main()
