from typing import List

def quick_sort(values:List[int]) -> List[int]:
    if not any(values): return values

    pivot = values.pop()
    less,equal,greater = [],[pivot],[]
    for value in values:
        if value < pivot:
            less.append(value)
        elif value > pivot:
            greater.append(value)
        else:
            equal.append(value)
    return quick_sort(less)+equal+quick_sort(greater) 
