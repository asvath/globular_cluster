import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def hmrplot(filename,nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	#c=cm.rainbow(np.linspace(0,1,4*len(filename)))

	
	time, one,two,three,rmedian = np.loadtxt(filename,unpack=True,usecols=(0,1,2,3,4))
             	
	l,p=filename.split(".txt")
	plt.plot(time,rmedian,color='red',label="rmedian")
	plt.plot(time,one,color='blue',label="first one percent")
	plt.plot(time,two,color='salmon',label="second one percent")
	plt.plot(time,three,color='orange',label="same mass as first one percent")

	plt.title('%s_parts_radius vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_parts_vs_time.pdf" %nameofplot)
	plt.close()


if __name__ == "__main__":
	import sys
	hmrplot(str(sys.argv[1]),str(sys.argv[2]))
