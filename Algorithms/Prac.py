lst = []
n = int(input())
for i in range(0,n):
    lst.append(int(input("Enter value in list:")))


for i in range(0,n-1):
    index = i
    for j in range(i, n):
        if lst[j]<lst[index]:
            index = j
    lst[i], lst[index] = lst[index], lst[i]

print(lst)