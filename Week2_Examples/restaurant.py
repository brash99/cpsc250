class Restaurant:
    # This is the constructor method -> it gets called by default
    # whenever one creates a new object of this class
    def __init__(self):
        print("Here I am in the constructor method of the Restaurant class")
        self.myname = "none"
        self.rating = -1
        self.price = "none"
        self.cuisine = "none"

    # Define setter and getter methods for each internal variable of the class
    def set_name(self, user_name):
        self.myname = user_name

    def get_name(self):
        return self.myname

    def set_rating(self, user_rating):
        self.rating = user_rating

    def get_rating(self):
        return self.rating

    def set_price(self, user_price):
        self.price = user_price

    def get_price(self):
        return self.price

    def set_cuisine(self, user_cuisine):
        self.cuisine = user_cuisine

    def get_cuisine(self):
        return self.cuisine

    # Define a print_info method, which summarizes object information
    def print_info(self):
        print(f'Restaurant Information:')
        print(f'      Name = {self.myname}')
        print(f'      Rating = {self.rating}')
        print(f'      Price = {self.price}')
        print(f'      Cuisine Type = {self.cuisine}')


if __name__ == "__main__":

    my_name = input()
    my_rating = int(input())
    my_price = input()
    my_cuisine = input()

    # Create a new Restaurant object ... this will call the __init__ constructor method
    # of the Restaurant class
    moes = Restaurant()

    # Call the print_info method, to see default values
    moes.print_info()

    # Set values of name, rating, price, and cuisine, based on user input
    moes.set_name(my_name)
    moes.set_rating(my_rating)
    moes.set_price(my_price)
    moes.set_cuisine(my_cuisine)

    # Call the print_info method again, to see updated values
    moes.print_info()
