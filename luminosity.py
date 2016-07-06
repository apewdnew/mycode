#!/usr/bin/env python
import math

msun=-26.8
r=float(raw_input("input radius:"))
d=float(raw_input("input distance:"))
albedo=1

m=msun+2.5*math.log10(d**2/(r**2*albedo))

print m

