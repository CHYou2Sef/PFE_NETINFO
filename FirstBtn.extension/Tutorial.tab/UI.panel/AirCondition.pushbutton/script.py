# -*- coding: utf-8 -*-
# # ¹¹ €
__name__ = "Choice Air Condition"
__title__ = "Air Condition UI"
import csv

import os
os.path.exists

import sqlite3
import sqlalchemy

from itertools import count

from rpw.utils.dotnet import Enum
from rpw.ui.forms.resources import *

from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox,Separator, Button, CheckBox)

import sys
sys.path.append(r"C:\Program Files\IronPython 2.7\lib")

#Price = os.environ["MY_DATA"]
#Price  = sys.argv[1]

f = open("C:\\Users\YOUSSEF\PFE\TotalPower.txt", "r")
Tpower = "Totale Power : " + f.read() +" W"
f.close()
#########################################

f = open("C:\\Users\\YOUSSEF\\PFE\\TotalPower.txt", "r")
TPower = float(f.read())
f.close()

print()

t = []
marg = 50


i = 0

if __name__ == 'Choice Air Condition':
    components = [
                    Label("*** Total Power Value:"),
                    #La valeur de puissance de chauffage qu'on a calculer
                    Label("The heating power value that we have calculated :"),
                    Label(" {:.3f} W".format(TPower)),
                    Separator(),
                    TextBox("Write_your_prefer_marge", Text = "50"),
                    # CheckBox('checkbox1', 'Check this:'),
                    Separator(),
                    # Donc on a choisi le climatiseur dont
                    Label("*So we chose the air conditioner whose,"
                    "the heating power is equal or lower by {} to the value calculated by the heat balance..".format(marg)),
                    Button('OK'), Button('Annuler')]

    form = FlexForm('Thermal balance', components)
    form.show()




# open the CSV file
with open('C:\\Users\\YOUSSEF\\PFE\\Air_condition_dataset.csv') as csv_file:
    # create a CSV reader object
    csv_reader = csv.reader(csv_file)
    # skip the header row
    header = next(csv_reader)

    # specify the consumption value you want to filter
    target_consumption = TPower

    # initialize a list to store the rows with the target consumption value
    target_rows = []

    # loop through each row in the CSV file
    for row in csv_reader:
        # extract the numerical value from the "Power_Consumption" column
        consumption_str = row[header.index("Power_Consumption")]
        x = consumption_str.split()
        consumption = float(x[0])
        # check if the extracted consumption value matches the target consumption
        if abs(consumption - target_consumption) <= marg:
            target_rows.append(row)

    # find the minimum price value among the rows with the target consumption
    min_price = min(float(row[header.index("Price")]) for row in target_rows)

    # find the rows that have the minimum price value
    min_price_rows = [row for row in target_rows if float(row[header.index("Price")]) == min_price]

    ii = 0
    # loop through each row with the minimum price value
    for row in min_price_rows:
        # print("Meilleur choix :")
        for i, value in enumerate(row):
            if header[i] == "Price":
                value = float(value) * 0.0372502
                t[ii] = "{} : {:.3f} DT".format(header[i], value)
                ii = ii + 1
            else:
                t[ii] = "{} : {}".format(header[i], value)
                ii = ii + 1


components2 =  [ ComboBox("combobox1", {"Data :":
                                   t
                               }),]
form2 = FlexForm('Thermal balance', components2)
form2.show()
print(form.values , form2.values)