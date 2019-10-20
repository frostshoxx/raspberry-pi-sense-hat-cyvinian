import random
import time
import threading
import queue

from sense_hat import SenseHat

# define a class that encapsulate a Cyvinian
class Cyvinian:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = random.randint(0,7)
        self.y = random.randint(0,7)
    
    def move(self):
        #print('orig x: ' + str(self.x) + ', y: ' + str(self.y))
        self.x = self.x + random.randint(-1,1)
        if self.x < 0: self.x = 0
        if self.x > 7: self.x = 7
        self.y = self.y + random.randint(-1,1)
        if self.y < 0: self.y = 0
        if self.y > 7: self.y = 7
        #print('new x: ' + str(self.x) + ', y: ' + str(self.y))

def draw_cyvinians(max_cyvinians):
    c1 = Cyvinian("Roland", 9)
    while 1:
        sense.clear()
        c1.move()        
        sense.set_pixel(c1.x, c1.y, (0, random.randint(60,80), 0))
        time.sleep(0.70)

# Intialize sense hat
sense = SenseHat()
sense.clear()
max_cyvinians = queue.Queue()
max_cyvinians.put(random.randint(10,64))

led_rendering_thread = threading.Thread(target = draw_cyvinians(max_cyvinians))
led_rendering_thread.start()
