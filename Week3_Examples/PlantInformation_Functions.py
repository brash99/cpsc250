from PlantFlower import Plant, Flower

def print_list(garden):
    for i in range(len(garden)):
        print(f'Plant {i + 1} Information:')
        garden[i].print_info()
        print()
