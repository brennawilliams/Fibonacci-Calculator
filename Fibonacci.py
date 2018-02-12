# Chapter 3 - Ex. 12: Fibonacci Calculator

a = 0
b = 1
p = 1
while b <= 75025:
	print(str(p) + ": " + str(b))
	p = p + 1
	a, b = b, a + b 
