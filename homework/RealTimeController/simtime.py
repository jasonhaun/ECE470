import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
import threading
import signal

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

def handler(signum, frame):
	global dt
	global t1
	global count
	t2 = time.time()
	dt = t2 - t1
	t1 = t2
	count += 1
	if (count>5):
		count = 1
	elif (count == 5):
		print dt

signal.signal(signal.SIGVTALRM, handler)
count = 1
dt = 0
dtr = 0
t1 = time.time()
t1r = t1
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.2)
while(True):
	x = 0
