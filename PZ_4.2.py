import random
N = random.randrange(1,99)
K = random.randrange(1,99)
print('N = ', N)
print('K = ', K)
r = N
q = 0
while r >= K:
 r -= K
 q += 1
print("Частное: ", q)
print("Остаток: ", r)
