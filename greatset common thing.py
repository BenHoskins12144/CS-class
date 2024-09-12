import math

X=input("input number 1st number =")
X=int(X)
Y=input("input 2nd number")
Y=int(Y)
T=min(X,Y)
for i in range(1,int(T/2)+1):
        Y6=X%i
        Y5=Y%i
        if (Y6)==0 and (Y5)==(0):
              print(f"{T} {Y5} {Y6}")
    

    
    
    