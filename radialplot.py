#! /usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import sys
from pyraf import iraf
from scipy.optimize import curve_fit

dire="ss"

iraf.plot(_doprint=0)
iraf.pradprof("../sub_pi.fits", xinit=262, yinit=252, radius=230, az1=97, az2=103, center="no", list="yes",Stdout="list"+dire)
x,y=loadtxt("list"+dire, usecols=(0,1), unpack=True)
t=len(x)
p=int(round(max(x)))
r2=[]
aver1=[]
std1=[]
tmp=range(p)
#r2=[s+0.5 for s in tmp]

for j in range(p):
        q=[]
	for i in range(t):
		if ((x[i]>j) and (x[i]<=j+1)):
			q.append(y[i])
        if q==[]:
                continue
        r2.append(j+0.5)
	aver1.append(mean(q))
	std1.append(std(q))
	
#convert to log relative errorbar
k=len(aver1)
std2=[]
for i in range(k):
        std2.append(0.434*std1[i]/aver1[i])
p2=[math.log10(t) for t in aver1]
pe2up=[]
pe2down=[]
for i in range(k):
  pe2up.append(math.pow(10,std2[i]+p2[i])-aver1[i])
  pe2down.append(aver1[i]-math.pow(10,p2[i]-std2[i]))


f=open("prof"+dire,"w")
for z in range(len(r2)):
	print>>f,r2[z],aver1[z],pe2up[z],pe2down[z],std1[z]
f.close()

filename="list"+dire+".png"

#calculation
#x=array(range(0,100,5))
#x=float(x)/100
#y=1/(3.2+2.8*x)

#plot
x,y=loadtxt("prof"+dire, usecols=(0,1), unpack=True)
fig=plt.figure(figsize=(8,6), dpi=120)
plot,=plt.semilogy(x,y,'o')
#plot1,=plt.loglog(x,y,'or')  #'o' means scatter plot, plt.plot to plot normal plot
#plot2,=plt.loglog(xo,yo,'ob')
#plot following list
ylabel("ADU")
#xlabel(r"\textit{R/AU}")
#ylabel("ADU")
xlabel("Radus")
xlim([0,230])
#pe2 = np.array(pe)
#pe2[pe>=p] = p[pe>=p]*.999999

savefig(filename)
clf()

