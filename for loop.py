# Fibonacci sequence up to n terms :-
n=int(input("Enter a terms :"))
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
