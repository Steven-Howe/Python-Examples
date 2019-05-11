"""
Program Name: CIS110 Program 9
Program Description: Program simulates a Powerball drawing.
Author: Steven Howe
Date Created: 4/3/2019
Notes of Interest: Uses the Python time library and random library

"""
import time
from random import randrange

# Powerball number between 1 - 26
def pickPowerball():
	powerball = randrange(1, 27)
	return powerball 

# Generates sorted list of five numbers between 0 - 68
def pickFive():
	numbers = []

	while len(numbers) != 5:
		numbers.append(randrange(0, 69))
		# Eliminates duplicates
		numbers = list(set(numbers))

	numbers.sort()
	return numbers

# Lists user defined amount of drawings
def main():
	print("\nThis program will simulate a Powerball drawing.")

	n = int(input("Enter the number of drawings: "))
	count = 0

	for i in range(n):
		count += 1
		print("For drawing:", count,"The numbers are:", pickFive(), "and the Powerball is:", pickPowerball())



#prints authors name, class, and date
print("Steven Howe")
print("CIS110 Program 9")
#this function will print the current date and time using asctime()
print(time.asctime(time.localtime(time.time())))

main()