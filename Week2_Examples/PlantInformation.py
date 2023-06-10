from PlantFlower import Plant, Flower


def print_list(garden):
    for i in range(len(garden)):
        print(f'Plant {i + 1} Information:')
        garden[i].print_info()
        print()


if __name__ == "__main__":
    my_garden = []
    user_string = input()

    while user_string != '-1':
        tokens = user_string.split()
        plant_type = tokens[0]
        plant_name = tokens[1]
        plant_cost = tokens[2]
        if plant_type == 'plant':
            my_plant = Plant(plant_name, plant_cost)
            my_garden.append(my_plant)
        elif plant_type == 'flower':
            is_annual = tokens[3]
            color_of_flowers = tokens[4]
            my_flower = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(my_flower)
        user_string = input()

    print_list(my_garden)
