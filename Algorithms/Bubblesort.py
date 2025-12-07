#Bubble Sort: Check each adj element and swap, check all the way
#Time complexity: O(n^2)

#Taking Input list
lst=[]
n = int(input("Number of elements you wish to enter:"))
print("\n")
for i in range(0,n):
    lst.append(int(input("Enter element in list:")))        # or lst = list(map(int,input().split()))

#Operation:
for i in range(0,n-1):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print("Sorted List:", lst)