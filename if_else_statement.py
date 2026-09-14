# 1) Largest three number:-
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
# Output:-
# Enter a first number :85
# Enter a second number :99
# Enter a third number :68
# larger number= 99

# 2) Check two number's are equal or not using function :
def check(a,b):
    if a==b:
        print("The given both number's are equal")
    else:
        print("The given number's are not equal ")
X=int(input("Enter a first number :"))
Y=int(input("Enter a second number :"))
check(X,Y)

# Output:
# Enter a first number :7
# Enter a second number :8
# The given number's are not equal

# 3) Check leap year or not :
year=int(input("Enter a Year :"))

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not Leap Year")

# Output:
# Enter a Year :2025
# Not Leap Year
 
