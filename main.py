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


#TASK3

class SquareGenerator:
    def generate_squares(self, start, end):

        squares = [x**2 for x in range(start, end + 1)]
        return squares

square_gen = SquareGenerator()

squares_1_to_10 = square_gen.generate_squares(1, 10)

squares_5_to_15 = square_gen.generate_squares(5, 15)

print("List of squares from 1 to 10:")
print(squares_1_to_10)

print("\nList of squares from 5 to 15:")
print(squares_5_to_15)




#TASK4

import math

class SquareGenerator:
    def generate_squares(self, start, end):

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

square_gen = SquareGenerator()

squares_1_to_10 = square_gen.generate_squares(1, 10)

square_roots_1_to_10 = square_gen.calculate_square_roots(squares_1_to_10)

print("List of squares from 1 to 10:")
print(squares_1_to_10)

print("\nSquare roots of numbers in the list:")
print(square_roots_1_to_10)





