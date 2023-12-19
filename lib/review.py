from customer import customer1, customer2
from restaurant import restaurant1

class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)

    def rating(self):
        return self.rating
    
    @classmethod
    def all(clses):
        return clses.reviews

    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
# review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer2, restaurant2, 5)

# print(restaurant1.reviews())
# print(restaurant2.customers())
    
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Cheka")

review1 = Review(customer1, restaurant1, 4)
print(review1.get_rating())
    
    



