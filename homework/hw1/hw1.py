# written by Jason Haun

import math 

def arm3( angle1, angle2, angle3, length1, length2, length3 ):
	"Determine the location of the end effector of a 3 joint 2D arm"
	# first joint is assumed to be at (0,0)
	
	# convert angles to radians for math library
	angle1 = math.radians( angle1 )
	angle2 = math.radians( angle2 )
	angle3 = math.radians( angle3 )
	
	# find X,Y for joint between arm1 and arm2 relative to origin
	x1 = length1 * math.cos( angle1 )
	y1 = length1 * math.sin( angle1 )
	
	# find X,Y for joint between arm2 and arm3 relative to previous joint
	angle2 += angle1 # get total angle from X plane
	x2 = length2 * math.cos( angle2 )
	y2 = length2 * math.sin( angle2 )
	
	# find X, Y for end effector relative to previous joint
	angle3 += angle2 # sum of all angles gets angle relative to X plane
	x3 = length3 * math.cos( angle3 )
	y3 = length3 * math.sin( angle3 )
	
	# find X,Y for end effector relative to origin
	x = x1 + x2 + x3
	y = y1 + y2 + y3
	
	
	return (x, y)


# wrapper function for demonstration purposes 
angle1 = input("Angle 1: ")
angle2 = input("Angle 2: ")
angle3 = input("Angle 3: ")
length1 = input("Length 1: ")
length2 = input("Length 2: ")
length3 = input("Length 3: ")

print("End Effector at ", arm3(angle1, angle2, angle3, length1, length2, length3))

