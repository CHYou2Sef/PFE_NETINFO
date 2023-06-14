# # # -*- coding: utf-8 -*-
#
# __name__ = "Air Condition Choice"
# __title__ = "Best Air Condition"
#
# import os
# os.path.exists
#
#
# import csv
#
#
# with open('C:\Users\YOUSSEF\PFE\Air_condition_dataset.csv', 'rb') as csvfile:
#     # Create a CSV reader
#     df = csv.reader(csvfile, delimiter=',')
# csvfile.close()
# # Read the CSV file into a Pandas dataframe
# #df = csv.reader("C:\Users\YOUSSEF\PFE\Air_condition_dataset.csv")
# #df = pd.read_excel("Air_condition_dataset.xlsx", encoding="ISO-8859-1")
#
# # Get user input for power consumption value
# #X = float(input("Enter the power consumption value: "))
# #result = df["Power_Consumption"]   #.astype(float)
# #long = len(result)
# #print("La totle de ligne est {} lignes ".format(long))
# #T = []
# i=0
# j=0
# #with open("C:\\Users\YOUSSEF\PFE\TotalPower.txt","r") as f:
# #    TPower = f.read()
#
# f = open("C:\\Users\\YOUSSEF\\PFE\\TotalPower.txt", "r")
# TPower = float(f.read())
# f.close()
#
# #print(TPower)
#
# name = df["Brand_name"]
# result = df["Power_Consumption"]
# price  = df["Price"]
#
# long = len(result)
# print("Le nombre total de lignes est {}".format(long))
#
# T = []
# p = []
#
# for i in range(long):
#     x = result[i].split()
#     y = price[i].astype(float) * 0.0372502
#     z = name[i]
#     num1  = x[0]
#    # print(num1)
#     num2  = float(num1)
#     if num2 <= TPower and num2 >= TPower-50:
#         T.append(z)
#         T.append("{:.3f}".format(num2))
#         T.append(y)
#         p.append(y)
#
# Mprice = min(p)
# print("La valeur de puissance de chaffage qu'on a calculer: ",TPower," W")
# #print("Les valeurs de puissances de chauffages sont:", T)
# print("La liste des climatiseurs où les puissances de chauffages sont égeux à la valeur calculer :", T)
# print("Le meilleur choix selon le prix est : {:.3f} DT".format(Mprice))
# print("Donc on a choisi le climatisseur ")
#
# # ¹¹ €
#
# #filtered_df = df[df["Power_Consumption"].apply(lambda x: float(x.split()[0])) <= 1900.0]
# #T = filtered_df["Power_Consumption"].apply(lambda x: float(x.split()[0])).tolist()
#
# #print("Les valeurs de T sont:", T)
#
# #print(df["Power_Consumption"])
# #print(result)
#


import csv

f = open("C:\\Users\\YOUSSEF\\PFE\\TotalPower.txt", "r")
TPower = float(f.read())
f.close()

print("* La valeur de puissance de chaffage qu'on a calculer : {:.3f} W".format(TPower))

marg = 50

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
        # na5ou les colonnes "Power_Consumption"
        consumption_str = row[header.index("Power_Consumption")]
        # consumption = float(consumption_str.replace(" W", "")) or float(consumption_str.replace(" kWh", ""))
        # na5ou ex: 123 w  ne7i l W
        x = consumption_str.split()
        consumption = float(x[0])
        # check if the extracted consumption value matches the target consumption
        if abs(consumption - target_consumption) <= marg:
            target_rows.append(row)


    if len(target_rows) != 0 :

        # find the minimum price value among the rows with the target consumption
        min_price = min(float(row[header.index("Price")]) for row in target_rows)

        # min_price.astype(float) * 0.0372502
        # find the rows that have the minimum price value
        min_price_rows = [row for row in target_rows if float(row[header.index("Price")]) == min_price]

        print(
            "* Donc on a choisi le climatisseur dont la puissance de chauffage est égale ou inferieur par {} au valeur calculer par le bilan thermique ..".format(
                marg))
        # loop through each row with the minimum price value
        for row in min_price_rows:
            # get the consumption value for this row
            # consumption = float(row[header.index("Power_Consumption")])
            # print the rows within 50 units of consumption of the minimum value

            print("Meilleur choix :")
            for i, value in enumerate(row):
                if header[i] == "Price":
                    value = float(value) * 0.0372502
                    print("{} : {:.3f} DT".format(header[i], value))
                else:
                    print("{} : {} ".format(header[i], value))
    else:
        print ("* Le valeur calculer de puissance de consommation {:.3f} W n'existe pas dans le tableau des chauffages.".format(TPower))