# Кортеж - упорядоченная последовательность элементов
# Кортеж нельзя изменять. Неизменяемый тип как строка или число

# Объекты в кортежах могут быть разных типов
# В кортеже важен порядок элементов

my_tuple = ('apple', 151, ('hello', 1), {'a' : 1}, [1, 2])
print(my_tuple)
my2_tuple = ('apple', 151, ('hello', 1), {'a' : 1}, [1, 2])

print(my_tuple == my2_tuple)

print(len(my2_tuple))

# Получение значений
print(my2_tuple[-1])

my_nums = (10, 5, 100, 0)
print(type(my_nums))

# так нельзя my_nums[1] = 7
# удалять тоже del my_nums[1]


# При этом, если в кортеже изменяемые объекты - их содержимое можно менять 
# Кортеж словарей
users = (
    {
        'user_id': 134,
        'user_name': 'Alice',
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])
users[1]['user_id'] = 100
print(users[1]['user_id'])

a = 2
b = 3
c = 4
d = (a, b, c)
print(d)

# По несуществующему индексу - ошибка
# print(d[3])

# функция get тут недоступна

print(d + users)


# Методы кортежей
# count - количество опр. элементов в кортеже и index - найти индекс опредлённого элемента

f = (3, 3, 3, 4)
print(f.count(3))

print(f.index(4))

# Кортеж можно конвертировать в список
new_f = list(f)
new_f.append('her')
print(new_f)
# Можно конвертировать обратно в тапл
neeeew_f = tuple(new_f)
print(neeeew_f)


# Практика
my_numss = (10, 5, 100, 0, 5, 5)

# Этот способ позволяет найти следующее совпадение
# метод index поддерживает второй аргумент
# С помощью цикла можно сделать это
index_one = my_numss.index(5)
index_two = my_numss.index(5, index_one + 1)
index_therr = my_numss.index(5, index_two + 1)
print(index_therr)

my_list = list(my_numss)
my_list.append(7)
print(my_list)

my_nuuuuums = tuple(my_list)
print(my_nuuuuums)

tuple = tuple({'a': 1, 'bad': [1, 2]})
print(tuple)