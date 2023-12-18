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
        return clses.all

    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant
    
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

print(restaurant1.reviews())
print(restaurant2.customers())
    
    



