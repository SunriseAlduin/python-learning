# Диапазон - упорядоченная неизменяемая последовательность элементов
# есть индексы, но изменять их нельзя
# обычно ипользуются в циклах

my_range = range(7)
print(my_range)

print(list(my_range))

# начальное конечное шаг
new_range = range(10, 20, 3)
print(new_range)
print(list(new_range))

print(new_range[2])

# цикл

for n in new_range:
    print(n)


mrg = range(5)
print(mrg)
print(type(mrg))
print(mrg[-1])


for n in range(2, 7):
    print(n)


print(set(range(12,25, 5)))

print(mrg.count(13))

my = range(10, 31, 10)
spisok = []

for n in my:
    spisok.append(n)

print(spisok)    