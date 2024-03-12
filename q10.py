num = int(input('enter a number:'))

ans = 0

while(num != 0):
    ans = ans*10 + num%10
    num = num//10

print(ans)