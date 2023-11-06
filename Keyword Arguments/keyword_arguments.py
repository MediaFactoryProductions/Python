def calculate_rectangle_area(length, width):
    return length * width

area1 = calculate_rectangle_area(length=5, width=3)
area2 = calculate_rectangle_area(width=4, length=5)

print("Area 1: ", area1)
print("Area 2:", area2)


def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Calculate the area of two different triangles
area1 = calculate_triangle_area(base=6, height=4)
area2 = calculate_triangle_area(height=7, base=5)

# Print the results
print("Area of Triangle 1:", area1)
print("Area of Triangle 2:", area2)