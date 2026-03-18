import random

number = [random.randint(1, 100) for _ in range(random.randint(7, 10))]


mn = min(number)
mx = max(number)


number.remove(mn)
number.remove(mx)

average = sum(number) / len(number)

print(f"Исходные баллы: {number}")
print(f"Удаляем минимум ({mn}) и максимум ({mx}).")
print(f"Оставшиеся баллы: {number}")
print(f"Средний рейтинг: {average}")


