#hw 5
#collaborator: Vi-Linh Nguyen
import math
from math import factorial
#Problem 1
#Answer:
def rps(p1Choice,p2Choice):
	p1Choice=p1Choice.upper()
	p2Choice=p2Choice.upper()
	if(p1Choice==p2Choice):
		return 0
	elif(p1Choice=='R' and p2Choice=='P'):
		return 2
	elif(p1Choice=='R' and p2Choice=='S'):
		return 1
	elif(p1Choice=='P' and p2Choice=='R'):
		return 1
	elif(p1Choice=='P' and p2Choice=='S'):
		return 2
	elif(p1Choice=='S' and p2Choice=='P'):
		return 1
	elif(p1Choice=='S' and p2Choice=='R'):
		return 2
#___________________________________

#Problem 2
#Answer:
def isPrime(n):
	if n < 1:
		return False
	else:
		for i in range (2, n):
			if(n%i==0):
				return False
		else:
			return True
#___________________________________

#Problem 3
#Answer:
#reference: https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/		
#Use this as a base
def playerHasLastInitial(filename, char):
	with open(filename,'r') as fiLe:
		header=next(fiLe)
		filRL=fiLe.readline()
		while fiLe.readline():
			filRL=fiLe.readline()
			if char in filRL:
				filRL=filRL.split()
				if char==filRL[1][0]:
					return True
				else:
					return False
		fiLe.close()
#___________________________________

#Problem 4
#Answer:
def maxFactorial(n):
    v=[]
    for i in range(2,n+1):
        if factorial(i) <= n:
            v.append(i)
        else:
            break
    return v[-1]
#___________________________________



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('hw5_test.py', verbose=True))
