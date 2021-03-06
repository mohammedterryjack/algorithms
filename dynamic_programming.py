from typing import List,Dict, Optional

def fibonacci_recursion(n:int, memory:dict={}) -> int:
    if n <= 2: return 1
    if n not in memory: memory[n] = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    return memory[n]

#print(50,fibonacci_recursion(50))

def fibonacci_iteration(n:int) -> int:
    memory = [0]*(n+2)
    memory[1] = 1
    for index in range(n):
        memory[index+1] += memory[index]
        memory[index+2] += memory[index]
    return memory[n]

#print(50,fibonacci_iteration(50))


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

def create_word_with_substrings(target_word:str, substrings:List[str],memory:Dict[str,List[str]]={}) -> List[str]:
    if not any(target_word): return []
    if target_word not in memory:
        prefix_combination = None
        for prefix in substrings:
            if target_word.startswith(prefix):
                valid_prefixes = create_word_with_substrings(target_word.lstrip(prefix),substrings)
                if valid_prefixes is not None:
                    prefix_combination = valid_prefixes + [prefix]
                    break 
        memory[target_word] = prefix_combination
    return memory[target_word]

#print(create_word_with_substrings("abcdef",["abc","cd","def","cde"]))
#print(create_word_with_substrings("skateboard",["bo","ate","sk","ska","boar","d"]))


def create_sum_with_least_values(target_sum:int, values:List[int],memory:Dict[str,Optional[List[int]]]={}) -> Optional[List[int]]:
    if target_sum < 0: return  
    if target_sum == 0: return []

    if target_sum not in memory: 
        shortest_combination = None
        for value in values:
            results = create_sum_with_least_values(target_sum-value,values)
            if results is None: continue
            combination = results + [value]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination
        memory[target_sum] = shortest_combination
    
    return memory[target_sum]

#print(create_sum_with_least_values(111,[3,23,10]))
