import os

os.chdir(r"C:\Users\HI\OneDrive\Desktop\estoreproject\estore")
import sys
sys.path.append(r"C:\Users\HI\OneDrive\Desktop\estoreproject\estore")
import mysql.connector
import pandas as pd
import json
import shoplib as op

v = op.Buyings()
summary = {}
customer = 1
today_sales = 0
flow = 'y'
while flow == 'y':
    if input('Welcome to online store\n1. Book your products\n2. Cancel your products\nYour choice: ') == '1':
        info = v.Buy()
        summary[customer] = info
        customer += 1
        print("Thank you for shopping")
        flow = input('Do you want to continue[y/n]:').lower()
        if flow == "n":
            break
    else:
        v.cancel()
    
        print("Thank you for shopping")
        flow = input('Do you want to continue[y/n]:').lower()
        if flow == "n":
            break

for key in summary.keys():
    today_sales += summary[key]['num items']
with open("data.json", "w") as f:
    json.dump(summary, f)
with open("data.json") as f:
    data = pd.read_json(f, orient='index')
    df = pd.DataFrame(data)
    print(df.head())
    print("Today sales: " + str(today_sales))
    print("Number of ac sold out today {}".format(df['ac'].sum(axis=0)))
    print("Number of coolers sold out today {}".format(df['cooler'].sum(axis=0)))
    print("Number of fans sold out today {}".format(df['fan'].sum(axis=0)))
    print("Number of heaters sold out today {}".format(df['heater'].sum(axis=0)))
