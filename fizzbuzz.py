# In the programming language of your choice, write a program 
# generating the first n Fibonacci numbers F(n), printing ...
# - ... "Buzz" when F(n) is divisible by 3.
# - ... "Fizz" when F(n) is divisible by 5.
# - ... "BuzzFizz" when F(n) is prime.
# - ... the value F(n) otherwise.
# 
# Bonus points for efficient implementation, testing, documentation, 
# and/or upload your code to GitHub.

import math

# PrintFibbonaci will generate the first n Fibonacci numbers F(n), passing them 
# to DecideHowToPrint for printing.
#  
# @param generate_this_many The number of Fibbonaci numbers to generate. A value of zero
# or less will generate nothing. 
# 1 will generate DecideHowToPrint[1], 
# 2 will generate DecideHowToPrint[1,1], 
# 3 will generate DecideHowToPrint[1,1,2]. 
# 
def PrintFibbonaci(generate_this_many):
	if generate_this_many < 1:
		return
	elif generate_this_many == 1: 
		DecideHowToPrint(1)
		return
	elif generate_this_many >= 2: 
		DecideHowToPrint(1)
		DecideHowToPrint(1)
		
	fibb1 = 1
	fibb2 = 1
	# fibb2 is the (index_of_fibb_num)th Fibbonaci number  
	index_of_fibb_num = 2;
	
	while index_of_fibb_num < generate_this_many:
		fibb3 = fibb2 + fibb1
		DecideHowToPrint(fibb3) 
		fibb1 = fibb2
		fibb2 = fibb3
		index_of_fibb_num = index_of_fibb_num + 1

# DecideHowToPrint will print 
# - ... "Buzz" when n is divisible by 3.
# - ... "Fizz" when n is divisible by 5.
# - ... "BuzzFizz" when n is prime.
# - ... the value n otherwise.
def DecideHowToPrint(n):
	if n == 0:
		printThis = 0
	elif n % 3 == 0:
		printThis = "Buzz"
	elif n % 5 == 0:
		printThis = "Fizz"
	elif CheckIfPrime(n):
		printThis = "BuzzFizz" 
	else:
		printThis = n
		
	print printThis
	return printThis
	
# CheckIfPrime will return 1 if prime and 0 if not prime. 	
#
# @param n number to check 
def CheckIfPrime(n):
	if n <= 1:
		return 0
	
	for divisor in range(2, int(math.sqrt(n)) + 1):
		if n % divisor == 0:
			return 0

	return 1
	
PrintFibbonaci(50)