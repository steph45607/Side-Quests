import time

def delay(msg, sec):
    time.sleep(sec)
    print(msg)

delay("This is message",5)