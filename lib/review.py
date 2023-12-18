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
    
    



