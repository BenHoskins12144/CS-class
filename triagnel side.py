import math
X99=input("Do You Have Hypotnuse? 1=yes 2=no =")
Y5=X99
if Y5==("1"):
    X=input("input hypotnuse =")
    X=float(X)
    Y5=math.sqrt(X**2/2)
    print(f"{Y5}")

Y99=input("Do you have agecent or oposite side lenth? 1=yes 2=no =")
X5=Y99
if X5==("1"):
    X1=input("input agacent or oposite side =")
    X1=float(X)
    Y1=math.sqrt(X1**2+X1**2)*.707
    print(f"{Y1}")