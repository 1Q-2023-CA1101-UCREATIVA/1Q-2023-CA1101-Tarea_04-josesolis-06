import math
r = math.sqrt((x-0)**2+(y-0)**2)
print(r)

def puntaje(x, y):
if (5 < r <= 10):
    print("1 punto")
elif (1 < r <= 5):
    print("5 puntos")
elif (r <= 1):
    print("10 puntos")
elif(r>=10.1):
    print("0 puntos")

puntaje(1,12)
puntaje(3,6)
puntaje(2,4)
puntaje(0.15,0.45)