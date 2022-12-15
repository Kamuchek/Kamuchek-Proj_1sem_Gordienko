import random
N = random.randrange(1000,10000)
N = 2222
print("Число: ", N)
p1 = int(N/100)
p2 = N-p1*100
p2_d1 = int(p2/10)
p2_d0 = p2 - p2_d1*10
print("Половина 1: ", p1)
print("Половина 2: ", p2)
print("Десятки: ", p2_d1)
print("Единицы: ", p2_d0)
x = (p1 == (p2_d0*10 + p2_d1))
print("Число одинаково слева направо и справа налево: ", x)
