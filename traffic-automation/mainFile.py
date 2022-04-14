import multiThread as multi 
import time


sourceLane1 = r"E:\workspace\srcImg\s5.jpg"
sourceLane2 = r"E:\workspace\srcImg\s6.jpg"

sourceLane3 = r"E:\workspace\srcImg\s8.jpg"
sourceLane4 = r"E:\workspace\srcImg\s9.jpg"

print("Algorithm started")

startPoint = 1
while(True):
    if startPoint == 1 :
        print()
        multi.entry(sourceLane1, sourceLane2)
        startPoint = 2 
    if startPoint == 2:
        print()
        multi.entry(sourceLane3, sourceLane4)
        startPoint = 1 
    # n = int(input("\ncontinue??"))
    # if n == 0:
    #     break
