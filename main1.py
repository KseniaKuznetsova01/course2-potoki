from threading import Thread
import time
t0=time.time()

f = open('text.txt', 'r')
def funk(n):

    for line in f:
        line = int(line)
        print(n, line*line)


th1 = Thread(target=funk, args=(1, ))
th2 = Thread(target=funk, args=(2, ))
t1=time.time()
th1.start()
th2.start()
th1.join()
th2.join()
f.close()
print(t1-t0)
print(time.time()-t1)