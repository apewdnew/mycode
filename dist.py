#!/usr/bin/env python

# This is used to calculate the distance between two points in the 2D Cartesian coordinate system.

import math

def dist(x1,y1,x2,y2):
	x1,y1,x2,y2=[float(x1),float(y1),float(x2),float(y2)]
	dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
	print "The distance is: ",dist

x1,y1,x2,y2=raw_input("input coordinate:").split()
#x1,y1,x2,y2=1,2,3,4
dist(x1,y1,x2,y2)

