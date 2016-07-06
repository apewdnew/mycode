#!/usr/bin/env python

import numpy as np
from astropy.io import fits
import sys

image=sys.argv[1]

def convert(im):
    image=fits.open(im)
    data=image[0].data
    jy_con=3.54e-7
    arcsec_con=0.0095*0.0095
    exptime=image[0].header['EXP1TIME']
    coadd=image[0].header['COADD']
    con=jy_con/(arcsec_con*exptime*coadd)
    image_jysec=data*con
    
    #create header
    prihdr=image[0].header
    prihdr['BUNIT']="Jy/arcsec2"
    
    result=fits.PrimaryHDU(image_jysec,header=prihdr)
    result.writeto('a_jysec.fits')
    return 0

convert(image)

