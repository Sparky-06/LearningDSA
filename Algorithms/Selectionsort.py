#Selection Sort: Find the smallest number from the list and bring it to the front and shift the rest of the pack.
#Time Complixity: O(n^2)

#Taking Input list
lst=[]
n = int(input("Number of elements you wish to enter:"))
print("\n")
for i in range(0,n):
    lst.append(int(input("Enter element in list:")))

#Operation:
for i in range(0,n-1):
    min_index = i
    for j in range(i+1, n):
        if lst[j]<lst[min_index]:
            min_index = j                #Finding index of min element
    
    min_val = lst.pop(min_index)         #Getting the min element out of lst
    lst.insert(i, min_val)       #And getting it inserted at the first place


print("Sorted list:", lst)
        
