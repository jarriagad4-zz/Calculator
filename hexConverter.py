from BD import *
from HD import *

#TODO change this to calculator type (Ex.: Decimal to hex or decimal to binary or etc...)
input1 = input('Choose a calculator: \n A. Integer to Binary \n B. Binary to Integer \n C. Integer to Hex \n D. Hex to Integer')


if input1 in ['A' , 'a']:
    num1 = input('Enter an integer: ')
    print('Binary: ' + D2B(num1))
elif input1 in ['B', 'b']:
    num1 = input('Enter a binary number: ')
    print('Integer: ' + B2D(num1))
elif input1 in ['C', 'c']:
    num1 = input('Enter an integer: ')
    print('Hex value: ' + D2H(num1))
else:
    print('Not a valid input')






