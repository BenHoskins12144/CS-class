import math
print(f"gcf finder WOW!!!")
X=input("input number 1st number =")

Y=input("input 2nd number")
X=int(X)
Y=int(Y)
T=min(X,Y)
gcf=1
for i in range(1,int(T)+1):
      Y6=X%i
      Y5=Y%i
      if (Y6)==0 and (Y5)==(0):
            gcf=(i)
print(f"{gcf}")
    

    
    
