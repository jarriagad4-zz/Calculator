#Decimal to Binary (D2B) function
def D2B(num1):
    list1 = []

    num1 = int(num1)
    #loops stays open as long as num1 is more than 0 (may need to be adjusted)
    while num1 > 0:
        #for even numbers
        if num1 % 2 == 0:
            list1.append('0')
            num1 = num1 / 2
        #for odd numbers
        if num1 % 2 != 0:
            list1.append('1')
            num1 = (num1 - 1) / 2

    #make string from list
    str1 = ''.join(list1)

    #reversal of the string
    txt = str1 [::-1]
    return(txt)

#Binary to Decimal (B2D) function
def B2D(num1): 
    tot = '0'
    for i in num1:
        i = int(i)
        tot = int(tot)
        tot = tot * 2 + i
    return(str(tot))





