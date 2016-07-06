#! /usr/bin/env python


#This is used to calculate the angular resolution of telescope at different wavelength.
#Yi Yang, 2015/06/11

import os
import platform
#Calculate the resolution of telescope

wavelength=float(raw_input("input wavelength in micrometer:"))
d=float(raw_input("input diameter in meter:"))

trwave=wavelength/1000000
theta=1.22*trwave/d
arcsec=theta*180*3600/3.1415926

print "resolution is",arcsec,"arcsec"

#Judge the operating system
if (platform.system()=="Windows"):
	os.system('pause')
