from liblovense.comm import LovenseSyncSerial

def main():
    s = LovenseSyncSerial()
    s.open("/dev/tty.LVS-C011-SPPDev")
    s.deviceType()
    status = s.readStatus()
    print "Device Type: %s" % (status)
    s.deviceStatus()
    status = s.readStatus()
    print "Device Type: %s" % (status)
    s.batteryLevel()
    status = s.readStatus()
    print "Battery Level: %s" % (status)
    return 0

if __name__ == "__main__":
    main()
