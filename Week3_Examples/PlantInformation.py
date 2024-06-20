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

from PlantInformation_Functions import print_list, read_plant_input

if __name__ == "__main__":

    my_garden = read_plant_input()

    print_list(my_garden)
