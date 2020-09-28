def add1(n):
    return n + 1


def square(n):
    return n ** 2


def is_even(n):
    return n % 2 == 0


def get_odds(nums):
    return [n for n in nums if not is_even(n)]


def only_natural_divison(num, denom):
    if num <= 0 or denom <= 0:
        raise ValueError
    return num / denom


def dot_product(v1, v2):
    return sum((a * b for a, b in zip(v1, v2)))
