import numpy as np
import matplotlib.pyplot as plt
import nbody
import os

def readconvert(filename,startnum,stepsize,filenum):
	
	snapsy=nbody.readviewdat(filename)
	x=snapsy['x']
	y=snapsy['y']
	z=snapsy['z']
	m=snapsy['m']
	vx=snapsy['vx'] 
	vy=snapsy['vy']
	vz=snapsy['vz']
	
   
   	#mcluster=np.sum(m)
	msy=np.concatenate((m[:1000]*0.9/0.53,m[1000:]))
	mnew=np.sum(msy)
	
	#to plot every nth particle
	x=x[startnum::stepsize]
	y=y[startnum::stepsize]
	z=z[startnum::stepsize]
	m=m[startnum::stepsize]
	vx=vx[startnum::stepsize]
	vy=vy[startnum::stepsize]
	vz=vz[startnum::stepsize]
	print len(x)
#	m=np.concatenate((m[:len(m)/100]*0.53/0.9,m[len(m)/100:]))
        m=np.concatenate((m[:len(m)/100:2]*0.53/0.9,m[1:len(m)/100:2],m[len(m)/100:]))
	m=(mnew/np.sum(m))*m

        

	np.transpose(np.concatenate(([x,y,z,m],[vx,vy,vz,m]),axis=1)).astype('float32').tofile("asha.NBODY_%03d" %filenum)

   	
   	
	return


if __name__ == "__main__":
	import sys
	readconvert(str(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))

