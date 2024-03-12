n = int (input("enter a number:"))
def geomatric_sum(n):
    if n < 1:
        return 0
    else:
        return (pow(2,n) + geomatric_sum(n-1))
print("the gemotric sum of the given number is :",geomatric_sum(n))