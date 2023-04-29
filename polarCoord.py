import matplotlib.pyplot as plt

from LidarX2 import LidarX2
import sys
import time

if __name__ == '__main__':
    print("Reaching")
    angle = []
    dist = []
    lidar = LidarX2("/dev/ttyUSB0")
    
    plt.axes(projection = "polar")

    if not lidar.open():
        print("Cannot open lidar")
        exit(1)
    t = time.time()
   
    angle.append(0)
    while time.time() - t < 5:
        measures = lidar.getMeasures()
        for m in measures:
            
            if(m.angle > angle[-1]):
                angle.append(m.angle)
                dist.append(m.distance)
                if len(angle) == 2 and angle[0] == 0:
                    angle = angle[1:]
                    plt.polar(angle, dist, 'g.')
                else:
                    plt.polar(angle, dist, 'g.')
        time.sleep(1)
    lidar.close()

    plt.title("Angle and distance in Polar")
    plt.show()




