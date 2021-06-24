from threading import Thread
import time

def BigBox(color):
    while True:
        print(color,"Big box is open")
        time.sleep(5)
        print(color,"Big box is closed")
        time.sleep(5)
def SmallBox(color):
    while True:
        print(color,"Small box is open")
        time.sleep(1)
        print(color,"Small box is closed")
        time.sleep(1)

bigBoxThread = Thread(target=BigBox,args=('red',))
smallBoxThread = Thread(target=SmallBox,args=('blue',))
bigBoxThread.daemon=True
smallBoxThread.daemon=True
bigBoxThread.start()
smallBoxThread.start()
while True:
    pass
