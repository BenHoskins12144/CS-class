import csv
import numpy as np

A=input("number for A")

A=float(A)
G=A*5+A+1-5
H=A*5+A+1
G=int(G)
H=int(H)

with open('myfile.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for i in range(G,H):
        for i in csv_reader:
            print(i)
            
            
