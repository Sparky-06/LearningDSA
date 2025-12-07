import array as arr
x = list(range(0,1001,5))

for i in range(0, len(x)):
    print(x[i], end = " ")
print("\n")

num = int(input("Enter element to search:"))
print("\n")
try:
    index = x.index(num)
    print(f"{num} is at {index} index.")

except:
    print(f"{num} is not in list.")