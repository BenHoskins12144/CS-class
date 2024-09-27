# given opposite side and hypotnuse calculate angle
import math
from Benfunctions import radiansToDegrees
H=input("Input Hypotnuse : ")
O=input("Input Opposite : ")
H=float(H)
O=float(O)
Y=O/H
X=math.asin(Y)
X1=radiansToDegrees(X)
print(f"{X1}")