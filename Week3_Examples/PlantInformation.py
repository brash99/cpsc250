# import PlantFlower ... this will work, but then we would have to type
#                          PlantFlower.Plant and PlantFlower.Flower
#                           (Interpreter:  look for a file called PlantFlower.py)
#
# import PlantFlower as pf ... this will work, but then we would have to type
#                              pf.Plant and pf.Flower
#
# from PlantFlower import * ... this will work, but is a bit dangerous because
#                                it imports everything from the module
#                               and could overwrite other functions or variables
#                               with the same name
# from PlantFlower import Plant, Flower ... this is the best way to import
#                                          because it only imports the classes
#                                          we need
# from file.py import my_function ... this is how to import a function from a file

from PlantFlower import Plant, Flower

def print_list(garden):
    for i in range(len(garden)):
        print(f'Plant {i + 1} Information:')
        garden[i].print_info()
        print()

if __name__ == "__main__":

    my_garden = [] # Create an empty list to store the plants and flowers

    user_string = input() # Get the first line of input

    while user_string != '-1': # Continue until the user enters -1
        # Process the line of input
        line_elements = user_string.split() # Split the line into list of strings

        # Extract the plant type, plant name, and plant cost (first three elements)
        # from the list of strings
        # These will exist for both plants AND flowers
        plant_type = line_elements[0]
        plant_name = line_elements[1]
        plant_cost = line_elements[2]

        # Create the appropriate object, and add it to the list

        if plant_type == 'plant':
            # If the plant type is a plant, create a plant object (we have all the info)
            my_plant = Plant(plant_name, plant_cost)
            my_garden.append(my_plant)
        elif plant_type == 'flower':
            # If the plant type is a flower, extract the remaining two elements
            # from the list of strings
            is_annual = line_elements[3]
            color_of_flowers = line_elements[4]
            # Create a flower object (we now have all the info)
            my_flower = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(my_flower)

        user_string = input() # Get the next line of input


    # End of while loop:  I now have a my_garden list of plant and flower objects

    print_list(my_garden)
