import random
import time
import threading
import queue

from sense_hat import SenseHat

def draw_cyvinians(max_cyvinians):
    while 1:
        sense.clear()
        cyvinian_count = 0
        stop_at = max_cyvinians.get()
        while cyvinian_count < stop_at:
            sense.set_pixel(random.randint(0,7), random.randint(0,7), (0, random.randint(20,80), 0))
            sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(20,80), 0, 0))
            sense.set_pixel(random.randint(0,7), random.randint(0,7), (0, 0, random.randint(20,80)))
            #sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            #sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(40,60), random.randint(40,60), random.randint(40,60)))
            cyvinian_count += 1    
        time.sleep(1)
        max_cyvinians.put(random.randint(10,64))

# Intialize sense hat
sense = SenseHat()
sense.clear()
max_cyvinians = queue.Queue()
max_cyvinians.put(random.randint(10,64))

thread1 = threading.Thread(target = draw_cyvinians(max_cyvinians))
thread1.start()
