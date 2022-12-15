import random
A = random.randrange(1,11)
B = random.randrange(A+1,21)
print("A = ",A)
print("B = ",B)
print()
K = 1
for i in range(A,B+1):
    for j in range(0,K):
        print(i,end=" ")
    print()
    K += 1
