# find if the given number is a palindrome or not?
a=input("enter the number")
d=a[::-1]
if a==d:
    print(f"the number is {a} palindrome:")
else:
      print(f"the number is {a} not palindrome:")