from typing import List,Dict, Optional

def fibonacci(n:int, memory:Dict[str,int]={}) -> int:
    if n <= 2: return 1
    if n not in memory: memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]

#print(fibonacci(50))


def grid_traveller(x:int,y:int,memory:Dict[str,int]={}) -> int:
    if x==0 or y==0: return 0
    if x==1 and y==1: return 1
    coordinates = ','.join(map(str,sorted((x,y))))
    if coordinates not in memory: memory[coordinates] = grid_traveller(x-1,y) + grid_traveller(x,y-1)
    return memory[coordinates]

#print(grid_traveller(18,18))

def create_sum_with_values(target_sum:int, values:List[int],memory:Dict[str,Optional[List[int]]]={}) -> Optional[List[int]]:
    if target_sum < 0: return  
    if target_sum == 0: return []
    for value in values:
        results = create_sum_with_values(target_sum-value,values)
        if results is not None:
            if target_sum not in memory: memory[target_sum] = results + [value]
            return memory[target_sum]
    if target_sum not in memory: memory[target_sum] = None
    return memory[target_sum]

#print(create_sum_with_values(10,[19,7,44,3]))
