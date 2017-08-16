"calcular numero de fibonacci de forma optima - memoization"

mem = [1,1]

def fib(n):
    if n < len(mem):
        return mem[n]
    else:
        res = fib(n-1) + fib(n-2)
        mem.append(res)
        return res


fib(5000000000)
