n = int(input("enter a number"))
def binarytooctal(n):
    if n>1:
        binarytooctal(n//8)
    print(n%8,end =" ")
binarytooctal(n)