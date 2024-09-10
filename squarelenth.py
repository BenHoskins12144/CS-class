import math
X=input("input")
#input is side of sqaure
X=float(X)
Y=X**2
#Y is the area of the square 
E=Y/3.14
L=math.sqrt(E)
L=float(L)
E=float(E)
#E should be the area of the square/circle devided by pi getting the
T=E/2
#T seperates the lines devding by 2 gettting the circumferece
F=2*math.sqrt(math.pi*Y)
F=float(F)
print (f"{X} {Y} {F} ")
print (f"the circumfrence of a circle with the same area of a square with the hight of {X} is {F} and the radius is {T}")
P=T**2*3.14
print(f"{P} radius {L}")
