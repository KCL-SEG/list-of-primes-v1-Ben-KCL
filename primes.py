"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
	list = []
	num = 2
	while len(list) < number_of_primes:
		for divisor in range(2, num + 1):
			if divisor == num:
				list.append(num)
			elif num % divisor == 0:
				break
		num += 1
	return list
