class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


a = (((-1,0,1),3,2),4,(5,6,(7,8,None)))

def tuppletobinary(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = tuppletobinary(data[0])
        node.right = tuppletobinary(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

node0 = TreeNode(4)
node1 = TreeNode(3)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

tree1 = node0

tree2 = tuppletobinary(a)



def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)   

display_keys(tree2,'    ')