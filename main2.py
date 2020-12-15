import time

def Number(n):
    return n*n

t0=time.time()
f = open('text.txt', 'r')
t1 = time.time()
for line in f:
    print(Number(int(line)))
print(t1- t0)
print(time.time()-t1)
f.close()

from threading import Thread
import time

t0=time.time()

with open('text.txt', 'r') as f:
    line = f.readlines()

t1 = time.time()


def funk(n, en=1, lst = []):
    while True:
        if n == 1:
            lst.append(line[en - 1][:-1])
            en += 1
        elif n == 2 and len(lst) > 0:
            print(lst[-1] * lst[-1])
            en += 1
        else:
            break


th1 = Thread(target=funk, args=(1, ))
th2 = Thread(target=funk, args=(2, ))

th1.start()
th2.start()
th1.join()
th2.join()
f.close()
print(t1-t0)
print(time.time()-t1)


from concurrent.futures import ThreadPoolExecutor, as_completed
import time

t0 = time.time()

def Number(lst, n, ls=[]):
    ls.append(int(lst[n]))
    for i in range(len(ls)):
        print(ls[i] * ls[i])

with open('text.txt', 'r') as f:
    lst = f.readlines()


with ThreadPoolExecutor(max_workers=2) as pool:
    t1 = time.time()
    r = [pool.submit(f, lst, i) for i in range(10000)]

    for future in as_completed(r):
        print(future.result())

f.close()
print(t1 - t0)
print(time.time()-t1)