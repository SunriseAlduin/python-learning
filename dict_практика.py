my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk)
print(id(my_disk))

print(my_disk.popitem())
print(my_disk.get('type', 'hdd'))


# Копирование словаря

new_disk = my_disk.copy()
new_disk['type'] = 'ssd'
print(my_disk)
print(new_disk)


print(len(new_disk))

# Конвертация других значений в словарь
my_list = [('first', 0), ['second', True]]
my_dict = dict(my_list)
print(my_dict)




# Задача

# diction = {

# }

# a = input('Введите ключ')
# b = input('Введите значение')
# diction[a] = b
# c = input('Введите ключ')
# d = input('Введите значение')
# diction[c] = d
# e = input('Введите ключ')
# f = input('Введите значение')
# diction[e] = f

# print(diction)

