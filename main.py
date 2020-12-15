import time

def ReverseNumber(n):
    return n*n

t0=time.time()
f = open('text.txt', 'r')

t1=time.time()
for line in f:
    print(ReverseNumber(int(line)))
print(t1-t0)
print(time.time()-t1)
f.close()