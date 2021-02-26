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

def a_star(
    graph:Dict[str,List[str]], 
    nodes_queue:List[str], 
    seen:Set[str],
    scoring_function:callable
) -> None:
    if not any(nodes_queue): return 
    node = nodes_queue.pop()
    if node not in seen: 
        print(node)
        connected_nodes = list(sorted(graph.get(node),key=scoring_function))
        nodes_queue += connected_nodes
        seen.add(node)
    a_star(graph,nodes_queue,seen,scoring_function)
    
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

#def example_heuristic(node:str) -> int:
#    """
#    heuristically score node
#    (better node = higher score)
#    """
#    GOAL = "F"
#    COORDINATES = {
#        'A' : (0,0), 'B' : (0,1), 'C' : (0,2),
#        'D' : (1,0), 'E' : (2,0), 'F' : (2,1)    
#    }
#    distance_to_goal = euclidean(COORDINATES.get(node),COORDINATES.get(GOAL)) + 1
#    return 1/distance_to_goal

#a_star(example_graph,["A"],set(),example_heuristic)
