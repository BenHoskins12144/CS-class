




def INFOINPUT(F,S,L,H,E,G,O):
    for i in range(0,99):
        with open("myfile.py", "w") as INFOINPUTFILE:
            if PersonCount == i:
                INFOINPUTFILE.write("\n")
            
    
    
    if F == "":
        print("not provided")
        with open("myfile.py", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write("first name not provided or unknown ")
    else: 
        with open("myfile.py", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"Firstname = {F}  ")
            print(F)
    if S =="":
         print("not provided")
         with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nmiddle name not provided or unknown  ")
    else: 
        with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nMiddlename = {S}  ")
            print(S)
    if L =="":
         print("not provided")
         with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nlast name not provided or unknown  ")
    else: 
        with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nLastname = {L}  ")
            print(L)
    if H =="":
         print("not provided")
         with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nhight not provided or unknown ")
    else: 
        with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nHight = {H}  ")
        print(H)
    if E =="":
         print("not provided")
         with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write("\neye color not provided or unknown  ")
    else: 
        with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nEyeColor = {E}  ")
            print(E)
 
    if G =="":
        print("not provided")
        with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write("\ngender not provided or unknown ")
    else: 
        with open("myfile.txt", "w") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nGender = {G}  ")
            print(f"{G}")

 



   



F = input("input first name :")

S = input("input middle name :")

L = input("last name :")

H = input("Input hight :")

E = input("Input eye color :")

G = input("Input gender :")

O = 0

INFOINPUT(F,S,L,H,E,G,O)

