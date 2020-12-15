from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def ReverseNumber(n):
    n = int(n)

    return n*n

t0=time.time()
f =  open('text.txt', 'r')
t1 = time.time()
with ThreadPoolExecutor(max_workers=3) as pool:
    r = [pool.submit(ReverseNumber, line) for line in f]

    for future in as_completed(r):
        print(future.result())

f.close()
print(t1-t0)
print(time.time()-t1)