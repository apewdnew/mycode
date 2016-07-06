#! /usr/bin/env python

#This is used to make the radial stokes image.
#Credit: Yi Yang 2016/03/29
#input (python) stokesrad.py q u xcenter ycenter qphi uphi

import numpy as np
import pyfits
import sys

q=sys.argv[1]
u=sys.argv[2]
xcenter=float(sys.argv[3])
ycenter=float(sys.argv[4])
qphi=sys.argv[5]
uphi=sys.argv[6]

#n=np.zeros((512,512))

def stokesrad(a,b,x,y,qp,up):
    image1 = pyfits.open(a)
    image2 = pyfits.open(b)
    data1=image1[0].data
    data2=image2[0].data
    size=data1.shape
    phiq=np.zeros(size)
    phiu=np.zeros(size)
    for i in range(size[0]):
        for j in range(size[1]):
            phi=np.arctan((float(j)-x)/(float(i)-y))-0.04276066666667
            phiq[i][j]=data1[i][j]*np.cos(2*phi)+data2[i][j]*np.sin(2*phi)
            phiu[i][j]=-data1[i][j]*np.sin(2*phi)+data2[i][j]*np.cos(2*phi)
    output1=pyfits.PrimaryHDU(phiq)
    output1.writeto(qp)
    output2=pyfits.PrimaryHDU(phiu)
    output2.writeto(up)
    return

stokesrad(q,u,xcenter,ycenter,qphi,uphi)
