class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name
    
restaurant1 = Restaurant("Cheka")
restaurant2 = Restaurant("Goodies")

print(restaurant1.reviews())
print(restaurant2.customers())