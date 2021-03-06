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

    x=np.concatenate((x[:len(x)/100:2],x[1:len(x)/100:2],x[len(x)/100:]))
    y=np.concatenate((y[:len(y)/100:2],y[1:len(y)/100:2],y[len(y)/100:]))
    z=np.concatenate((z[:len(z)/100:2],z[1:len(z)/100:2],z[len(z)/100:]))
    vx=np.concatenate((vx[:len(vx)/100:2],vx[1:len(vx)/100:2],vx[len(vx)/100:]))
    vy=np.concatenate((vy[:len(vy)/100:2],vy[1:len(vy)/100:2],vy[len(vy)/100:]))
    vz=np.concatenate((vz[:len(vz)/100:2],vz[1:len(vz)/100:2],vz[len(vz)/100:]))
        

	np.transpose(np.concatenate(([x,y,z,m],[vx,vy,vz,m]),axis=1)).astype('float32').tofile("asha.NBODY_%03d" %filenum)

   	
   	
	return


if __name__ == "__main__":
	import sys
	readconvert(str(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))

