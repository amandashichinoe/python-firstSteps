#função recursiva para calcular o fatorial de um número

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(3))