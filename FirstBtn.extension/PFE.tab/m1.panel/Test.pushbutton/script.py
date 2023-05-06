# # -*- coding: utf-8 -*-

__name__ = "Air Condition Choice"
__title__ = "Best Air Condition"

import os
os.path.exists

import pandas as pd
import csv


with open('C:\Users\YOUSSEF\PFE\Air_condition_dataset.csv', 'rb') as csvfile:
    # Create a CSV reader
    df = csv.reader(csvfile, delimiter=',')
csvfile.close()
# Read the CSV file into a Pandas dataframe
#df = csv.reader("C:\Users\YOUSSEF\PFE\Air_condition_dataset.csv")
#df = pd.read_excel("Air_condition_dataset.xlsx", encoding="ISO-8859-1")

# Get user input for power consumption value
#X = float(input("Enter the power consumption value: "))
#result = df["Power_Consumption"]   #.astype(float)
#long = len(result)
#print("La totle de ligne est {} lignes ".format(long))
#T = []
i=0
j=0
#with open("C:\\Users\YOUSSEF\PFE\TotalPower.txt","r") as f:
#    TPower = f.read()

f = open("C:\\Users\\YOUSSEF\\PFE\\TotalPower.txt", "r")
TPower = float(f.read())
f.close()

#print(TPower)

name = df["Brand_name"]
result = df["Power_Consumption"]
price  = df["Price"]

long = len(result)
print("Le nombre total de lignes est {}".format(long))

T = []
p = []

for i in range(long):
    x = result[i].split()
    y = price[i].astype(float) * 0.0372502
    z = name[i]
    num1  = x[0]
   # print(num1)
    num2  = float(num1)
    if num2 <= TPower and num2 >= TPower-50:
        T.append(z)
        T.append("{:.3f}".format(num2))
        T.append(y)
        p.append(y)

Mprice = min(p)
print("La valeur de puissance de chaffage qu'on a calculer: ",TPower," W")
#print("Les valeurs de puissances de chauffages sont:", T)
print("La liste des climatiseurs où les puissances de chauffages sont égeux à la valeur calculer :", T)
print("Le meilleur choix selon le prix est : {:.3f} DT".format(Mprice))
print("Donc on a choisi le climatisseur ")

# ¹¹ €

#filtered_df = df[df["Power_Consumption"].apply(lambda x: float(x.split()[0])) <= 1900.0]
#T = filtered_df["Power_Consumption"].apply(lambda x: float(x.split()[0])).tolist()

#print("Les valeurs de T sont:", T)

#print(df["Power_Consumption"])
#print(result)

