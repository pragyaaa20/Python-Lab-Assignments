n =int (input("enter a number:"))
curr_number = 1
prev_number = 0
print("the series:",prev_number,curr_number,end = " ")
for i in range (2,n):
    n3=  prev_number + curr_number
    prev_number = curr_number
    curr_number = n3
    
    print(curr_number, end = " ")
print("\r")
