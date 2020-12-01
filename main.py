import time

def ReverseNumber(n):
    return n*n

t0=time.time()
f = open('text.txt', 'r')

for line in f:
    print(ReverseNumber(int(line)))

print(time.time()-t0)
f.close()