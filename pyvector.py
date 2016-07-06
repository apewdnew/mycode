import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

#read data
qdata=fits.open("../sub_q.fits")[0].data
udata=fits.open("../sub_u.fits")[0].data

def databin(data,binsize):
	x,y=data.shape
	data_view=data.reshape(x//binsize,binsize,y//binsize,binsize)
	data_bin=data_view.mean(axis=3).mean(axis=1)
	return data_bin

#bin data
#qdata_view=qdata.reshape(64,8,64,8)
#qdata_bin=qdata_view.mean(axis=3).mean(axis=1)
#udata_view=udata.reshape(64,8,64,8)
#udata_bin=udata_view.mean(axis=3).mean(axis=1)
binsize=8
qdata_bin=databin(qdata,binsize)
udata_bin=databin(udata,binsize)


#polarization angle calculation
theta_p=0.5*np.arctan(qdata_bin/udata_bin)
theta_px=np.cos(theta_p)
theta_py=np.sin(theta_p)
x,y=np.indices(theta_px)
theta_py
theta_py.shape
np.indices(theta_px)
np.indices(theta_py)
np.indices(theta_py.shape)
x,y=np.indices(theta_py.shape)

#plot
vmap=plt.quiver(x,y,theta_px,theta_py)
#plt.show()
plt.savefig("test.png")

