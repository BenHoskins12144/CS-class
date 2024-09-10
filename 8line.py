X=input("input number")
X=float(X)
for i in range(1,11):
    Y=X%i
    if Y==0:
        print(f"Yes {X} is devisable by {i} ")
        