par = int(input())
strokes = int(input())

# Handle the error condition first
if (par < 3) or par > 5:
    name = "Error"
# Check each of the four other possibilities
elif strokes == par - 2:
    name = "Eagle"
elif strokes == par - 1:
    name = "Birdie"
elif strokes == par:
    name = "Par"
elif strokes == par + 1:
    name = "Bogey"
else:
    name = "Error"

print(name)
