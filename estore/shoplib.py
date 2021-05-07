import random
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
     password="Vijju@123",
    database="eapp"
)
mycursor = mydb.cursor()

#for x in mycursor:
     #print(x)

class Buyings:
     def __init__(self):
          self.Buyings = {}
          self.available_items = 500

     def Buy(self):
          info = dict()
          name = input("enter your username:")
          print("Welcome {}".format(name))
          info['name'] = name
          region = input("Enter region: ")
          info['region'] = region
          num_items = int(input('enter number of items: '))
          self.available_items -= num_items
          info['num items'] = num_items
          products = ['ac', 'cooler', 'fan', 'heater']
          product_sales = [0, 0, 0, 0]
          prices = [50000, 20000, 1000, 7000]
          price = 0
          c = 1
          for i in products:
               print(str(c) + ". " + i)
               c += 1
          for i in range(num_items):
               t = int(input("Choose a product: "))
               product_sales[t - 1] += 1
               price += prices[t - 1]
          print("Total price: " + str(price))
          if price > 10000:
               price -= (price * 20 / 100)
               print('Discount:\nYou have saved 20%')
               print("Final price: " + str(price))
          if price < 5000:
               print("you have won a gift hamper")
          for i in range(len(products)):
               info[products[i]] = product_sales[i]
               info['price'] = price
               self.Buyings[name] = info
          print(self.Buyings)
          final_tuple = (name,products[t],price,region,num_items)
          sql = "INSERT INTO customer_table (name, product,price,region,quantity) VALUES (%s,%s,%s,%s,%s)"
        
          mycursor.execute(sql,final_tuple)
        
          mydb.commit()
          return info
          
         

     def cancel(self):
        p = input("enter your username:")
        mycursor.execute("select name from customer_table")
        names = mycursor.fetchall()
        print(names)
        if (p,) in names:
            A = random.randrange(5000, 6000)
            print(A)
            t = int(input("enter user OTP:"))
            if A == t:
                query = "delete from customer_table where name = '%s'"%(p)
                mycursor.execute(query)
                mydb.commit()
                print("items cancelled")
                #self.available_items += self.Buyings[p]['num items']
                #del (self.Buyings[p])
                
            else:
                print('Wrong OTP. Please try again')
        else:
            print('No user found...!')
       # print(self.Buyings)
        #print(self.available_items)
