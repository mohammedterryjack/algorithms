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


def create_word_with_substrings(target_word:str, substrings:List[str]) -> List[str]:
    target_index = len(target_word)
    mex_offset = len(max(substrings,key=len))
    memory = [None]*(target_index + mex_offset)
    memory[0] = []
    for index,character in enumerate(target_word):
        if memory[index] is not None:
            for substring in substrings:
                if substring.startswith(character):
                    memory[index + len(substring)] = memory[index] + [substring]
    return memory[target_index]


#print(create_word_with_substrings("abcdef",["abc","cd","def","cde"]))
#print(create_word_with_substrings("skateboard",["bo","ate","sk","ska","boar","d"]))
