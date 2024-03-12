l =[1,2,3,4]
flag = 0
for i in range(0,len(l)-1):
    if l[i] >= l[i+1]:
        flag = 1
        break
if flag==0:
    print("sorted list")
else:
    print("unsorted list")