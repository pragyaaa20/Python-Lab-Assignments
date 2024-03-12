num = int(input("enter a number:"))

isP = True
for i in range(2,num//2+1):
    if(num%i == 0):
        print('number is not prime')
        isP = False
        break

if(isP):
    print('number is prime')