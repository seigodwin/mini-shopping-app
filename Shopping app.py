class Mall:
    cost = 2
    inventory = {
        "APPLE": 10,
        "BANANA": 15,
        "RICE": 20,
        "YAM": 22
    }

    def __init__(self, name: str, balance: float):
        self.name = name
        self.userBalance = balance
        print(f"Welcome {self.name}!")
        print(f"You have Ghc{self.userBalance} in your account!")

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

    def runApp(self):

        while True:
            self.printMenu()
            try:
                choice = int(input("Please choose an option from the list above: "))
                if choice == 5:
                    print("Thanks for shopping with us!")
                    break
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
print("....Create an account....")
name = input("Enter your name: ")
balance = float(input("Enter the amount you want to deposit: "))
m1 = Mall(name, balance) 
m1.runApp()
