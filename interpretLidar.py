import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
import sys
import time
from LidarX2 import LidarX2

angle = []
dist = []
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(projection='polar')
def animate(i):
    
    ax1.clear()
    ax1.plot(angle,dist)
if __name__ == '__main__':

    lidar = LidarX2("/dev/ttyUSB0")

    if not lidar.open():
        print("Cannot open lidar")
        exit(1)
    t = time.time()
    
    while time.time() - t < 5:
        measures = lidar.getMeasures()
        for m in measures:
            angle.append(m.angle)
            dist.append(m.distance)
        time.sleep(1)
    lidar.close()
    ani = animation.FuncAnimation(fig, animate, interval=1000)

    plt.show()
    '''
    plt.title("Angle vs Distance")
    plt.axes(projection = "polar")
    #Activate plot before 20 second sample
    while time.time() - t < 20:
        measures = lidar.getMeasures()
        
        plt.axes(projection = "polar")
        plt.polar(angle, dist)
        
plt.show()
    ''' 
    '''
    for line in open(sys.argv[1], "r"):
        lines = [i for i in line.split()]

        angle.append(float(lines[0]))
        dist.append(float(lines[1]))
    '''
#plt.xlabel("Angle")
#plt.ylabel("Dist")
#plt.yticks(dist)
    plt.savefig("FigureData.png")

