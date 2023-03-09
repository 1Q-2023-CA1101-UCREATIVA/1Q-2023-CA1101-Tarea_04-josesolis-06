import math

def puntaje(x, y):
    r = math.sqrt((x)**2+(y)**2)
    if (5 < r <= 10):
        return 1
    elif (1 < r <= 5):
        return 5
    elif (r <= 1):
        return 10
    elif(r>=10.1):
        return 0

print(puntaje(2,7))
print(puntaje(3,6))
print(puntaje(2,4))
print(puntaje(0.15,0.45))