def fibonacci(n:int, memory:dict={}) -> int:
    if n <= 2: return 1
    if n not in memory: memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]

#print(fibonacci(50))


def grid_traveller(x:int,y:int,memory:dict={}) -> int:
    if x==0 or y==0: return 0
    if x==1 and y==1: return 1
    coordinates = ','.join(map(str,sorted((x,y))))
    if coordinates not in memory: memory[coordinates] = grid_traveller(x-1,y) + grid_traveller(x,y-1)
    return memory[coordinates]

#print(grid_traveller(18,18))
