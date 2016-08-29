import sys

def collatz(number, numbers):
	if number == 1:
		numbers.append(1)
		print "Done"
		print numbers
	elif number % 2 == 0:
		numbers.append(number)
		collatz(number / 2, numbers)
	else:
		numbers.append(number)
		collatz(3 * number + 1, numbers)

def main():
	numbers = []
	collatz(int(sys.argv[1]), numbers)

main()
