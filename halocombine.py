#! /usr/bin/env python

#This is used to combine the polarized halo of a binary system

from astropy.io import fits 

image1 = fits.open('input1.fits')
image2 = fits.open('input2.fits')
output = fits.PrimaryHDU(size)

for i in range(size):
	for j in range(size):
		output[i,j]=max(image1[i,j],image2[i,j])

output.writeto("combine.fits")