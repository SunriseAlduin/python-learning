# Словарь - пара ключ-значение
# Ключи не являются атрибутами
# т.е. получить доступ к ключу через точку нельзя

my_motorbike = {
    'brand': 'Suzuki',
    'price': 300000,
    'engine_vol': 0.6,
}

other_motorbike = {
    'brand': 'Suzuki',
    'price': 300000,
    'engine_vol': 0.6,
}

print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))


# Получение значений
print(my_motorbike['engine_vol'])

# Изменить значение просто через оператор присваивания

# Аттрибуты можно узнать через dir()
print(my_motorbike.keys())

my_motorbike['price'] = 350000
print(my_motorbike)

# Добавить новый элемент
my_motorbike['is_new'] = False
# Если же попробовать узнать значение несуществующего ключа выйдет ошибка


# Удаление элементов
del my_motorbike['is_new']
print(my_motorbike)