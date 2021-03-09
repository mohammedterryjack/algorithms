class Node:
    def __init__(self, value:int) -> None:
        self.value = value 
        self.children = []

def sum_tree(node:Node) -> int:
    if node is None: return 0
    return node.value + sum(map(sum_tree,node.children))

#a = Node(1)
#b = Node(2)
#c = Node(3)
#d = Node(4)
#root = Node(5)
#c.children = [a,b]
#d.children = [c]
#root.children = [d]
#print(sum_tree(root))
