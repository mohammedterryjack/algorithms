from typing import List

def binary_search(values:List[int], target_value:int, start_index:int, end_index:int) -> int:
    """
    finds index of target_value using recursive binary search
    if target_value is not in set of values, returns -1
    """
    index_range = end_index - start_index
    if index_range <= 0: return -1
    mid_index = index_range//2
    split_index = start_index + mid_index 
    return split_index if values[split_index] == target_value else max(
        binary_search(values,target_value,start_index,split_index),
        binary_search(values,target_value,split_index+1,end_index)
    ) 
