from typing import List, Tuple


def index(values:List[int], target_value:int) -> int:
    """
    finds index of target_value using recursive binary search
    if target_value is not in set of values, returns -1
    """
    return binary_search(
        ordered_indexed_values = sorted(
            enumerate(values),
            key=lambda index_value_pair:index_value_pair[-1]
        ),
        target_value=target_value
    )

def binary_search(ordered_indexed_values:List[Tuple[int,int]], target_value:int) -> int:
    if not any(ordered_indexed_values): return -1
    
    middle_index = len(ordered_indexed_values)//2
    index,value = ordered_indexed_values[middle_index]
    
    if target_value==value: 
        return index
    return binary_search(
        ordered_index_values=ordered_indexed_values[:middle_index],
        target_value=target_value
    ) if target_value < value else binary_search(
        ordered_index_values=ordered_indexed_values[middle_index+1:],
        target_value=target_value
    )
