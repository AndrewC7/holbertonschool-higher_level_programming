#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
	        x = 32
        else:
	        x = 0
        print("{:c}".format(ord(letter) - x), end="")
    print( )
