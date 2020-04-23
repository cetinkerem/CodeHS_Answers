inputs = []

for i in range(5):
    inputs.append(
        (
            int(input("X Coord:")),
            int(input("Y Coord: "))
        )
    )

x1, y1 = inputs[0]
x2, y2 = inputs[1]
print("Slope between " + str(inputs[0]) + " and " + str(inputs[1]) + ": " + str((y2 - y1) / (x2 - x1)))

x1, y1 = inputs[1]
x2, y2 = inputs[2]
print("Slope between " + str(inputs[1]) + " and " + str(inputs[2]) + ": " + str((y2 - y1) / (x2 - x1)))

x1, y1 = inputs[2]
x2, y2 = inputs[3]
print("Slope between " + str(inputs[2]) + " and " + str(inputs[3]) + ": " + str((y2 - y1) / (x2 - x1)))

x1, y1 = inputs[3]
x2, y2 = inputs[4]
print("Slope between " + str(inputs[3]) + " and " + str(inputs[4]) + ": " + str((y2 - y1) / (x2 - x1)))

x1, y1 = inputs[4]
x2, y2 = inputs[0]
print("Slope between " + str(inputs[4]) + " and " + str(inputs[0]) + ": " + str((y2 - y1) / (x2 - x1)))
