HEXdict = {
    0: '0', 
    1: '1',
    2: '2', 
    3: '3', 
    4: '4', 
    5: '5',
    6: '6', 
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

#Integer to Hex function
def D2H(num1):
    num1 = int(num1)    #turns input from num into int
    
    #opens two lists to append values to
    list1 = []
    list2 = []

    #This loop takes int and cycles it through two motions
    while num1 > 0:
        num2 = num1 % 16    #num2 is the remainder
        num1 = num1 // 16   #num 1 is then transformed to quotient of original num1
        list1.append(num2)
        
    for i in list1:
        hex1 = HEXdict[i]
        list2.append(hex1)

    str2 = ''.join(list2)

    #reversal of the string
    txt1 = str2 [::-1]
    return(txt1)


