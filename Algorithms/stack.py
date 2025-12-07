class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, ele):
        self.stack.append(ele)
        self.top+=1
        print(self.stack)
    
    def pop(self):
        if self.stack:
            self.stack.pop(self.top)
            self.top -= 1
            print(self.stack)
        else:
            print("Stack is empty")

    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(self.top)

    def isEmpty(self):
        if self.top == -1:
            print(True)
        else:
            print(False)


    def size(self):
        print(self.top+1)
    
stack1 = Stack()

while True:
    print()
    print("1 for push")
    print("2 for pop")
    print("3 for peek")
    print("4 for isEmpty")
    print("5 for size")
    print("6 for exit")
    choice = int(input("Enter choice:"))

    if choice == 1:
        num = int(input("Enter push ele:"))
        stack1.push(num)

    elif choice == 2:
        stack1.pop()

    elif choice == 3:
        stack1.peek()
    
    elif choice == 4:
        stack1.isEmpty()
    
    elif choice == 5:
        stack1.size()
    
    elif choice == 6:
        break

    print()
    