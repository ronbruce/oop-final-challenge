class Person:
    def __init__(self, name, favorite_drink, wallet):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip_amount = 0  # Initialize tip amount to 0

    def my_order(self, order_type, tip_amount=0):
        order = Order(self, order_type, tip_amount)
        return order

class Order:
    def __init__(self, person, order_type, tip_amount=0):
        self.person = person
        self.type = order_type
        self.tip_amount = tip_amount
        self.price = self.calculate_price()

    def calculate_price(self):
        # Decide on the price based on the order type
        if self.type == "Coffee":
            return 2.5
        elif self.type == "Tea":
            return 3.0
        elif self.type == "Milk":
            return 1.5
        else:
            return 0.0  # Default price for unknown order types

    def to_string(self):
        return f"{self.person.name} orders: {self.type} with tip: ${self.tip_amount}"

class CoffeeBar:
    def __init__(self, barista):
        self.orders_list = []
        self.receipts = []  # New property to track receipts
        self.tip_jar = 0  # New property to track tips
        self.barista = barista
        self.register = 0

    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        for order in self.orders_list:
            total_cost = order.price + order.tip_amount

            if total_cost <= order.person.wallet:
                order.person.wallet -= total_cost
                self.register += order.price  # Add the order amount to the register
                self.tip_jar += order.tip_amount  # Add the tip amount to the tip jar

                # Add the order to the receipts list
                self.receipts.append(order)

                # Print the processed order with wallet balance and tip
                print(f"{self.barista.name} {order.to_string()}. Wallet balance: ${order.person.wallet}. Tip Jar: ${self.tip_jar}")
            else:
                print(f"Insufficient funds for {order.person.name} to place the order.")

        # Clear the processed orders from the orders list
        self.orders_list = []

    def cash_out(self):
        print(f"Total amount in the register: ${self.register}")

    def view_receipts(self):
        print("\nReceipts:")
        for receipt in self.receipts:
            print(f"{self.barista.name} {receipt.to_string()}")

    def cash_out_tip_jar(self):
        # Add the tip jar to Kevin's wallet
        self.barista.wallet += self.tip_jar
        print(f"{self.barista.name}'s wallet after cashing out tip jar: ${self.barista.wallet}")
        self.tip_jar = 0  # Reset the tip jar after cashing out

class Barista(Person):
    def __init__(self, name, greeting):
        super().__init__(name, "Barista", 0)  # Barista has a wallet, initialized with 0
        self.greeting = greeting

# Example usage:
Amy = Person("Amy", "Coffee", 10.0)
Bob = Person("Bob", "Tea", 5.0)
Cat = Person("Cat", "Milk", 8.0)
Larrys_Coffee = CoffeeBar(Barista("Kevin", "Hey dude!"))

order1 = Amy.my_order("Coffee", 2.0)  # Amy tips $2
order2 = Bob.my_order("Tea", 1.0)  # Bob tips $1
order3 = Cat.my_order("Milk", 1.5)  # Cat tips $1.5

Larrys_Coffee.place_order(order1)
Larrys_Coffee.place_order(order2)
Larrys_Coffee.place_order(order3)

Larrys_Coffee.process_orders()
Larrys_Coffee.cash_out()
Larrys_Coffee.view_receipts()
Larrys_Coffee.cash_out_tip_jar()