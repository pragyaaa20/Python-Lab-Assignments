'''l = [2,4,6,8]
large = l[0]
small = l[0]
for ele in range(0,len(l)):
    if large <  ele:
        large = ele
    if small > ele:
        small = ele
print("largest:",large)
print("smallest:",small)'''


'''l = [3,5,10,6]
l.sort(reverse=True)
print("largest element in a list:",l[0])
l.sort()
print("smallest elements in alist:",l[0])'''


l = [6,10,11,19,3,7]
print("smallest element:",min(l))
print("largest element:",max(l))
