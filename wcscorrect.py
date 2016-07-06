from astropy.io import fits

data, header = fits.getdata("PIimage.fits", header=True)

header['CRPIX1']=512
header['CRPIX2']=1024
header['CRVAL1']=68.123762
header['CRVAL2']=17.528819

header['CD1_1']=-2.64E-6
header['CD1_2']=0
header['CD2_1']=0
header['CD2_2']=2.64E-6


fits.writeto('output_file.fits', data, header, clobber=True)
