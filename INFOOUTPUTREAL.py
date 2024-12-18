



class StudentDB:
    def __init__(self):
         A = 1
         
        






class Student:
    def __init__(self):
        self.firstname = None
        self.middlename = None
        self.lastname = None
        self.hight = None
        self.eyecolor = None
        self.gender = None

    def print(self):
            print(f"{self.firstname} {self.middlename} {self.lastname} {self.hight} {self.eyecolor} {self.gender} {self.EmailLower}")

    def guessEmail(self):
         self.Email = self.firstname[0] + self.lastname + "@fulton-school.org"
         self.EmailLower =self.Email.lower()

        
    








def getStudentData(studentNumber):
    Z = studentNumber
    Z = float(Z)
    I = 6*Z+2
    I1 = I+5
    I = int(I)
    I1= int(I1)
    
    with open('myfile.csv', 'r') as file:
    
        Lines = file.readlines()
        
        print(Lines[I:I1])
        
        firstname = Lines[I]
        
        middlename = Lines[I+1]
        
        lastname = Lines[I+2]
        
        hight = Lines[I+3]
        
        eyecolor = Lines[I+4]

        gender = Lines[I+5]
        
        
        
        firstnamesplit = firstname.split("=")
        firstnamesplit = firstnamesplit[1].strip()
        

        middlenamesplit = middlename.split("=")
        middlenamesplit = middlenamesplit[1].strip()

        lastnamesplit = lastname.split("=")
        lastnamesplit = lastnamesplit[1].strip()

        hightsplit = hight.split("=")
        hightsplit = hightsplit[1].strip()

        eyecolorsplit = eyecolor.split("=")
        eyecolorsplit = eyecolorsplit[1].strip()

        gendersplit = gender.split("=")
        gendersplit = gendersplit[1].strip()

        # print(f"{firstnamesplit} {middlenamesplit} {lastnamesplit} {hightsplit} {eyecolorsplit} {gendersplit}")

        S = Student()
        S.firstname = firstnamesplit
        S.middlename = middlenamesplit
        S.lastname = lastnamesplit
        S.hight = hightsplit
        S.eyecolor = eyecolorsplit
        S.gender = gendersplit 
        S.guessEmail()

        

        S.print()



getStudentData("0")





