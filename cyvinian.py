import random
import time
import threading
import queue

from sense_hat import SenseHat

# define a class for orb of life, which generate another Cyvinian
class OrbOfLife:
    
    def __init__(self):
        self.x = random.randint(0,7)
        self.y = random.randint(0,7)
    
    def draw(self):
        sense.set_pixel(self.x, self.y, (0, 0, random.randint(100,150)))

    def move(self):        
        self.x = self.x + random.randint(-1,1)
        self.y = self.y + random.randint(-1,1)
        # make sure the orb of life doesn't go off the board
        if self.x < 0: self.x = 0
        if self.x > 7: self.x = 7            
        if self.y < 0: self.y = 0
        if self.y > 7: self.y = 7
        
    def respawn(self):
        self.x = random.randint(0,7)
        self.y = random.randint(0,7)
        
# define a class that encapsulate a Cyvinian
class Cyvinian:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = random.randint(0,8)
        self.y = random.randint(0,8)
        self.hunger = random.randint(0,10)

    def is_fed(self):
        if self.hunger == 0:
            return True
        else:
            return False
        
    def is_hungry(self):
        if self.hunger > 10:
            if self.hunger >= 20: self.hunger = 19
            return True
        else:
            return False
        
    def move(self, orb_of_life):
        # seek for orb of life if hungry
        if (self.is_hungry() == True):
            if self.x < orb_of_life.x: self.x = self.x + 1
            if self.x > orb_of_life.x: self.x = self.x - 1
            if self.y < orb_of_life.y: self.y = self.y + 1
            if self.y > orb_of_life.y: self.y = self.y - 1
        else:
            # otherwise, just walk randomly
            self.x = self.x + random.randint(-1,1)
            self.y = self.y + random.randint(-1,1)
            
        # make sure the Cyvinian doesn't go off the board
        if self.x < 0: self.x = 0
        if self.x > 7: self.x = 7            
        if self.y < 0: self.y = 0
        if self.y > 7: self.y = 7
        
        # Check if the Cyvinian consume orb of life
        if self.x == orb_of_life.x and self.y == orb_of_life.y:
            self.hunger = 0
            orb_of_life.respawn()
        else:
        # Otherwise, add more hunger
            self.hunger = self.hunger + 1 
    
    def draw(self):
        if self.is_fed() == True:
            color = (random.randint(60,80), random.randint(60,80), 0)
        elif self.is_hungry() == True:
            color = (random.randint(60,80),0 , 0)
        else:
            color = (0, random.randint(60,80), 0)
        sense.set_pixel(self.x, self.y, color)

def draw_cyvinians(max_cyvinians):
    c1 = Cyvinian("Roland", 3)
    c2 = Cyvinian("Vanessa", 5)
    o1 = OrbOfLife()
    while 1:
        sense.clear()
        o1.move()
        c1.move(o1)
        c2.move(o1)
        o1.draw()
        c1.draw()
        c2.draw()
        time.sleep(0.25)

# Intialize sense hat
sense = SenseHat()
sense.clear()
max_cyvinians = queue.Queue()
max_cyvinians.put(random.randint(10,64))

led_rendering_thread = threading.Thread(target = draw_cyvinians(max_cyvinians))
led_rendering_thread.start()
