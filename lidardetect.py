
import PyLidar3
import time # Time module
import math
#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
x=[]
y=[]
for _ in range(360):
    y.append(0)
    x.append(0)
port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size)


data = []
if(Obj.Connect()): #continuous loop
    print("hello")
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 

    #Calculate distance and insert conditions into for loop
       # print(next(gen))
    
    while(time.time() - t) < 5:
        print(next(gen))
        time.sleep(0.5)
    for angle in range(0,360):
        #data = next(gen)
        if(data[angle]>1000):
            x[angle] = data[angle] * math.cos(math.radians(angle)) #convert to radians
            y[angle] = data[angle] * math.sin(math.radians(angle)) #convert to radians
            print("The x angle is : " + x[angle])
            print("The y angle is : " + y[angle])
            #time.sleep(0.5)
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
