# Author: Steven Howe
# Class: CIS 120 Data Structures
# Project: 2
# Date: 9/11/2019
# Purpose: A quiz game to identify the capitals of states

import random


class StateQuiz:

    def __init__(self):
        self.game = self  # initialize

    def intro_message(self):
        """Prints message intro with instructions."""
        print("""
        Welcome! This is the State Capital Quiz. The object of 
        the game is to guess as many correct state capitals as you can.
        You get to choose how many rounds you play, good luck!""")

    def read_file(self):
        """Reads file and appends lines to a list and returns the list."""
        data = []
        file = open("StatesCapitals.txt", "r")  # opens StatesCapitals.txt

        for x in file:  # reads each line of file
            data.append(x)  # appends line to a list
        # return the data list
        """
        print(data)  # to test functioning
        """
        return data

    def pick_rounds(self):
        """Asks for user input for number of rounds, returns a int."""
        pick = input("\nEnter the amount of rounds you'd like to play! ")  # get input for amount of rounds to play
        return int(pick)  # returns user answer as an int

    def get_data(self, data):
        """Generates random int and obtains corresponding index of file, then strips whitespace,
        splits line into separate variables which are then returned."""
        unit_index = random.randint(1, 50)  # generate random int
        line = data[unit_index]  # obtain file line at the given index
        line = line.strip()  # gets rid of whitespace
        state, capital = line.split(",")   # Remove comma and make state and capital into separate entities
        """
        print(state) # For testing purposes
        print(capital) # For testing purposes
        """
        return state, capital

    def get_answer(self, state):
        """Asks user for answer to question then returns the answer."""
        answer = input(f"\nWhat is the capital of {state}? ")  # formats state from get_data into prompt

        return answer

    def compare(self, answer, capital):
        """Compares the given user answer to the actual correct answer,
        prints a message based on being correct or incorrect, accumulates
        a wrong or right answer and returns these values."""
        correct = 0
        wrong = 0

        if answer.lower() == capital.lower():  # compares answer from get_answer to capital from get_data
            print("You got it correct!")  # prints if answer is correct
            correct += 1
        elif answer.lower() != capital.lower():
            print(f"Sorry, the right answer was {capital}.")   # prints if answer is wrong
            wrong += 1
        else:
            print("Something went wrong!")  # prints if something other than above occurs

        return correct, wrong  # return count for right or wrong answer

    def count_rounds(self, correct, wrong):
        """Takes counts of correct and wrong answers and tallies them up and
        shows the user their win/loss record."""
        final_correct = 0
        final_wrong = 0
        final_correct += correct  # take count from compare and accumulate tally
        final_wrong += wrong

        print(f"\nYou won {final_correct} rounds and lost {final_wrong} rounds.")


def main():
    correct = 0
    wrong = 0
    game = StateQuiz()
    game.intro_message()
    rounds = game.pick_rounds()

    for x in range(rounds):  # will run through game for amount of rounds decided by user
        data = game.read_file()
        state, capital = game.get_data(data)
        answer = game.get_answer(state)
        x, y = game.compare(answer, capital)
        correct += x
        wrong += y

    game.count_rounds(correct, wrong)  # tallies and prints final number of wins/losses


if __name__ == '__main__':
    main()

