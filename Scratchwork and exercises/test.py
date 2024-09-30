import math

# Dimensions of the rectangle
width = 10
height = 9

# Diameter of each circle
diameter = 1

# Grid arrangement
grid_circles = (width // diameter) * (height // diameter)

# Hexagonal arrangement
rows = math.floor(height / (math.sqrt(3) / 2))
odd_rows = math.ceil(rows / 2)
even_rows = rows // 2
hex_circles = (odd_rows * (width // diameter)) + (even_rows * ((width - diameter / 2) // diameter))

print(f"Grid arrangement: {grid_circles} circles")
print(f"Hexagonal arrangement: {hex_circles} circles")