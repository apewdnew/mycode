#! /usr/bin/env python

#This is used to make the polarized intensity image.
#Credit: Yi Yang 2016/03/29
#input (python) mkpi.py q u pi

import numpy as np
from astropy.io import fits
import sys

q=sys.argv[1]
u=sys.argv[2]
pi=sys.argv[3]

#n=np.zeros((512,512))

def mkpi(a,b,pi):
    image1 = fits.open(a)
    image2 = fits.open(b)
    data1=image1[0].data
    data2=image2[0].data
    result=np.sqrt(data1*data1+data2*data2)
    output = fits.PrimaryHDU(result)
    output.writeto(pi)
    return 0

mkpi(q,u,pi)
