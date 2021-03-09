class Node:
    def __init__(self, name:str,value:int) -> None:
        self.name = name
        self.value = value 
        self.children = []
     
    def __repr__(self) -> str:
        return self.name


def depth_first_search(stack:List[Node]) -> int:
    if not any(stack): return 0 
    node = stack.pop()
    print(node)
    stack.extend(node.children)
    return node.value + depth_first_search(stack)

def breadth_first_search(queue:List[Node]) -> int:
    if not any(queue): return 0
    node = queue.pop(0)
    print(node)
    queue.extend(node.children)
    return node.value + breadth_first_search(queue)

def simplified_breadth_first_search(node:Node) -> int:
    if node is None: return 0
    return node.value + sum(map(simplified_breadth_first_search,node.children))

# a = Node("a",1)
# b = Node("b",2)
# c = Node("c",3)
# d = Node("d",4)
# e = Node("e",5)
# f = Node("f",6)
# g = Node("g",7)
# b.children = [d,e]
# c.children = [f,g]
# a.children = [b,c]
# print(depth_first_search([a]))
# print(breadth_first_search([a]))
# print(simplified_breadth_first_search(a))

