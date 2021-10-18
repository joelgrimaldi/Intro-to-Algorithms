import time

def fib1(n):
    if n<=0: 
        print("Input invalid")
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fib1(n-1)+fib1(n-2)

start = time.time()

for x in range(1,44):
    print(x,fib1(x),time.time()-start)
    start = time.time()