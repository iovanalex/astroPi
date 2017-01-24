#!/usr/bin/python
import time
from sense_hat import SenseHat

sense = SenseHat()

sense.set_imu_config(True, True, True)

while True:

#    orientation = sense.get_orientation_radians()
    orientation = sense.get_orientation_degrees()
    north = sense.get_compass()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    print("North: %s" % north)

