from customer import Customer
from review import Review
from customer import customer1, customer2

class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.restaurants.append(self)
        self.reviews = []

    def name(self):
        return self.name

    @classmethod
    def all(clses):
        return clses.restaurants

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list(set(review.get_customer() for review in self.reviews))

    def average_star_rating(self):
        if not self.reviews:
            return 0

        total_ratings = sum(review.get_rating() for review in self.reviews)
        average_rating = total_ratings / len(self.reviews)
        return average_rating


# Test
restaurant1 = Restaurant("Cheka")
restaurant2 = Restaurant("Bistro")

# Test
print(restaurant1.name())  

# Test adding reviews
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)

# Test average rating
print(restaurant1.average_star_rating())
