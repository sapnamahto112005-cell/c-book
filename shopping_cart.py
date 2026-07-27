

import random 

total = 0 

with open("shopping_list.txt","a") as file:

        file.write(f"\n--------------------------------------------------------------------------\n")  
        file.write(f"WELCOME TO OUR FAMILY MART !!! YOU WILL BE  ANY PROBLEM PLEASE CONTACT OUR STAFF MEMBER\n")
        file.write(f"--------------------------------------------------------------------------\n")
          
        while(True):
          groceries = input("select your item: ")
          
          if groceries.lower() == "done":
              break
          
          amount = random.randint(20,100)

          if total + amount > 500:
               print("limit reached! shopping stopped!!!!")
               break 
          
          print(f"add to cart: {groceries}")
          print(f"price: {amount}")

          file.write(f"groceries: {groceries} -> price: {amount}\n")

          total += amount

        file.write(f"total amount: {total}\n")

print(f"total amount: {total}")











