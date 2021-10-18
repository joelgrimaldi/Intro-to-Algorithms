import time

def fib2(n):
    if n==0: return 0
    f = [0,1]
    for x in range(2,n):
        f.append(f[x-1] + f[x-2])
    return f[n-1]

start = time.time()

for x in range(1,44):
    for y in range(1000001):
        fib2(x)
    print(x,fib2(x),(time.time()-start)/1000000)
    start = time.time()