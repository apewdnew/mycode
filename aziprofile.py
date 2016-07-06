#! /usr/bin/env python
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import sys
from pyraf import iraf
#import pdb


#pyraf command
p=[]
pe=[]
for i in range(360/5):
  q=[]
  iraf.plot(_doprint=0)
  iraf.pradprof("pi.fits", xinit=257.071, yinit=256.058, radius=50, az1=5*i, az2=5*i+5, center="no", list="yes",Stdout="profile1")
  x,y=loadtxt("profile1", usecols=(0,1), unpack=True)
  t=len(x)
  for j in range(t):
    if x[j] < 15: continue
    q.append(y[j])
  p.append(mean(q))
  pe.append(std(q))
px=range(0,360,5)
filename="pfaalarger15err.png"

fig=plt.figure(figsize=(8,6), dpi=120)
plot,=plt.semilogy(px,p)
#plot1,=plt.loglog(x,y,'or')  #'o' means scatter plot, plt.plot to plot normal plot
#plot2,=plt.loglog(xo,yo,'ob')
#plot following list
#ylabel(r"$F_{\nu}/Jy/sec^{2}$")
#xlabel(r"\textit{R/AU}")
ylabel("ADU")
xlabel("Position angle")
xlim([0,360])
#pe2 = np.array(pe)
#pe2[pe>=p] = p[pe>=p]*.999999
plt.errorbar(px,p,yerr=pe,fmt='o')
#title(...)
ylim(1E1,1E4)
yscale("log",nonposy='clip')
#xlim(...)
#plot.show()
#legend([plot1,plot2],["model","observation"],numpoints=1)
f=open('std', 'w')
for tmp in pe:
  f.write("%s\n" % tmp)
f.close()
f2=open('value', 'w')
for tmp in p:
  print>>f2, tmp
f2.close()

savefig(filename)
clf()