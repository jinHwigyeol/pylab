import math

def spherevolum(r):
    v = (4.0/3.0) * math.pi * (r**3)
    return v

def sphere(r):
    s = 4.0 * math.pi * (r**2)
    return s

r = float(input("구의 반지름은? : "))

print("부피는 : ",spherevolum(r))
print("넓이는 :",sphere(r))