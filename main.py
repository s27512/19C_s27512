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




#TASK5

import math


class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots


square_gen = SquareGenerator()

try:

    squares_invalid_range = square_gen.generate_squares(10, 5)
except ValueError as e:
    print("Error:", e)
else:

    squares_1_to_10 = square_gen.generate_squares(1, 10)

    square_roots_1_to_10 = square_gen.calculate_square_roots(squares_1_to_10)

    print("List of squares from 1 to 10:")
    print(squares_1_to_10)

    print("\nSquare roots of numbers in the list:")
    print(square_roots_1_to_10)



#TASK6

import math

class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

    #TASK7

    import math

    class SquareGenerator:
        def generate_squares(self, start, end):

            if end < start:
                raise ValueError("End of range must be greater than or equal to start.")

            squares = [x ** 2 for x in range(start, end + 1)]
            return squares

        def calculate_square_roots(self, numbers):

            square_roots = [math.sqrt(num) for num in numbers]
            return square_roots

        from square_package.square_generator import SquareGenerator

        square_gen = SquareGenerator()

        squares_1_to_10 = square_gen.generate_squares(1, 10)

        square_roots_1_to_10 = square_gen.calculate_square_roots(squares_1_to_10)

        print("List of squares from 1 to 10:")
        print(squares_1_to_10)

        print("\nSquare roots of numbers in the list:")
        print(square_roots_1_to_10)



    #TASK8

    import math

    class SquareGenerator:
        def generate_squares(self, start, end):

            if end < start:
                raise ValueError("End of range must be greater than or equal to start.")

            squares = [x ** 2 for x in range(start, end + 1)]
            return squares

        def calculate_square_roots(self, numbers):

            square_roots = [math.sqrt(num) for num in numbers]
            return square_roots

    class CubicGenerator(SquareGenerator):
        def generate_cubes(self, start, end):

            if end < start:
                raise ValueError("End of range must be greater than or equal to start.")

            cubes = [x ** 3 for x in range(start, end + 1)]
            return cubes

        def calculate_cube_roots(self, numbers):

            cube_roots = [math.pow(num, 1 / 3) for num in numbers]
            return cube_roots

        from square_package.square_generator import CubicGenerator

        cubic_gen = CubicGenerator()

        cubes_1_to_10 = cubic_gen.generate_cubes(1, 10)

        cube_roots_1_to_10 = cubic_gen.calculate_cube_roots(cubes_1_to_10)

        print("List of cubes from 1 to 10:")
        print(cubes_1_to_10)

        print("\nCube roots of numbers in the list:")
        print(cube_roots_1_to_10)


    #TASK9

    import math

class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")

        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

    def calculate_cube_roots(self, numbers):

        cube_roots = [math.pow(num, 1/3) for num in numbers]
        return cube_roots

    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    from square_package.square_generator import CubicGenerator

    cubic_gen = CubicGenerator()

    cubes_1_to_10 = cubic_gen.generate_cubes(1, 10)

    cube_roots_1_to_10 = cubic_gen.calculate_cube_roots(cubes_1_to_10)

    print("List of cubes from 1 to 10:")
    print(cubes_1_to_10)

    print("\nCube roots of numbers in the list:")
    print(cube_roots_1_to_10)

    try:
        squares_10_to_1 = cubic_gen.generate_squares(10, 1)
        print("\nList of squares from 10 to 1:")
        print(squares_10_to_1)
    except ValueError as e:
        print("\nError:", e)



#TASK10

import math
from abc import ABC, abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):

        pass

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")

        cubes = [x**3 for x in range(start, end + 1)]
        return cubes

    def calculate_cube_roots(self, numbers):

        cube_roots = [math.pow(num, 1/3) for num in numbers]
        return cube_roots

    def generate_squares(self, start, end):

        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")

        squares = [x**2 for x in range(start, end + 1)]
        return squares

    from square_package.square_generator import CubicGenerator

    cubic_gen = CubicGenerator()

    cubes_1_to_10 = cubic_gen.generate_cubes(1, 10)

    cube_roots_1_to_10 = cubic_gen.calculate_cube_roots(cubes_1_to_10)

    print("List of cubes from 1 to 10:")
    print(cubes_1_to_10)

    print("\nCube roots of numbers in the list:")
    print(cube_roots_1_to_10)

    squares_10_to_1 = cubic_gen.generate_squares(10, 1)
    print("\nList of squares from 10 to 1:")
    print(squares_10_to_1)










