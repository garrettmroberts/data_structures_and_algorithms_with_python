# 1.1
from random import randint, randrange
from typing import List, Tuple


def is_multiple(n: int, m: int):
    if (n == 0 or m == 0): return False
    return n % m == 0

# 1.2
def is_even(k: int) -> bool:
    return bin(k)[-1] == '0'

# 1.3
def minmax(data: List[int]) -> Tuple[int, int]:
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        elif x > max_val:
            max_val = x
    return (min_val, max_val)

# 1.4
def sum_of_squares(n: int) -> int:
    sum = 0
    for x in range(1, n):
        sum += x**2
    return sum

# 1.5
def sum_of_squares_redux(n: int) -> int:
    return sum(i**2 for i in range(1, n))

# 1.6
def sum_of_odd_squares(n: int) -> int:
    sum = 0
    for x in range(1, n, 2):
        sum += x**2
    return sum

# 1.7
def sum_of_odd_squares_redux(n: int) -> int:
    return sum(i**2 for i in range(1, n, 2))

# 1.9
list(range(50, 81, 10))

#1.10
list(range(8, -9, -2))

#1.11
[2**x for x in range(9)]

#1.12
def random_choice(data: List[str]) -> List[str]:
    return data[randrange(len(data))]

# 1.14
def find_odd_pair(data: List[int]) -> bool:
    odds = {x for x in data if x % 2}
    return len(odds >= 2)

# 1.15
def distinct_numbers(data: List[int]) -> bool:
    return len(data) == len(set(data))

# 1.18
[x * (x-1) for x in range(1,11)]

#1.19
[chr(x) for x in list(range(97, 123))]

#1.20
def shuffle(data: List) -> List:
    n = len(data)
    for i in range(n):
        j = randint(i, n-1)
        data[i], data[j] = data[j], data[i]
    return data
