# Largest three number:
a=int(input("Enter a first number :"))
b=int(input("Enter a second number :"))
c=int(input("Enter a third number :"))

if a>b:
    if(a>c):
        print(" larger number=",a)
    else:
        print(" larger number=",c)
else:
    if(b>c):
        print("larger number=",b)
    else:
        print(" larger number=",c)
# Output:
# Enter a first number :85
# Enter a second number :99
# Enter a third number :68
# larger number= 99
