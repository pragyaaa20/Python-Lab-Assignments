num = int(input('enter a number:'))

ans = 0
temp = num

while(num != 0):
    ans = ans*10 + num%10
    num = num//10

if temp == ans:
    print('number is palindrome')
else:
    print('number is not palindrome')