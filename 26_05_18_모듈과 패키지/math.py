import math

import statistics

for i in [1, 6, 11, 16]:

    print(f"{i}! =", math.factorial(i))

print()


st = [80, 99, 77, 65, 92, 74, 82]

print(st)

print("중앙값:", statistics.median(st))

print("평균:", round(statistics.mean(st), 2))

print("분산:", round(statistics.variance(st), 2))

print("표준편차:", round(statistics.stdev(st), 2))
