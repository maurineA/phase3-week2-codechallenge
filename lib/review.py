class Review:
    _all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review._all_reviews.append(self)
        restaurant._reviews.append(self)  
        customer._reviews.append(self)   

    @property
    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls._all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant
