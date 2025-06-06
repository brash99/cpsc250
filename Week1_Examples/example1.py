def dostuff(radius):
    global pi
    area = 4 * pi * radius * radius
    volume = (4/3) * pi * radius * radius * radius
    return (area, volume)

if __name__ == "__main__":
    print("This is the main module, not imported.")
    pi = 3.14159  # Global variable for pi
    myradius = float(input())
    myarea, myvolume = dostuff(myradius)
    print("Area:", myarea)
    print("Volume:", myvolume)
