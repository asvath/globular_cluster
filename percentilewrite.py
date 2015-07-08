import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import savitzky_golay

def hmrplots(numberoffiles,nameoflist):

        import nbody

        """                                                                                                                                                                      
        Example:                                                                                                                                                                 
                                                                                                                                                                                 
        $ipython halfmassradius.py 119996 g_1_10                                                                                                                     
                                                                                                                                                                                 
        """
        
	with open("%s_percentile.txt" %nameoflist,"w") as f:
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
			
			l=len(r2)
		
			one=np.sqrt((r2[:l/200]))
			oneperc=np.percentile(one,[10,20,30,40,50,60,70,80,90])
			two=np.sqrt((r2[l/200:l/100]))
			twoperc=np.percentile(two,[10,20,30,40,50,60,70,80,90])
			three=np.sqrt((r2[l*4574/100000:l*5574/100000]))
			threeperc=np.percentile(three,[10,20,30,40,50,60,70,80,90])
			
			massy=np.sum(m)
			f.write('%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f \n' %(i,oneperc[0],oneperc[1],oneperc[2],oneperc[3],oneperc[4],oneperc[5],oneperc[6],oneperc[7],oneperc[8],twoperc[0],twoperc[1],twoperc[2],twoperc[3],twoperc[4],twoperc[5],twoperc[6],twoperc[7],twoperc[8],threeperc[0],threeperc[1],threeperc[2],threeperc[3],threeperc[4],threeperc[5],threeperc[6],threeperc[7],threeperc[8]))





if __name__ == "__main__":
        import sys
        hmrplots(int(sys.argv[1]),sys.argv[2])
