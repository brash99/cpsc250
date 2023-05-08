par = int(input())
strokes = int(input())

# Handle the error condition first
if (par < 3) or par > 5:
    name = "Error"
# Check each of the four other possibilities
elif strokes == par - 3:
    name = "Albatross"
elif strokes == par - 2:
    name = "Eagle"
elif strokes == par - 1:
    name = "Birdie"
elif strokes == par:
    name = "Par"
elif strokes == par + 1:
    name = "Bogey"
elif strokes == par + 2:
    name = "Double Bogey"
elif strokes == par + 3:
    name = "Triple Bogey"
elif strokes == par + 4:
    name = "Quadruple Bogey"
elif strokes == par + 5:
    name = "Quintuple Bogey"
else:
    name = str(strokes)

print(name)
