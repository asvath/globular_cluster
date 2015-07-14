import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from itertools import cycle

def percentileplot(nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	c=cm.rainbow(np.linspace(0,1,3))
	acyc=cycle(c)
	

	onezero,onetwo,onethree,onefour,onefive = np.loadtxt("%s_one_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4))
	twozero,twotwo,twothree,twofour,twofive = np.loadtxt("%s_two_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4))
	threezero,threetwo,threethree,threefour,threefive = np.loadtxt("%s_three_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4))
	
	y=[10,20,30,40,50,60,70,80,90]
	plt.plot(onezero,y,color=acyc.next(),label="first one percent")
	plt.plot(twozero,y,color=acyc.next(),label="second one percent")
	plt.plot(threezero,y,color=acyc.next(),label="same mass as first one percent")

	plt.title('%s_0000 cmf'%nameofplot)
	plt.ylabel('percentile')
	plt.xlabel('')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_time0000cmf.pdf" %nameofplot)
	plt.close()


	plt.plot(onetwo,y,color=acyc.next(),label="first one percent")
	plt.plot(twotwo,y,color=acyc.next(),label="second one percent")
	plt.plot(threetwo,y,color=acyc.next(),label="same mass as first one percent")

	plt.title('%s_2000 cmf'%nameofplot)
	plt.ylabel('percentile')
	plt.xlabel('')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_time2000cmf.pdf" %nameofplot)
	plt.close()


	plt.plot(onethree,y,color=acyc.next(),label="first one percent")
	plt.plot(twothree,y,color=acyc.next(),label="second one percent")
	plt.plot(threethree,y,color=acyc.next(),label="same mass as first one percent")

	plt.title('%s_3000 cmf'%nameofplot)
	plt.ylabel('percentile')
	plt.xlabel('')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_time3000cmf.pdf" %nameofplot)
	plt.close()




	plt.plot(onefour,y,color=acyc.next(),label="first one percent")
	plt.plot(twofour,y,color=acyc.next(),label="second one percent")
	plt.plot(threefour,y,color=acyc.next(),label="same mass as first one percent")

	plt.title('%s_4000 cmf'%nameofplot)
	plt.ylabel('percentile')
	plt.xlabel('')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_time4000cmf.pdf" %nameofplot)
	plt.close()

	plt.plot(onefive,y,color=acyc.next(),label="first one percent")
	plt.plot(twofive,y,color=acyc.next(),label="second one percent")
	plt.plot(threefive,y,color=acyc.next(),label="same mass as first one percent")

	plt.title('%s_=5000 cmf'%nameofplot)
	plt.ylabel('percentile')
	plt.xlabel('')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_time5000cmf.pdf" %nameofplot)
	plt.close()





if __name__ == "__main__":
	import sys
	percentileplot(str(sys.argv[1]))
