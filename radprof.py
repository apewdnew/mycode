#! /usr/bin/env python

#Copying and pasting from StackOverflow
#http://stackoverflow.com/questions/34965275/radial-profile-from-a-fits-image



from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

minorLocator = AutoMinorLocator()


def radial_profile(data, center):
    x, y = np.indices((data.shape))
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    r = r.astype(np.int)

    tbin = np.bincount(r.ravel(), data.ravel())
    nr = np.bincount(r.ravel())
    radialprofile = tbin / nr
    return radialprofile 


fitsFile = fits.open('testfig.fits')
img = fitsFile[0].data[0]
img[np.isnan(img)] = 0

#center = np.unravel_index(img.argmax(), img.shape)
center = (-fitsFile[0].header['LBOUND2']+1, -fitsFile[0].header['LBOUND1']+1)
rad_profile = radial_profile(img, center)

fig, ax = plt.subplots()
plt.plot(rad_profile[0:22], 'x-')

ax.xaxis.set_minor_locator(minorLocator)

plt.tick_params(which='both', width=2)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=4, color='r')
plt.grid()
ax.set_ylabel(fitsFile[0].header['Label'] + " (" + fitsFile[0].header['BUNIT'] + ")")
ax.set_xlabel("Pixels")
plt.grid(which="minor")
plt.show()
