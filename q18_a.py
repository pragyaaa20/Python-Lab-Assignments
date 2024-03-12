n = int(input("enter a number"))
def binarytodecimal(n):
    if n>1:
        binarytodecimal(n//2)
    print(n%2,end =" ")
binarytodecimal(n)