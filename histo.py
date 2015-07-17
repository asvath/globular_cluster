import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.interpolate
from itertools import cycle

def filter_value(a,b,value):
	someList=zip(a,b)
	for x, y in someList:
	        if x == value :
	            return x,y



def histoplot(nameofplot): 

	"""
	Example:

	$ipython hmrplot list nameofplot

	"""
	c=cm.rainbow(np.linspace(0,1,3))
	acyc=cycle(c)
	ray=[]

	onezero,oneone,oneonefive,onetwo,onetwofive,onethree,onethreefive,onefour,onefourfive,onefive,onefivefive = np.loadtxt("%s_one_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))
	twozero,twoone,twoonefive,twotwo,twotwofive,twothree,twothreefive,twofour,twofourfive,twofive,twofivefive = np.loadtxt("%s_two_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))
	threezero,threeone,threeonefive,threetwo,threetwofive,threethree,threethreefive,threefour,threefourfive,threefive,threefivefive = np.loadtxt("%s_three_at_time_percentile.txt" %nameofplot,unpack=True,usecols=(0,1,2,3,4,5,6,7,8,9,10))

	y=[10,20,30,40,50,60,70,80,90]

	lmax=np.log10(onezero[-1])
	lmin=np.log10(onezero[0])
	xsone=10**np.arange(lmin-0.2,lmax,0.03)

	splinefit=scipy.interpolate.InterpolatedUnivariateSpline(np.insert(onezero,0,0.0),np.insert(np.sqrt(y),0,0.0))
	w=splinefit(xsone)
	ysone=w**2
	splinedfit=splinefit.derivative()

	ysoneder=splinedfit(xsone)*2*w
	ysoneder=ysoneder/(4*np.pi*xsone**2)

	dy=splinedfit(onezero)*2*np.sqrt(y)
	dy=dy/(4*np.pi*onezero**2)
	

	plt.plot(xsone,ysone,label="")
	plt.scatter(onezero,y)

	plt.title('%s_first_1_percent'%nameofplot)
	plt.ylabel('number of particles')
	plt.xlabel('r')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_test.pdf" %nameofplot)
	plt.close()


	plt.plot(np.log10(xsone),np.log10(ysoneder))
	plt.scatter(np.log10(onezero[:-1]),np.log10(dy[:-1]))

	plt.title('%s_first_1_percent'%nameofplot)
	plt.ylabel('log (Density)')
	plt.xlabel('log (r)')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_der.pdf" %nameofplot)
	plt.close()
	
	
	
	#print "HELLO"
	
	#play here for histogram

	#p,q=filter_value(xsone,ysone,100)
	xsone=xsone.astype(int)
	ysone=ysone.astype(int)
	a=zip(xsone,ysone)
	numberofparticles=[]


	
	

	z= [ (x,y) for x, y in a if x  == 100 ]
	
	p100,q100=zip(*z)
	q100=np.sum(q100)/len(q100)
	
	number_of_particles100=(q100/100.0)*200000
	
	


	z= [ (x,y) for x, y in a if x  == 150 ]
	
	p150,q150=zip(*z)
	q150=np.sum(q150)/len(q150)
	
	print q150
	print q100
	number_of_particles150=((q150-q100)/100.0)*200000
	
	



	z= [ (x,y) for x, y in a if x  == 200 ]
	
	p200,q200=zip(*z)
	q200=np.sum(q200)/len(q200)
	
	number_of_particles200=((q200-q150)/100.0*200000)



	z= [ (x,y) for x, y in a if x  == 250 ]
	
	p250,q250=zip(*z)
	q250=np.sum(q250)/len(q250)
	
	number_of_particles250=((q250-q200)/100.0*200000)


 
	z= [ (x,y) for x, y in a if x  == 300 ]
	
	p300,q300=zip(*z)
	q300=np.sum(q300)/len(q300)
	
	
	number_of_particles300=((q300-q250)/100.0*200000)
	print number_of_particles300


 
	z= [ (x,y) for x, y in a if x  == 350 ]
	
	p350,q350=zip(*z)
	q350=np.sum(q350)/len(q350)

	number_of_particles350=((q350-q300)/100.0*200000)
	print number_of_particles350


	z= [ (x,y) for x, y in a if x  == 400 ]
	print z
	p400,q400=zip(*z)
	q400=np.sum(q400)/len(q400)
	
	number_of_particles400=((q400-q350)/100.0*200000)


	z= [ (x,y) for x, y in a if x  == 450 ]
	print z
	p450,q450=zip(*z)
	q450=np.sum(q450)/len(q450)
	
	number_of_particles450=((q450-q400)/100.0*200000)



	#z= [ (x,y) for x, y in a if x  == 500 ]
	#print z
	#p500,q500=zip(*z)
	#q500=np.sum(q500)/len(q500)
	
	#number_of_particles500=(q500/100*20000) - number_of_particles400
	
	numberofparticles=[number_of_particles100,number_of_particles150,number_of_particles200,number_of_particles250,number_of_particles300,number_of_particles350,number_of_particles400,number_of_particles450]
	rmedian=[100,150,200,250,300,350,400,450]
	plt.bar(rmedian,numberofparticles,width=50)

	#plt.scatter(rmedian,numberofparticles,label="first one percent")


	plt.title('%s_first_1_percent'%nameofplot)
	plt.ylabel('number of particles')
	plt.xlabel('rmedian')
	plt.legend(loc='upper right', shadow=True,prop={'size':6})
	plt.savefig("graph_%s_histo0000.pdf" %nameofplot)
	plt.close()

	



	



	
	
	#hello=np.array([9.9,6.7,2.4])
	#hello=hello.astype(int)
	#print hello




if __name__ == "__main__":
	import sys
	histoplot(str(sys.argv[1]))

