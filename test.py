from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

if __name__ == '__main__':
    # Test 

    # Create customers
    customer1 = Customer("Mary", "Wambui")
    customer2 = Customer("John", "Maina")

    # Create restaurants
    restaurant1 = Restaurant("Cheka")
    restaurant2 = Restaurant("Burger King")

    # Add reviews
    customer1.add_review(restaurant1, 5)
    customer1.add_review(restaurant2, 4)
    customer2.add_review(restaurant1, 4)

    # Print customer output
    print(customer1.full_name())  
    print(customer1.num_reviews()) 

    # Print restaurant information
    print(Restaurant.all())  
    print(restaurant1.customers())  
    print(restaurant1.average_star_rating()) 

    # Print review information
    print(Review.all())
