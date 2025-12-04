class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, address, name):
        self.address = address
        super().__init__(name)
        
    def place_order(self, item):
        return DeliveryOrder(self.name, item)
    
class Driver(Person):
    def __init__(self, vehicle, name):
        self.vehicle = vehicle
        super().__init__(name)

    def deliver(self, order):
        order.status = "delivered"
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}")

class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status
        self.driver = ""

    def assign_driver(self, driver):
        self.driver = driver

    def summary(self):
        if self.status == "preparing":
            return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver}"
        else:
            return f"Order for {self.item} -> {self.status}"


c1 = Customer("A1", "Alice")
c2 = Customer("A2", "Bob")
d1 = Driver("motorcycle", "David")
order1 = c1.place_order("Laptop")
order2 = c2.place_order("Headphones")
order1.assign_driver(d1.name)
order2.assign_driver(d1.name)
c1.introduce()
c2.introduce()
d1.introduce()
print()
print(order1.summary())
print()
print(order2.summary())
print()
d1.deliver(order1)
d1.deliver(order2)
print()
print("Final Status:")
print(order1.summary())
print(order2.summary())
