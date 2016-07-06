#! /usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import sys

x,y=loadtxt("bprof", usecols=(0,1), unpack=True)
t=len(x)
p=int(round(max(x)))
aver1=[]
std1=[]
tmp=range(p)
r2=[s+0.5 for s in tmp]

for j in range(p):
        q=[]
	for i in range(t):
		if ((x[i]>j) and (x[i]<=j+1)):
			q.append(y[i])
	aver1.append(mean(q))
	std1.append(std(q))

output=[r2,aver1,std1]

f=open("bprofbin","w")
for z in range(len(r2)):
	print>>f,r2[z],aver1[z],std1[z]
f.close()

