# Variables and Types

name = 'Jane'
age = 18
height = 5.5
is_student = False

print(name, type(name))
print(age, type (age))
print(height, type(height))
print(is_student, type(is_student))

# User Input and Math

name = input("What is your name? ")
birth_year = input("What year were you born? ")

age = 2026 - int(birth_year)

print("Hi, " + name + "! You are approximately " + str(age) + " years old. ")


# Type Conversion and f-strings

num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")

product = float(num_1) * float(num_2)

print(f"The product of {num_1} and {num_2} is {product}. ")

# Formatted Receipt

item = "Umbrella"
price = 10.95
quantity = 3
total = price * quantity

print("=====================")
print("       RECEIPT       ")
print("=====================")
print(f"Item: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print("---------------------")
print(f"Total: {total:.2f}")
print("=====================")


# Profile Card 

name = input("What is your name? ")
hometown = input("Where are you from? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me something fun about yourself: ")
birth_year = input("What year were you born? ")

age = 2026 - int(birth_year)

print()
print("╔══════════════════════════════╗")
print(f"          PROFILE: {name} ")
print()
print("╚══════════════════════════════╝")
print(f"Hometown: {hometown} ")
print(f"Hobby: {hobby} ")
print(f"Fun fact: {fun_fact} ")
print(f"Age: {age} ")
