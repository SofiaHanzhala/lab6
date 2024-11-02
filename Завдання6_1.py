write = list(map(float,input("Введіть декілька дійсних чисел: ").split()))
print(write)

rounded_integers = [round(num) for num in write]
print("Список цілих чисел: ", rounded_integers)