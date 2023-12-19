class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)
        self.reviews = []
      
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(clses):
        return clses.customers

    def num_reviews(self):
        return len(self.reviews)

    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]

    def restaurants(self):
        return list(set(review.restaurant for review in self.reviews))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        restaurant.reviews.append(new_review)


customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

print(customer1.num_reviews())
print(customer1.full_name()) 
print(customer2.full_name()) 