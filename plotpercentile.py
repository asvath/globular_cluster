import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from itertools import cycle

def percentileplot(filename,nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	c=cm.rainbow(np.linspace(0,1,30))
	acyc=cycle(c)
	
	time, oneone,onetwo,onethree,onefour,onefive,onesix,oneseven,oneeight,onenine,twoone,twotwo,twothree,twofour,twofive,twosix,twoseven,twoeight,twonine,threeone,threetwo,threethree,threefour,threefive,threesix,threeseven,threeeight,threenine  = np.loadtxt(filename,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27))
	time=time*0.016     	
	l,p=filename.split(".txt")
	
	plt.plot(time,oneone,color=acyc.next(),label="10th percentile")
	plt.plot(time,twoone,color=acyc.next(),label="10th percentile")
	plt.plot(time,threeone,color=acyc.next(),label="10th percentile")

	plt.title('%s_10th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_10th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,onetwo,color=acyc.next(),label="20th percentile")
	plt.plot(time,twotwo,color=acyc.next(),label="20th percentile")
	plt.plot(time,threetwo,color=acyc.next(),label="20th percentile")

	plt.title('%s_20th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_20th_percentile_vs_time.pdf" %nameofplot)
	plt.close()
			  
	plt.plot(time,onethree,color=acyc.next(),label="30th percentile")
	plt.plot(time,twothree,color=acyc.next(),label="30th percentile")
	plt.plot(time,threethree,color=acyc.next(),label="30th percentile")

	plt.title('%s_30th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_30th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,onefour,color=acyc.next(),label="40th percentile")
	plt.plot(time,twofour,color=acyc.next(),label="40th percentile")
	plt.plot(time,threefour,color=acyc.next(),label="40th percentile")

	plt.title('%s_40th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_40th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,onefive,color=acyc.next(),label="50th percentile")
	plt.plot(time,twofive,color=acyc.next(),label="50th percentile")
	plt.plot(time,threefive,color=acyc.next(),label="50th percentile")

	plt.title('%s_50th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_50th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,onesix,color=acyc.next(),label="60th percentile")
	plt.plot(time,twosix,color=acyc.next(),label="60th percentile")
	plt.plot(time,threesix,color=acyc.next(),label="60th percentile")

	plt.title('%s_60th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_60th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,oneseven,color=acyc.next(),label="70th percentile")
	plt.plot(time,twoseven,color=acyc.next(),label="70th percentile")
	plt.plot(time,threeseven,color=acyc.next(),label="70th percentile")

	plt.title('%s_70th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_70th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,oneeight,color=acyc.next(),label="80th percentile")
	plt.plot(time,twoeight,color=acyc.next(),label="80th percentile")
	plt.plot(time,threeeight,color=acyc.next(),label="80th percentile")

	plt.title('%s_80th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_80th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.plot(time,onenine,color=acyc.next(),label="90th percentile")
	plt.plot(time,twonine,color=acyc.next(),label="90th percentile")
	plt.plot(time,threenine,color=acyc.next(),label="90th percentile")

	plt.title('%s_90th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_90th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

if __name__ == "__main__":
	import sys
	percentileplot(str(sys.argv[1]),str(sys.argv[2]))

