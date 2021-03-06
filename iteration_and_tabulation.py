

def fibonacci(n:int) -> int:
    memory = [0]*(n+2)
    memory[1] = 1
    for index in range(n):
        memory[index+1] += memory[index]
        memory[index+2] += memory[index]
    return memory[n]

#print(50,fibonacci(50))
