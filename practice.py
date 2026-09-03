input_user=input("Enter a Numbers :");
digit_to_remove=input("Enter a Digit to Remove :")
result=""
for Character in input_user :
    if Character!=digit_to_remove :
        result+=Character;
print(" Number After Remove:",result);
