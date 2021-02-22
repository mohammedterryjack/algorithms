from typing import List

def quick_sort(values:List[int]) -> List[int]:
    if len(values) == 0: return values

    pivot = values.pop()
    less,equal,greater = [],[pivot],[]
    for value in values:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)
    return quick_sort(less)+equal+quick_sort(greater) 
