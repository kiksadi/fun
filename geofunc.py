# function to greet the user
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')
# function to display a message
def display_message():
    """Display a message."""
    print("I'm learning about functions.")
display_message()
# function to calculate the area of a rectangle
def get_rectangle_area(length, width):
    """Return the area of a rectangle."""
    area = length * width
    return area
print(get_rectangle_area(2, 3))
# function to calculate the perimeter of a rectangle
def get_rectangle_perimeter(length, width):
    """Return the perimeter of a rectangle."""
    perimeter = 2 * (length + width)
    return perimeter
print(get_rectangle_perimeter(2, 3))
# function to calculate the area of a triangle
def get_triangle_area(base, height):
    """Return the area of a triangle."""
    area = (base * height) / 2
    return area
print(get_triangle_area(2, 3))
# function to calculate the perimeter of a triangle
def get_triangle_perimeter(base, height):
    """Return the perimeter of a triangle."""
    perimeter = base + height + (base * height)
    return perimeter
print(get_triangle_perimeter(2, 3))
# function to calculate the area of a circle
def get_circle_area(radius):
    """Return the area of a circle."""
    area = (radius ** 2) * 3.14
    return area
print(get_circle_area(2))
# function to calculate the perimeter of a circle
def get_circle_perimeter(radius):
    """Return the perimeter of a circle."""
    perimeter = 2 * 3.14 * radius
    return perimeter
print(get_circle_perimeter(2))
# function to calculate the area of a trapezoid
def get_trapezoid_area(base1, base2, height):
    """Return the area of a trapezoid."""
    area = ((base1 + base2) * height) / 2
    return area
print(get_trapezoid_area(2, 3, 4))
# function to calculate the perimeter of a trapezoid
def get_trapezoid_perimeter(base1, base2, height):
    """Return the perimeter of a trapezoid."""
    perimeter = base1 + base2 + (2 * height)
    return perimeter
print(get_trapezoid_perimeter(2, 3, 4))