#Insertion sort: Bring in element one by one from index from left and sort it right away

#Taking Input list
lst=[]
n = int(input("Number of elements you wish to enter:"))
print("\n")
for i in range(0,n):
    lst.append(int(input("Enter element in list:")))

#Operation:

for i in range(1, n):
    insert_index = i
    current_val = lst.pop(i)
    for j in range(i-1, -1, -1):
        if lst[j] > current_val:
            insert_index = j
        else:
            break
    lst.insert(insert_index, current_val)

print("Sorted List:", lst)