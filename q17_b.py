num = int(input('enter a number:'))
def sum(num):
    s = 0
    for i in range(1,num+1):
         s = s + i
    print("sum of natural number is:", s)
sum(num)