




def INFOINPUT(F,S,L,H,E,G,):
            
    
    
    if F == "":
        print("not provided")
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nFirstname = not provided or unknown ")
    else: 
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nFirstname = {F}  ")
            print(F)
    if S =="":
         print("not provided")
         with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nMiddlename = not provided or unknown  ")
    else: 
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nMiddlename = {S}  ")
            print(S)
    if L =="":
         print("not provided")
         with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nLastname = not provided or unknown  ")
    else: 
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nLastname = {L}  ")
            print(L)
    if H =="":
         print("not provided")
         with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nHight = not provided or unknown ")
    else: 
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nHight = {H}  ")
        print(H)
    if E =="":
         print("not provided")
         with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nEyecolor = not provided or unknown  ")
    else: 
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nEyeColor = {E}  ")
            print(E)
 
    if G =="":
        print("not provided")
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write("\nGender = not provided or unknown ")
    else: 
        with open("myfile.csv", "a") as INFOINPUTFILE:
            INFOINPUTFILE.write(f"\nGender = {G}  ")
            print(f"{G}")

 



   



F = input("input first name :")

S = input("input middle name :")

L = input("last name :")

H = input("Input hight :")

E = input("Input eye color :")

G = input("Input gender :")



INFOINPUT(F,S,L,H,E,G)

