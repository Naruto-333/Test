from machine import Pin
import utime
import time

abort_time=22.73


delta=0

pins=[
    Pin(15,Pin.OUT),#B-1A
    Pin(17,Pin.OUT),#B-1B
    Pin(16,Pin.OUT),#A-1A
    Pin(14,Pin.OUT)#A-1B
    ]

full_step_sequence=[
    [1,1,0,0],
    [1,1,0,0],
    [1,1,0,0],
    [0,0,0,0]
    ]

start=time.time()

while delta <= abort_time:
    delta = time.time()-start
    for step in full_step_sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(.001)
        
            