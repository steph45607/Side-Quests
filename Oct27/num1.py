import time

def delay(msg, sec):
    time.sleep(sec) #delay code in sec
    print(msg) #print msg parameter

delay("This is message",5)