write = input("Напишіть декілька слів: ").split()
print(write)

shortest_word = min(write, key=len)
print("Найкоротше слово в тексті:", shortest_word)