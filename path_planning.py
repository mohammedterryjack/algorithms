from typing import List,Dict,Set
from scipy.spatial.distance import euclidean

class Node:
    def __init__(self,name:str,weight:int=0,coordinates:Tuple[int,int]=(0,0)) -> None:
        self.name = name 
        self.coordinates = coordinates
        self.weight = weight
        self.previous = None
    
    def __repr__(self) -> str:
        return self.name
        
    def path_weight(self) -> int:
        if self.previous is None:
            return self.weight 
        return self.weight + self.previous.path_weight()

    def path_name(self) -> List[str]:
        if self.previous is None:
            return [self.name]
        return self.previous.path_name() + [self.name]
    
    def update_path(self,next_nodes:list) -> None:
        for node in next_nodes:
            if node.previous is None or node.previous.path_weight() > self.path_weight():
                node.previous = self
    
    def distance(self,target) -> int:
        return euclidean(self.coordinates,target.coordinates)
      
def breadth_first(
    graph:Dict[Node,List[Node]], 
    nodes_queue:List[Node], 
    seen:Set[Node],
    goal:Node
) -> None:
    if not any(nodes_queue): return 
    node = nodes_queue.pop(0)
    if node == goal:return
    if node not in seen: 
        print(node)
        connected_nodes = graph.get(node)
        node.update_path(connected_nodes)
        nodes_queue += connected_nodes
        seen.add(node)
    breadth_first(graph,nodes_queue,seen,goal)

def depth_first(
    graph:Dict[Node,List[Node]], 
    nodes_queue:List[Node], 
    seen:Set[Node],
    goal:Node
) -> None:
    if not any(nodes_queue): return
    node = nodes_queue.pop()
    if node == goal: return
    if node not in seen:
        print(node)
        connected_nodes = graph.get(node)
        node.update_path(connected_nodes)
        nodes_queue += connected_nodes
        seen.add(node)
    depth_first(graph,nodes_queue,seen,goal)


def a_star(
    graph:Dict[Node,List[Node]], 
    nodes_queue:List[Node], 
    seen:Set[Node],
    goal:Node
) -> None:
    if not any(nodes_queue): return 
    nodes_queue.sort(key=lambda node:node.path_weight() + node.distance(goal))
    node = nodes_queue.pop()
    if node == goal: return
    if node not in seen: 
        print(node)
        connected_nodes = graph.get(node)
        node.update_path(connected_nodes)
        nodes_queue += connected_nodes
        seen.add(node)
    a_star(graph,nodes_queue,seen,goal)
 

A = Node(name="A",weight=1,coordinates=(0,0))
B = Node(name="B",weight=2,coordinates=(0,1))
C = Node(name="C",weight=3,coordinates=(0,2))
D = Node(name="D",weight=4,coordinates=(1,0))
E = Node(name="E",weight=5,coordinates=(2,0))
F = Node(name="F",weight=6,coordinates=(2,1))
example_graph = {
 A : [B, C],
 B : [D, E],
 C : [F],
 D : [D],
 E : [F],
 F : []
}

#breadth_first(graph=example_graph,nodes_queue=[A],seen=set(),goal=F)
depth_first(graph=example_graph,nodes_queue=[A],seen=set(),goal=F)
#a_star(graph=example_graph,nodes_queue=[A],seen=set(),goal=F)
print(F.path_weight(),F.path_name())
