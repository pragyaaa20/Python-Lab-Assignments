num = int(input('enter a number:'))

digit = 0
 
i = num
while(i != 0):
    digit += 1
    i = i//10

sum = 0

i = num
while(i != 0):
    sum += (i%10)**digit
    i = i//10

if sum == num:
    print('number is armstrong')
else:
    print('number is not armstrong')
    
