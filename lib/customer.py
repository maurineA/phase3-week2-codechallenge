from lib.review import Review

class Customer:
    _all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer._all_customers.append(self)
        self._reviews = []

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        self._given_name = given_name

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        self._family_name = family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls._all_customers

    def restaurants(self):
        return list(set([review.restaurant for review in self._reviews]))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)  # Append the review to the _reviews attribute
        return review

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls._all_customers if customer.given_name == given_name]
