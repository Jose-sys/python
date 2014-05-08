"calcular numero de fibonacci de forma optima - memoization"

def fib(i):
    lista = [1,1]
    while len(lista) <= i+1:
        lista.append(lista[-1] + lista[-2])
    return lista[-1]


fib(5000000000)
