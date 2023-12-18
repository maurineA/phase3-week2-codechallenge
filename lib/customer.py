class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)
      
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(clses):
        return clses.all


customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

print(customer1.full_name()) 
print(customer2.full_name()) 