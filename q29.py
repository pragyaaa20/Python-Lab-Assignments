n = int (input("enter the number of steps:"))
table = ["10* {} = {}".format(x,x*10) for x in range(1,n+1)]
print(table)


table = list(map(lambda x : x*10,range(1,n+1)))
print(table)