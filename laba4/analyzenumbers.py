from numpy import array, sum, mean, max
from math import sqrt


def analyze_numbers():
    numbers = array([10, 20, 30, 40, 50])

    print("Масив:", numbers)
    print("Сума:", sum(numbers))
    print("Середнє:", mean(numbers))
    print("Максимум:", max(numbers))
    print("Квадратний корінь із 144:", sqrt(144))