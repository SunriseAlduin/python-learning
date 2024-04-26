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

# Получить доступ к ключу можно по переменной

key_name = 'brand'
other_motorbike[key_name] = 'BMW'
print(other_motorbike)

# Словари могут быть вложенными
my_motorbike['price_info'] = {
    'price': 25000,
    'is_available': True,
}

print(my_motorbike['price_info']['price'])


# Значения ключей могут быть записаны из переменной
# Можно даже вызывать в значении функцию которая вернёт итоговое значение ключа


# Длину словаря можно узнать с помощью len()

print(len(my_motorbike))
del my_motorbike['price_info']
print(len(my_motorbike))


# Есть метод словаря, чтобы узнать есть ли ключ в словаре get(ключ)
# И не получить ошибку, а None, если ключа нет
print(my_motorbike.get('model'))

# вторым значением можно передать то, что вернётся если ключа нет
print(my_motorbike.get('qty', 0))


print(my_motorbike.__doc__)