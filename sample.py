#!/usr/bin/env python3

# From this repo: https://github.com/nesnes/YDLidarX2_python

import time
from LidarX2 import LidarX2

lidar = LidarX2("/dev/ttyUSB0")  

if not lidar.open():
	print("Cannot open lidar")
	exit(1)

t = time.time()

while time.time() - t < 20:  # Run for 20 seconds
	measures = lidar.getMeasures()  # Get latest lidar measures
	for m in measures:
		print(m.angle, m.distance)
	time.sleep(1)
lidar.close()
