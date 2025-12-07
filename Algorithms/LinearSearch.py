
#Taking Input list
lst=[]
n = int(input("Number of elements you wish to enter:"))
print("\n")
for i in range(0,n):
    lst.append(int(input("Enter element in list:")))

searching_element = int(input("Enter the element to search:"))

for i in range(0,n):
    if lst[i] == searching_element:
        print("Number found at index", i+1, "!")
        break
    
