def fibonacci(n:int, memory:dict={}) -> int:
    if n <= 2: return 1
    if n not in memory: memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]

#print(fibonacci(50))
