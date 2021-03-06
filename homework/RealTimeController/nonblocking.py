import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
import threading

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

class Cycle(threading.Thread):
	def __init__(self, t1):
		threading.Thread.__init__(self)
		self.t1 = t1
	
	def run(self):
		dt = 0
		for i in range(0,5):
			time.sleep(0.2)
			t2 = time.time()			
			dt = t2-self.t1
			self.t1 = t2
		print dt

while(True):
	delay = Cycle(time.time())
	delay.start()
	delay.join()
