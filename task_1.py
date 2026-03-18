import random

number = [random.randint(1, 100) for _ in range(random.randint(7, 10))]


min_number = min(number)
max_number = max(number)


number.remove(min)
number.remove(max)

average = sum(number) / len(number)






