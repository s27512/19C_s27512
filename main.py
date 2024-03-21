#TASK1

squares = [x**2 for x in range(1, 11)]
print("List of squares from 1 to 10:")
print(squares)

#TASK2

def generate_squares(start, end):

    squares = [x**2 for x in range(start, end + 1)]
    return squares

squares_1_to_10 = generate_squares(1, 10)

squares_5_to_15 = generate_squares(5, 15)

print("List of squares from 1 to 10:")
print(squares_1_to_10)

print("\nList of squares from 5 to 15:")
print(squares_5_to_15)


