import random

def generate_set(size, lower, upper):
    return set(random.randint(lower,upper) for _ in range(size))

set1 = generate_set(15, 1, 10)
set2 = generate_set(15,1,30)

print("Перша множина:", set1)
print("Друга множина:", set2)

common_elements = set1.intersection(set2)
print("Спільні елементи:", common_elements)