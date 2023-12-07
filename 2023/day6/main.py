import math
time, distance = open(0).read().split("\n")

def getInt(l):
    return int(l.split(":")[1].replace(" ",''))
time = getInt(time) 
distance = getInt(distance)

print(time, distance)

ans = 1

def check(time, totalTime, distance):
    return 0 > time **2 - totalTime * time + distance
l, r = 0, time
def roots():
    a = 1
    b = -time
    c = distance
    num1 = -b + math.sqrt(b * b - 4 * a * c)
    num2 = -b - math.sqrt(b * b - 4 * a * c)
    den = 2 * a
    return (num2/den, num1/den)

r1, r2 = roots()
print(r1, r2)
r1 = math.ceil(r1)
r2 = math.floor(r2)
print(check(r1, time, distance), check(r2, time, distance))
print(r2 - r1 + 1)