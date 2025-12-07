class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

a = (((-5, 12, None),-3,-1),0,(30, 5, -10))

def tuptobin(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = tuptobin(data[0])
        node.right = tuptobin(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree1 = tuptobin(a)

def display(node, space = "\t", level = 0):
    if node == None:
        print(space*level + "e")
        return
    if node.left is None and node.right is None:
        print(space*level, node.key)
        return
    
    display(node.right, space, level+1)
    print(space*level, node.key)
    display(node.left, space, level+1)


print(a)
display(tree1, '    ')