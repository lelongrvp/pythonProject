'''
This is a simple example of a Python file that contains type hints.
'''
import math


def add(x: int, y: int) -> int:
    return x+y


def subtract(x: int, y: int) -> int:
    return x - y


def multiplication(x: int, y: int) -> int:
    return x * y


def modulus(x: int, y: int) -> int:
    return x % y


def division(x: int, y: int) -> int:
    return x / y


def exponential(x: int, y: int) -> int:
    return x ** y


def floor(x: int, y: int) -> int:
    return x // y


def euclidianDistanceFinder(x1: int, y1: int, x2: int, y2: int) -> int:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


if __name__ == "__main__":
    a: int = 3
    b: int = 4
    print(add(a, b))
    print(subtract(a, b))
    print(multiplication(a, b))
    print(modulus(a, b))
    print(division(a, b))
    print(exponential(a, b))
    print(floor(a, b))
    print("My name is Long")
    print("My family name is Le")
    print("I'm from Vietnam")
    print("I'm enjoying 30 days of python")
    print(type(10))
    print(type(9.8))
    print(type(3.14))
    print(type(4-4j))
    print(type(['Asanabeh', 'Python', 'Finland']))
    print(euclidianDistanceFinder(2, 3, 10, 8))
