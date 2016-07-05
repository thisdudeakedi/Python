#import simplegui
import time
from threading import Timer

# Event handler
def tick():
    print "tick!"

# Register handler
#timer = simplegui.create_timer(1000, tick)

t = 1 #counts down
while t>0:
      tick()
      time.sleep(1) #waits
      
# Start timer
t.start()
