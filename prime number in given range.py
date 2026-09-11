start = int(input("Enter a Start Number: "))
end = int(input("Enter a End Number: "))

print("Prime Numbers:")

for num in range(start, end + 1):

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)   
