X=input("test if prime number =")
X=float(X)
for i in range(1,10):
    Y=X%i
    if Y==0: 
        print(f"{X} is not a prime number")
    

