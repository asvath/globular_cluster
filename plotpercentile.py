import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from itertools import cycle

def percentileplot(filename,nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	c=cm.rainbow(np.linspace(0,1,6))
	acyc=cycle(c)
	
	time, oneone,onetwo,onethree,onefour,onefive,onesix,oneseven,oneeight,onenine,twoone,twotwo,twothree,twofour,twofive,twosix,twoseven,twoeight,twonine,threeone,threetwo,threethree,threefour,threefive,threesix,threeseven,threeeight,threenine  = np.loadtxt(filename,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27))
	time=time*0.016     	
	l,p=filename.split(".txt")
	name=["one","two","three","four","five","six","seven","eight","nine","ten"]
	for i in name:
		with open("%s_percentile.txt" %nameoflist,"w") as f:
			para="one%s" %name
			pararray="one%stime" %name
			coeff=np.polyfit(time,para,3)
			polynomial=np.poly1d(coeff)
			xs=np.arange(min(time),max(time),0.1)
			ys=polynomial(xs)
			one0000=polynomial(0)
			one2000=polynomial(2000)
			one3000=polynomial(3000)
			one4000=polynomial(4000)
			one5000=polynomial(5000)
		
	

	

	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twoone,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threeone,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)

	

	plt.title('%s_10th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_10th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,onetwo,color=acyc.next(),label="first 1%",s=0.1)
	plt.scatter(time,twotwo,color=acyc.next(),label="second 1%",s=0.11)
	plt.scatter(time,threetwo,color=acyc.next(),label="same mass as first 1%",s=0.1)

	coeff=np.polyfit(time,onetwo,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twotwo,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threetwo,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)



	plt.title('%s_20th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_20th_percentile_vs_time.pdf" %nameofplot)
	plt.close()
			  
	plt.scatter(time,onethree,color=acyc.next(),label="first 1%",s=0.1)
	plt.scatter(time,twothree,color=acyc.next(),label="second 1%",s=0.1)
	plt.scatter(time,threethree,color=acyc.next(),label="same mass as first 1%",s=1)


	coeff=np.polyfit(time,onethree,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twothree,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threethree,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)




	plt.title('%s_30th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_30th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,onefour,color=acyc.next(),label="first 1%",s=0.1)
	plt.scatter(time,twofour,color=acyc.next(),label="second 1%",s=0.1)
	plt.scatter(time,threefour,color=acyc.next(),label="same mass as first 1%",s=0.1)

	coeff=np.polyfit(time,onefour,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twofour,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threefour,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)



	plt.title('%s_40th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_40th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,onefive,color=acyc.next(),label="first 1%",s=1)
	plt.scatter(time,twofive,color=acyc.next(),label="second 1%",s=1)
	plt.scatter(time,threefive,color=acyc.next(),label="same mass as first 1%",s=1)

	coeff=np.polyfit(time,onefive,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twofive,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threefive,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)



	plt.title('%s_50th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_50th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,onesix,color=acyc.next(),label="first 1%",s=0.1)
	plt.scatter(time,twosix,color=acyc.next(),label="second 1%",s=0.1)
	plt.scatter(time,threesix,color=acyc.next(),label="same mass as first 1%",s=0.1)


	coeff=np.polyfit(time,onesix,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twosix,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threesix,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)


	plt.title('%s_60th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_60th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,oneseven,color=acyc.next(),label="first 1%",s=0.1)
	plt.scatter(time,twoseven,color=acyc.next(),label="second 1%",s=0.1)
	plt.scatter(time,threeseven,color=acyc.next(),label="same mass as first 1%",s=0.1)

	coeff=np.polyfit(time,oneseven,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twoseven,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threeseven,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)


	plt.title('%s_70th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_70th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,oneeight,color=acyc.next(),label="first 1%",s=1)
	plt.scatter(time,twoeight,color=acyc.next(),label="second 1%",s=1)
	plt.scatter(time,threeeight,color=acyc.next(),label="same mass as first 1%",s=1)

	coeff=np.polyfit(time,oneeight,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twoeight,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threeeight,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)


	plt.title('%s_80th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_80th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

	plt.scatter(time,onenine,color=acyc.next(),label="first 1%",s=0.1)
	plt.scatter(time,twonine,color=acyc.next(),label="second 1%",s=0.1)
	plt.scatter(time,threenine,color=acyc.next(),label="same mass as first 1%",s=0.1)

	coeff=np.polyfit(time,onenine,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit one",s=0.1)


	coeff=np.polyfit(time,twonine,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit two",s=0.1)

	coeff=np.polyfit(time,threenine,3)
	polynomial=np.poly1d(coeff)
	xs=np.arange(min(time),max(time),0.1)
	ys=polynomial(xs)
	plt.scatter(xs,ys,color=acyc.next(),label="fit three",s=0.1)


	plt.title('%s_90th_percentile vs time'%nameofplot)
	plt.ylabel('rmedian')
	plt.xlabel('time')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_90th_percentile_vs_time.pdf" %nameofplot)
	plt.close()

if __name__ == "__main__":
	import sys
	percentileplot(str(sys.argv[1]),str(sys.argv[2]))

