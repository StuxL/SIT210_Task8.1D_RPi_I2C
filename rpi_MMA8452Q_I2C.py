import smbus
import time

#MMA8452Q address 0x1d
bus = smbus.SMBus(1)

MODULE_ADDR = 0x1D
ADDR_OFFSET = 0x00
BYTE_LENGTH = 0x07

while(True):
        data = bus.read_i2c_block_data(MODULE_ADDR, ADDR_OFFSET, BYTE_LENGTH)

        xAccl = (data[1] * 256 + data[2]) / 16
        if xAccl > 2047 :
                xAccl -= 4096

        yAccl = (data[3] * 256 + data[4]) / 16
        if yAccl > 2047 :
                yAccl -= 4096

        zAccl = (data[5] * 256 + data[6]) / 16
        if zAccl > 2047 :
                zAccl -= 4096

        print "Acceleration in X-Axis : %d" %xAccl
        print "Acceleration in Y-Axis : %d" %yAccl
        print "Acceleration in Z-Axis : %d" %zAccl
        print "\n"
        time.sleep(1)
