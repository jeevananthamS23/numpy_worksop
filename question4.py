#write a program to find the sum of digits of a given number'
def  dig(a):
    if a<10:
        return a
    else:
        return a%10+dig(a//10)
    
c=int(input("enter the number"))
print("the sum of the digit is", dig(c))
