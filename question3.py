#write a program to find the factorial of a nummber
def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)
    

c=int(input("enter the number"))
d=fact(c)
print(f"the factorial of {c} is",d)