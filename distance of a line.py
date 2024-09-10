import math
X=input("X1=")
Y=input("Y1=")
X2=input("X2=")
Y2=input("Y2=")
X=float(X)
Y=float (Y)
X2=float(X2)
Y2=float(Y2)
R=X-X2
G=Y-Y2
L=R**2+G**2
H=math.sqrt(L)
H=float(H)
M1=(X+X2)/2
M2=(Y+Y2)/2
print(f"the lenth of the line is {H} the midpoint is {M1,M2}")
#7 13 4 -2