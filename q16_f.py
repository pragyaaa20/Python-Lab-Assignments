num = int(input("Enter the no. of rows: "))
val = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(val, end=" ")
        val+=1
    print("\r")
