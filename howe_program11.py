"""
Program Name: CIS110 Program 11
Program Description: Simulates a last-in first-out (LIFO) stack.
Author: Steven Howe
Date Created: 4/19/2019
Notes of Interest: Uses the Python time library

"""
import time

class Stack:

	def __init__(self):
		"""Initializes a stack"""
		self.stack = []




	def isEmpty(self):
		"""Tests if a stack is empty"""
		if self.stack == []:
			print("The stack is empty.")

		else:
			print("The stack is not empty.")



	def push(self, item):
		"""Pushes an item to the stack"""
		self.stack.append(item)



	def pop(self):
		"""Pop's last item from the stack"""
		item = self.stack.pop()
		return item



	def peek(self):
		"""Prints the contents of the stack"""
		print("The stack contains:",self.stack)



	def size(self):
		"""Prints the length of the stack"""
		print("The size of the stack is:",len(self.stack))



def main():
	print("This program simulates a last-in first-out (LIFO) stack.\n")
	# Creates object of Class Stack
	s = Stack()
	# User input instructions
	print("""When prompted: type "push" to push a value on the stack,
		type "pop" to pop a value from the stack, 
		type "quit" to exit the program. """)

	a = ""
	# Gets user input until user types 'quit'
	while a != "quit":
		# Gets user's first instruction, string is changed to lowercase for program ease
		a = str(input("\nWhat action would you like to complete? "))
		a.lower()

		if a == "push":
			n = (int(input("Type the number you'd like to push: ")))

			s.push(n)
			s.peek()	

		elif a == "pop":
			# If user tries to pop from an empty list program will return statement
			try:
				s.pop()
				s.peek()
			except IndexError:
				print("You cannot pop from an empty list.")
			

		elif a == "quit":
			quit()
		# Will print message if input is anything other than quit, push, pop, or quit	
		else:
			print("You have entered an incorrect action.")

	a = eval(input("\nWhat action would you like to complete? "))		



#prints authors name, class, and date
print("Steven Howe")
print("CIS110 Program 11")
#this function will print the current date and time using asctime()
print(time.asctime(time.localtime(time.time())))


if __name__ == '__main__':
	main()
