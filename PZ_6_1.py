import random
N = random.randrange(2,10)
A = random.randrange(-10,10)
D = random.randrange(-5,5)
print("N = ", N)
print("A = ", A)
print("D = ", D)
a = [A * (D**i) for i in range(N)]
print(a)
D = []
for i in range(0,len(a)-1):
    D.append(a[i+1] / a[i])
min_D = min(D)
max_D = max(D)
print("Min:",min_D)
print("Max:",max_D)
if int(round(min_D - max_D)) == 0:
    print("Denominator of progression:",min_D)
else:
    print("0?")
