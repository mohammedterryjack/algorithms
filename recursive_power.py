def is_odd(number:int) -> bool:
    return bool(number%2)

def power_efficiently(number:float, power:int) -> float:
    if not(power): return 1.
    result = power_efficiently(number,power//2)**2
    if is_odd(power): result *= number  
    return float(result)
