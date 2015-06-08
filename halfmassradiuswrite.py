import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def hmrplots(numberoffiles,nameoflist):

        import nbody

        """                                                                                                                                                                      
        Example:                                                                                                                                                                 
                                                                                                                                                                                 
        $ipython halfmassradius.py 119996 g_1_10                                                                                                                     
                                                                                                                                                                                 
        """
        
	with open("%s_halfmass_time.txt" %nameoflist,"w") as f:
		for i in range(0,numberoffiles,5):
			snapsy=nbody.readviewdat("Sp_%06d.bin" %i)
			x=snapsy['x']
			y=snapsy['y']
			z=snapsy['z']
			m=snapsy['m']
			vx=snapsy['vx'] 
			vy=snapsy['vy']
			vz=snapsy['vz']
			
			xcm=np.average(x,weights=m)
			ycm=np.average(y,weights=m)
			zcm=np.average(z,weights=m)
			r2=(x-xcm)**2+(y-ycm)**2+(z-zcm)**2
			#r2=x**2+y**2+z**2
			l=len(r2)
			'''
			print('%d %g %g %g %g' % (i,np.median(m[:l/100]),
						  np.median(m[l/100:2*l/100]),
						  np.median(m[l*4574/100000:l*5574/100000]),
						  np.median(m)))
						  '''

			#one=np.sqrt(np.median(r2[:l/100]))
			#two=np.sqrt(np.median(r2[l/100:2*l/100]))
			one=np.sqrt(np.median(r2[:l/200]))
			two=np.sqrt(np.median(r2[l/200:l/100]))
			three=np.sqrt(np.median(r2[l*4574/100000:l*5574/100000]))
			rmedian=np.sqrt(np.median(r2))
			massy=np.sum(m)
			f.write('%f %f %f %f %f %f\n' %(i,one,two,three,rmedian,massy))


if __name__ == "__main__":
        import sys
        hmrplots(int(sys.argv[1]),sys.argv[2])

