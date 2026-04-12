def somar(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def subtrair(*args):
    total = args[0]
    for arg in args[1:]:
        total -= arg
    return total

def multiplicar(*args):
    total = args[0]
    for arg in args[1:]:
        total *= arg
    return total

def dividir(a, b):
    total = a/b
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return total