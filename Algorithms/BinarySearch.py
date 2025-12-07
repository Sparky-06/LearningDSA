
#Taking Input list
lst=[]
n = int(input("Number of elements you wish to enter:"))
print("\n")
for i in range(0,n):
    lst.append(int(input("Enter element in list:")))

search = int(input("Enter number to find:"))
low = 0
high = len(lst)-1

while low<=high:
    a = (low+high)//2
    if lst[a] == search:
        print(lst)
        print(f"Element found at {a+1} position")
        break

    elif lst[a] > search:
        high = a-1

    elif lst[a] < search:
        low = a+1

if low > high:
    print("Element not present")