def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        start = (size // 2) - 1
        return mean(numbers[start:start + 2])
    else:
        return numbers[size // 2]


def mode(numbers):
    d = {}
    for n in numbers:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return max(d, key=lambda key: d[key])


def variance(numbers):
    xbar = mean(numbers)
    ss = sum([(x - xbar) ** 2 for x in numbers])
    return ss / (len(numbers) - 1)


def stdev(numbers):
    return variance(numbers) ** 0.5

