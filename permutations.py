from typing import List

def permutations(remaining_values:List[int]) -> List[List[int]]:
    if not any(remaining_values): return [[]]
    value = remaining_values.pop()
    all_permutations = []
    for permutation in permutations(remaining_values):
        for index in range(len(permutation)+1):
            all_permutations.append(
                permutation[:index] + [value] + permutation[index:] 
            )
    return all_permutations

#print(permutations(["a","b","c"]))
