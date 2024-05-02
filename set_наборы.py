# Набор - неупорядоченная последовательность элементов
# нет индексов
# содержит только УНИКАЛЬНЫЕ элементы
# можно изменять
# обычно в них сохраняют однотипные объекты

my_fruits = {'apple', 1, True, 1, 1, 1, 1}
print(my_fruits)
print(type(my_fruits))

# Можно из неуникального списка собрать только уникальные с помощью set
a = [1, 2, 3, 1, 2, 3, 5]
b = set(a)
print(b)

# Порядок элементов не важен при сравнении. индексов нет
c = {1, 5, 3, 2}
print(c == b)

print(len(b))


# 
posts_ids = {10, 25, 16, 73}
print(posts_ids)

# Изменяемые объекты в наборе
# lists_set = {[1, 2], [20, 5]}
# Такие объекты добавльять НЕЛЬЗЯ. Ни list ни dict ни set
# del не работает


# Practice
my_set = {(10, 10), 5, 15, 15}
print((my_set))

# создание пустово set
arg = set()
print(type(arg))


# Методы наборов
photo_sizes = {'1920x1080', '800x600'}
photo_sizes.add('1024x768')
print(photo_sizes)

other_sizes = {'100x100', '800x600'}
# Также сработает оператор |
all_sizes = photo_sizes.union(other_sizes)
print(all_sizes)

# также сработает оператор &
inters = photo_sizes.intersection(other_sizes)
print(inters)


# один набор включён в другой
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
res = nums.issubset(other_nums)
print(res)


# Практика
myy_set = {'abc', 'd', 'f', 'y'}
other_set = {'f', 'd'}

print(myy_set.intersection(other_set))
print(other_set.intersection(myy_set))

# не найдёт, потому что метод разложит строку на буквы
print(myy_set.intersection({'abc'}))

print(other_set.issubset(myy_set))
# если множества одинаковы тоже будет True
print(myy_set.issuperset(other_set))

# то же самое что myy_set - other_set
print(myy_set.difference(other_set))


# убрать элемент
# дискард не даст ошибку если элемента нет в списке
# .remove() - выдаст ошибку в таком случае
myy_set.discard('abc')
print(myy_set)

copied_set = myy_set.copy()
print(copied_set)

print(myy_set & copied_set)

# нахождение не пересекающихся
# объединение - пересечение
l = {1, 2, 3, 'l'}
t = {1, 2, 3, 't'}

print(l.symmetric_difference(t))
# то же самое
print((l | t) - (l & t))

# дз
dz = {1, 2, 3, 4, 5}
dz.add(6)

dz2 = {1, 2, 7, 8, 9}

dz3 = dz.intersection(dz2)
print(list(dz3))