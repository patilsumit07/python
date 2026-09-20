# Fibonacci sequence up to n terms :-
n=int(input("Enter a terms :-"))
a=0
b=1
print("Fibonacci Series")
for i in range(n):
    print(a,end ="\t")
    c=a+b
    a=b
    b=c

# Output :-
# Enter a terms :5
# Fibonacci Series
# 0       1       1       2       3


# Muliplication table from 1 to 10 :-
for i in range(1,11):
    print("\nTable of",i)

    for j in range(1,11):
        print(i,"x",j,"=",i*j)

# Output :-
# Table of 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# like this table 1 to 10     
