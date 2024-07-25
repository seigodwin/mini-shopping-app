import csv
import os
import re

def main():
    
    print("......Welcome to our Mall.....",)
    name = input("Enter your name: ").strip().title()
    email = get_email()
    try:
      balance = float(input("Enter the amount you want to deposit: "))
    except ValueError: print("Invalid amount! Enter a numer!")  
    m1 = Mall(name, email , balance )

    while True:
      try: 
        print("Enter 1 to  Sign up!" )
        option = int(input("Enter 2 to login if you already have an acoount"))
        if option == 1:
             agree = m1.sign_up()
             if agree:
                print(f"Welcome {name} !")
                print(f"Your balance is Ghc{balance}") 
                m1.runApp()
             else: print("Sign up was not successful!")   

        elif option ==2:
            agree = m1.login()
            print(f"Welcome {name} !")
            print(f"Your balance is Ghc{balance}")
            if agree :     
                m1.runApp()
            else: print("Log in failed!")    
        else: print("Choose between 1 or 2!") 
      except ValueError: print("Invalid input! Enter 1 or 2")     
   
class Mall:
    
    cost = 2
    inventory = {
        "APPLE": 10,
        "BANANA": 15,
        "RICE": 20,
        "YAM": 22
    }

    def __init__(self, name: str, email:str, balance: float):
        self.user_email = email
        self.user_name = name
        self.userBalance = balance
         

    def buyProduct(self, product: str, quantity: int):
        product_upper = product.upper()
        
        if product_upper in self.inventory:
            try:
                option = int(input(f"1 quantity of {product_upper} costs Ghc{self.cost}... Enter 1 to Confirm or 2 to Cancel: "))
                if option == 1:
                    if self.inventory[product_upper] >= quantity:
                        if quantity * self.cost <= self.userBalance:
                            self.inventory[product_upper] -= quantity
                            self.userBalance -= self.cost * quantity
                            print(f"You bought {quantity} quantity of {product_upper}")
                            print(f"Your new balance is Ghc{self.userBalance}")
                        else:
                            print(f"Your balance Ghc{self.userBalance} is not enough to buy {quantity} of {product_upper}s")
                    else:
                        print(f"There are only {self.inventory[product_upper]} of {product_upper} available")
                elif option == 2:
                    print("Purchase cancel successful!")
                else:
                    print("Wrong choice! Enter 1 or 2")
            except ValueError:
                print("Invalid input! Enter 1 or 2")
        else:
            print(f"The product '{product_upper}' is not in the inventory")

    def printAllProducts(self):
        print("Product - Quantity")
        for key, data in self.inventory.items():
            print(f"{key}  -   {data}")

    def addProduct(self, product: str, quantity: int):
        product_upper = product.upper()
        if product_upper in self.inventory:
            self.inventory[product_upper] += quantity
        else:
            self.inventory[product_upper] = quantity
        print(f"You have added {quantity} of {product_upper}s")

    def removeProduct(self, product: str, quantity: int):
        product_upper = product.upper()
        if product_upper in self.inventory:
            if self.inventory[product_upper] >= quantity:
                self.inventory[product_upper] -= quantity
            elif self.inventory[product_upper] == quantity:
                del self.inventory[product_upper]
            print(f"You deleted {quantity} {product_upper}s. Current quantity: {self.inventory.get(product_upper, 0)}")
        else:
            print(f"{product_upper} is absent in the inventory")

    def printMenu(self):
        print("........Menu.......")
        print("1. View all products")
        print("2. Buy a product")
        print("3. Add a product")
        print("4. Remove a product")
        print("5. Exit the app")

    def sign_up(self):
      self.file_exists = os.path.isfile("people.csv")
      self.sign_up_ = False
      self.name = self.user_name
      self.email = self.user_email

      if not self.name or  not self.email:
        print("Name or Email cannot be empty: ")
        return self.sign_up_

      with open("people.csv", "a") as file:
        writer = csv.DictWriter(file , fieldnames = ["name" , "email"])
        if not self.file_exists:
              writer.writeheader()
        writer.writerow({"name": self.name, "email":self.email})  
        self.sign_up_ = True
      return self.sign_up_
    
    def login(self):
      self.name = self.user_name
      self.email = self.user_email

      found = False  
      with open("people.csv", newline='') as file: 
          reader = csv.DictReader(file) 
          for row in reader: 
              if row["name"] == self.name and row["email"] == self.email: 
                  print("Login Successful!")
                  found = True
                  break 

      if not found:
        while True:
            try:
                choice = int(input("Log in failed! Enter 1 to sign up or 2 to exit the app: ")) 
                if choice == 1: 
                    found = self.sign_up()
                    break 
                elif choice == 2: 
                    print("Thanks for shopping with us!")
                    exit()
                else: 
                    print("Choose between 1 and 2")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 2.")
    
      return found
    
    def runApp(self):

        while True:
            self.printMenu()
            try:
                choice = int(input("Please choose an option from the list above: "))
                if choice == 5:
                    print("Thanks for shopping with us!")
                    exit()
                elif choice == 1:
                    self.printAllProducts()
                elif choice == 2:
                    product = input("Enter product name: ")
                    quantity = int(input("Enter quantity: "))
                    self.buyProduct(product, quantity)
                elif choice == 3:
                    product = input("Enter product name: ")
                    quantity = int(input("Enter quantity: "))
                    self.addProduct(product, quantity)
                elif choice == 4:
                    product = input("Enter product name: ")
                    quantity = int(input("Enter quantity: "))
                    self.removeProduct(product, quantity)
                else:
                    print("Wrong choice! Please choose an integer from 1 - 5")
            except ValueError:
                print("Invalid input! Please enter an integer from 1 - 5")

def get_email():
    while True:
       U_email = input("Enter your email ")
       if re.search("[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|edu)", U_email):
           email = U_email
           return email 
       else: print("Invalid email!")

main()                    
