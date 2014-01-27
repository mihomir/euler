def taken(g,n):
	for i in range(n):
		yield(g.next())

def taketo(g,n):
	x=g.next()
	while x<n:
		yield(x)
		x=g.next()



def fib():
	a=1
	b=2
	yield(a)
	yield(b)
	while 1:
		a=a+b
		yield(a)
		b=a+b
		yield(b)

def prime_gen():
	primes=[]
	n=2
	while 1:
		if all([n % prime != 0 for prime in primes]):
			primes.append(n)
			yield(n)
		n=n+1
		
from math import sqrt
def prime_optimus():
	primes=[2]
	primes_sqrt=[]
	i=0
	n=2
	while 1:
		if primes[i]<=sqrt(n):
			primes_sqrt.append(primes[i])
			i+=1
		if all([n % prime !=0 for prime in primes_sqrt]):
			primes.append(n)
			yield(n)
		n+=1

def check_prime(n, primes=None):
	if n<=1:
		return 0
	if not primes:
		gen = prime_optimus()
		primes = taketo(gen,sqrt(n)+1)
	return all([n % prime !=0 for prime in primes])

def mag_formula(a,b):
	i=0
	while 1:
		if not check_prime(i**2 + a*i + b):
			return i
		i+=1

def dig_to_pow(n,k):
	return sum([int(dig)**k for dig in str(n)])

def splice(n):
     i=0
     k=0
     x=''
     while i<n:
             x=''.join([x,str(k)])
             i+=len(str(k))
             k+=1
     return x

def mag(n):
	if n==0:
		return 0
	else:
		return 1

def num_to_word(n):
	if n==0:
		return ""
	if n==1:
		return "one"
	if n==2:
		return "two"
	if n==3:
		return "three"
	if n==4:
		return "four"
	if n==5:
		return "five"
	if n==6:
		return "six"
	if n==7:
		return "seven"
	if n==8:
		return "eight"
	if n==9:
		return "nine"
	if n==10:
		return "ten"
	if n==11:
		return "eleven"
	if n==12:
		return "twelve"
	if n==13:
		return "thirteen"
	if n==14:
		return "fourteen"
	if n==15:
		return "fifteen"
	if n in range(16,20):
		return num_to_word(n%10)+"teen"
	if n==20:
		return "twenty"
	if n==30:
		return "thirty"
	if n==40:
		return "forty"
	if n==50:
		return "fifty"
	if n in range (60,100,10):
		return num_to_word(n/10)+"ty"
	if n==100:
		return "hundred"
	if n==1000:
		return "onethousand"
	else:
		if n in range(20,100):
			return num_to_word(n-(n%10)) + num_to_word(n%10)
		else:
			return num_to_word(n/100)+num_to_word(100)+"and"*mag(n%100)+num_to_word(n%100)


