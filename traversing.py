from typing import List,Dict,Set

def breadth_first(
    graph:Dict[str,List[str]], 
    nodes_queue:List[str], 
    seen:Set[str]
) -> None:
    if not any(nodes_queue): return 
    node = nodes_queue.pop(0)
    if node not in seen: 
        print(node)
        connected_nodes = graph.get(node)
        nodes_queue += connected_nodes
        seen.add(node)
    breadth_first(graph,nodes_queue,seen)

def depth_first(
    graph:Dict[str,List[str]], 
    nodes_queue:List[str], 
    seen:Set[str]
) -> None:
    if not any(nodes_queue): return
    node = nodes_queue.pop()
    if node not in seen:
        print(node)
        connected_nodes = graph.get(node)
        nodes_queue += connected_nodes
        seen.add(node)
    depth_first(graph,nodes_queue,seen)
    
#example_graph = {
#  'A' : ['B','C'],
#  'B' : ['D', 'E'],
#  'C' : ['F'],
#  'D' : ['D'],
#  'E' : ['F'],
#  'F' : []
#}
#breadth_first(example_graph,["A"],set())
#depth_first(example_graph,["A"],set())
