import math
X99=input("Do You Have Hypotnuse?")
Y5=X99
if Y5==("yes"):
    X=input("input hypotnuse")
    X=float(X)
    Y5=math.sqrt(X**2/2)
    print(f"{Y5}")

Y99=input("Do you have agecent or oposite side lenth?")
X5=Y99
if X5==("Yes"):
    X1=input("input agacent or opisote side")
    X1=float(X)
    Y1=X1/.707
    print(f"{Y1}")