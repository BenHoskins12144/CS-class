def NAME(F,S,L):
    if P==("FSL"):
        print(f"{F}, {S}, {L}")
    if P==("SLF"):
        print(f"{S}, {L}, {F}")
    if P==("FLS"):
        print(f"{F}, {L}, {S}")
    if P==("SFL"):
        print(f"{S}, {F}, {L}")
    if P==("LFS"):
        print(f"{L}, {F}, {S}")
    if P==("LSF"):
        print(f"{L}, {S}, {F}")

P = input("input order :")

F = input("input first name :")

S = input("input middle name :")

L = input("last name :")

NAME(F,S,L)










