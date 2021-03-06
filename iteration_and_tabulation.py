from typing import List

def fibonacci(n:int) -> int:
    memory = [0]*(n+2)
    memory[1] = 1
    for index in range(n):
        memory[index+1] += memory[index]
        memory[index+2] += memory[index]
    return memory[n]

#print(50,fibonacci(50))


def create_sum_with_least_values(target_sum:int, values:List[int]) -> List[int]:
    memory = [None]*(target_sum + max(values))
    memory[0] = []
    for index in range(target_sum):
        if memory[index] is not None:
            subvalues = memory[index]
            for offset in values:
                new_subvalues = subvalues + [offset]
                if memory[index+offset] is None or len(new_subvalues) < len(memory[index+offset]): 
                    memory[index+offset] = new_subvalues
    return memory[target_sum]

#print(create_sum_with_least_values(111,[3,23,10]))
