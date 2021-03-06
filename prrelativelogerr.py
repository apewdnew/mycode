#! /usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import sys
from pyraf import iraf
import math
#import pdb
import matplotlib

#matplotlib.rc('text', usetex=True)
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

#pyraf command
p=[]
pe=[]
for i in range(360/5):
  q=[]
  iraf.plot(_doprint=0)
  iraf.pradprof("pi.fits", xinit=257.071, yinit=256.058, radius=50, az1=5*i, az2=5*i+5, center="no", list="yes",Stdout="profile1")
  x,y=loadtxt("profile1", usecols=(0,1), unpack=True)
  t=len(x)
  
  
#determine range of the profile
  for j in range(t):
    if x[j] < 15: continue
    q.append(y[j])
  p.append(mean(q))
  pe.append(std(q))
px=range(0,360,5)


#convert ADU to Jy
p=[a*0.000786 for a in p]
pe=[b*0.000786 for b in pe]

filename="pfaalarger10relativeerrjy.png"

#convert to log relative errorbar
k=len(p)
pe2=[]
for i in range(k):
  pe2.append(0.434*pe[i]/p[i])
p2=[math.log10(t) for t in p]
pe2up=[]
pe2down=[]
for i in range(k):
  pe2up.append(math.pow(10,pe2[i]+p2[i])-p[i])
  pe2down.append(p[i]-math.pow(10,p2[i]-pe2[i]))
  
#plot
fig=plt.figure(figsize=(8,6), dpi=120)
plot,=plt.semilogy(px,p)
#plot1,=plt.loglog(x,y,'or')  #'o' means scatter plot, plt.plot to plot normal plot
#plot2,=plt.loglog(xo,yo,'ob')
#plot following list
ylabel(r"$\rm F_{\nu}/Jy/sec^{2}$")
#xlabel(r"\textit{R/AU}")
#ylabel("ADU")
xlabel("Position angle")
xlim([0,360])
#pe2 = np.array(pe)
#pe2[pe>=p] = p[pe>=p]*.999999
plt.errorbar(px,p,yerr=[pe2down,pe2up],fmt='o')
#title(...)
ylim(1E-2,10)
yscale("log",nonposy='clip')
#xlim(...)
#plot.show()
#legend([plot1,plot2],["model","observation"],numpoints=1)
f=open('pe2up', 'w')
for tmp in pe2up:
  f.write("%s\n" % tmp)
f.close()
f2=open('pe2down', 'w')
for tmp in pe2down:
  print>>f2, tmp
f2.close()

savefig(filename)
clf()
