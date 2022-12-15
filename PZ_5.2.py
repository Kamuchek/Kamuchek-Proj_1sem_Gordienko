import random
def RectPS(x1,y1,x2,y2,Result):
    a = abs(x1-x2)
    b = abs(y1-y2)
    print("a = ", a)
    print("b = ", b)
    Result['P'] = 2*(a+b)
    Result['S'] = a*b
    return
x1, x2 = random.sample(range(-10, 10), 2)
y1, y2 = random.sample(range(-10, 10), 2)
print("x1 = ",x1,"; y1 = ",y1)
print("x2 = ",x2,"; y2 = ",y2)
R = {'P' : None, 'S' : None}
RectPS(x1,y1,x2,y2,R)
print('P = ', R['P'])
print('S = ', R['S'])
