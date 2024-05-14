# При использовании неизменяемых объектов
# объект создастся только один раз
# Пример ниже

a = 10
b = 10
print(id(a))
print(id(b))

# Если надо избежать изменения всех копий объекта
# То копии можно создавать с помощью а = объект.copy()
# при этом вложенные объекты сохранят свои ссылки

info = {
    'name': 'Nikita',
    'is_instructor': True,
    'reviews': []
}

info_copy = info.copy()

info_copy['reviews'].append('Great course!')

print(info)
print(info_copy)

# Глубокое копирование
from copy import deepcopy

info_deepcopy = deepcopy(info)
info_deepcopy['reviews'].append('fsdfsd')

print(info)
print(info_deepcopy)

