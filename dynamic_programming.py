from typing import List,Dict

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


def is_sum_in_values(target_sum:int, values:List[int],memory:Dict[str,bool]={}) -> bool:
    if target_sum < 0: return False 
    if target_sum == 0: return True
    for value in values:
        if is_sum_in_values(target_sum-value,values): 
            if target_sum not in memory: memory[target_sum] = True
            return memory[target_sum]
    if target_sum not in memory: memory[target_sum] = False
    return memory[target_sum]

#print(is_sum_in_values(10,[19,7,44,3]))
