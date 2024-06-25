
class Vehicle:
    def __init__(self, vehicle_make, vehicle_value):
        self.vehicle_make = vehicle_make
        self.vehicle_value = vehicle_value
        #assigning the 'self' value for the vehicle make and value ^^


    def display_info(self):
        print(f'   Vehicle Make: {self.vehicle_make}')
        print(f'   Value: {self.vehicle_value}') #prints the make and the model in proper format


class Car(Vehicle):
    def __init__(self, car_make, car_value, car_model, car_year):
        super().__init__(car_make, car_value)  #the super function used here makes sure that the init method of the vehicle class is applied to 'car' and 'truck'
        self.car_model = car_model
        self.car_year = car_year

    def display_info(self):
        print(f'   Description: {self.car_year} {self.vehicle_make} {self.car_model}')  #could use vehicle.make here since the super function was called earlier
        print(f'   Value: {self.vehicle_value}')  #super function used earlier - dont need to call car_value specifically

class Truck(Vehicle):
    def __init__(self, truck_make, truck_value, truck_model, truck_year, is_allwd):
        super().__init__(truck_make, truck_value)  #used the same principle of calling back the super funcion so that truck make and value are apllied from vehicle make and value.
        self.truck_model = truck_model
        self.truck_year = truck_year
        self.is_allwd = is_allwd

    def display_info(self):
        print(f'   Description: {self.truck_year} {self.vehicle_make} {self.truck_model}')
        print(f'   Value: {self.vehicle_value}')
        print(f'   All Wheel Drive: {self.is_allwd}')
        #displaying the info for specifically the truck class^ awd is allowed on a truck, but not car



def display_list(my_collection):
    for index, vehicle in enumerate(my_collection):  #this line starts a 'for loop' that will go through the list. 'enumerate' will assign an index value & vehicle obj from list
        print(f'Vehicle {index + 1} Information:') #we don't start countin at 0, so index+1 will start at 1
        vehicle.display_info()
        print() #for readability, will put a separate, blank line in

if __name__ == "__main__":

    my_collection = [] #adding an empty collection

    user_string = input()

    while user_string != 'done':  #checks to make sure the user isn't done with the program
        data = user_string.split()
        if data[0] == 'vehicle':  #if the user input is vehicle, it will run this
            make, value = data[1], data[2]
            my_collection.append(Vehicle(make, value))
        elif data[0] == 'car':  #if the user input is car, it will run this
            make, value, model, year = data[1], data[2], data[3], data[4]
            my_collection.append(Car(make, value, model, year))
        elif data[0] == 'truck':  #if the user input is truck, it will run this
            make, value, model, year, all_wheel_drive = data[1], data[2], data[3], data[4], data[5]
            my_collection.append(Truck(make, value, model, year, all_wheel_drive == 'true')) #awd is true if the model is a truck
        user_string = input()



    display_list(my_collection)
