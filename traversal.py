from typing import List,Dict,Set

def breadth_first_traversal(
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
    breadth_first_traversal(graph,nodes_queue,seen)

    
#example_graph = {
#  'A' : ['B','C'],
#  'B' : ['D', 'E'],
#  'C' : ['F'],
#  'D' : ['D'],
#  'E' : ['F'],
#  'F' : []
#}
#breadth_first_traversal(example_graph,["A"],set())
