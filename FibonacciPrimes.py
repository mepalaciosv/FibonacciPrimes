# FibonacciPrimes.py
# Code for calculating the first Fibonacci primes in an hour of computation
# Author : Margarita Palacios

import time


print('Execution of the Fibonacci primes calculation program')
print('Calculated primes in an hour of runtime by index:')

x = 1
# t_end = time.time() + 60 * minutes to run program
t_end = time.time() + 60 * 60

def fib(f):
	if f < 2:
		return f
	else:
	    return fib(f - 1) + fib(f - 2)

def prime(num):
	flag = False

	for i in range(2 , num):
		if (num % i) == 0:
			flag = False
			break
		else:
			flag = True

	if(num == 2):
		flag = True

	return flag

print ('n' , 'Fn')
while time.time() < t_end:
 	if (prime(fib(x)) == True):
 		print (x , fib(x))
	x = x + 1
	

# End of program