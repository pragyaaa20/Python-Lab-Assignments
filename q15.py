n = int (input("enter a number to check:"))
rev = 0
temp =n
if (n>=500 and n<=1000):
    while(n != 0):
        a = n%10
        rev = (rev*10) + a
        n = n//10
    if temp==rev:
        print("the number is palindrome")
    else:
        print("the  number is not palindrome")
else:
    print("the number is not in range")


