import threading
import interestRegion as roi
import time


totalVehicles = 0
lbTime = 0.5
limit = 120

def lane1(src1):
    data = roi.initialize(src1)
    print("First lane has {} vehicles.".format(data[1])) 
    global totalVehicles
    totalVehicles += data[1]

def lane2(src2):
    data = roi.initialize(src2)
    print("Second lane has {} vehicles.".format(data[1]))
    global totalVehicles
    totalVehicles += data[1]

def entry(sourceLane1, sourceLane2):
    global totalVehicles
    totalVehicles = 0

    t1 = threading.Thread(target=lane1, args=(sourceLane1,))
    t2 = threading.Thread(target=lane2, args=(sourceLane2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both lanes have {} vehicles collectively.".format(totalVehicles)) 
    average = round(totalVehicles/2)
    print("Average vehicle count is {}".format(average))
    timeNeed = lbTime * average
    if timeNeed >= limit:
        timeNeed = limit
    print("{} seconds will be sufficient".format(round(timeNeed)))
    print("Going to sleep now")
    #time.sleep(timeNeed - 7)
    #time.sleep(2)
    print("Waiting for next Lane...")