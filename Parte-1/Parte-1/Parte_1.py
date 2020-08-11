#FIBONACCI ITERATIVO 

def fibo(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    return n2
for j in range(20):
    print(fibo(j))

#FIBONACCI RECURSIVO

def fibR(n):
    if n < 2:
        return n
    return fibR(n-1) + fibR(n-2)

for j in range(20):
    print(fiboR(j))

