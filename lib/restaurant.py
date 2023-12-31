class Restaurant:
    _all_restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant._all_restaurants.append(self)
        self._reviews = []

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all_restaurants

    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set([review.customer() for review in self._reviews]))

    def average_star_rating(self):
        if not self._reviews:
            return 0
        total_ratings = sum([review.rating for review in self._reviews])
        return total_ratings / len(self._reviews)
