a = (i for i in range(1, 100))
print(a)

def generator():
    yield "hell"
    yield  "python"
    yield 11

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))

import sys
print(sys.getsizeof(([i for i in range(1, 10000+1)])))
print(sys.getsizeof(((j for j in range(1, 10000+1)))))

import time

def lazy_evaluation(n):
    print("1 sec sleep")
    time.sleep(1)
    return  n

n_list = [lazy_evaluation(n) for n in range(1,6)]
for i in n_list:
    print(i)

n_generator = (lazy_evaluation(n) for n in range(1, 6))
for j in n_generator:
    print(j)