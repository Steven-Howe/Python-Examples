"""
Program Name: CIS110 Program 5
Program Description: This program encodes and decodes a Casesar cipher.
Author: Steven Howe
Date Created: 2/25/2019
Notes of Interest: Uses the Python time library.

"""
import time


def main():

    print("This program encodes a message into Caesar cipher.")
    print()

    key = int(input("Enter the key shift value (#): "))
    plain = str(input("Enter the phrase to encode: ")).upper()

    cipher = ""
    decrypt = ""

     
    alphaList = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                 "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

   

    for letter in plain:
        index = alphaList.index(letter)
        pos = (int(index)+ int(key))% 26
        cipher = cipher + chr(ord(letter) + pos)


    for letter in cipher:
        decrypt = decrypt + chr(ord(letter) - pos)

    print("Original message was: ",plain)
    print()
    print("Encoded message follows: ",cipher)
    print()
    print("Decrypted message follows: ",decrypt)



    #prints authors name, class, and date
    print("Steven Howe")
    print("CIS110 Program X")
    #this function will print the current date and time using asctime()
    print(time.asctime(time.localtime(time.time())))

main()
