class Restaurant:

    # This is the constructor method -> it gets called by default
    # whenever one creates a new object of this class
    #
    # In this version, the user must specify the name and cuisine, but the rating and price
    # are assigned default values.
    #
    # Note that name, cuisine (i.e. the ones that the user MUST provide,
    # MUST come before rating,price in the
    # function parameter list!!!
    #
    # In my opinion, it is best to have
    # ALL parameters have default values, so that the user can choose
    # to provide them or not.
    #
    # e.g
    #
    # def __init__(self, name="none", cuisine="none", rating=-1, price="none"):
    #       self.name = name
    #       self.rating = rating
    #       self.price = price
    #       self.cuisine = cuisine
    #
    # In this way, any of the following statements are valid:
    #  moes = Restaurant()
    #  moes = Restaurant("Moe's")
    #  moes = Restaurant("Moe's", "Mexican")
    #  moes = Restaurant("Moe's", "Mexican", 7)
    #  moes = Restaurant("Moe's", "Mexican", 7, "***")



    def __init__(self, name, cuisine, rating=-1, price="none"):
        """
        :param name:  Name of the restaurant (string)
        :param rating: Rating (1-10, int)
        :param price: Price (*-*****, string)
        :param cuisine: Cuisine Type (string)
        """
        self.name = name
        self.rating = rating
        self.price = price
        self.cuisine = cuisine

    # Define a print_info method, which summarizes object information
    def __str__(self):
        return (f'Restaurant Information:\n'
                f'      Name = {self.name}\n'
                f'      Rating = {self.rating}\n'
                f'      Price = {self.price}\n'
                f'      Cuisine Type = {self.cuisine}')

    # Define setter and getter methods for each internal variable of the class
    def set_name(self, user_name):
        self.name = user_name

    def get_name(self):
        return self.name

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


if __name__ == "__main__":

    #help(Restaurant)

    my_name = input("Enter the name of the restaurant:")
    my_rating = int(input("Enter the rating of the restaurant:"))
    my_price = input("Enter the price of the restaurant:")
    my_cuisine = input("Enter the cuisine type of the restaurant:")

    # Create a new Restaurant object ... this will call the __init__ constructor method
    # of the Restaurant class
    moes = Restaurant(my_name, my_cuisine, my_rating, my_price)

    # If we wanted to, we could still use setter methods to set the other values
    # moes.set_rating(6)
    # moes.set_price("**")

    # Call the print_info method, to see initial values
    print(moes)

    panera = Restaurant("Panera", "Soups and Sandwiches", 4, "*****")
    fiveguys = Restaurant("Five Guys", "Burgers", 10, "****")

    print(panera)
    print(fiveguys)
