fruits = [True, 'banana', 'lime', '123']
quantities = [100, 70, 50, 120]
availability = [True, False, True, False]

fruit_qtys_zip = zip(fruits, quantities, availability)
print(fruit_qtys_zip)

fruit_qtys_zip = list(fruit_qtys_zip)
print(fruit_qtys_zip)

# При конвертации в список мы получаем список кортежей
print(type(fruit_qtys_zip[1]))

# Для конвертации можно использовать не только списки, но и другие
# последовательности, единственное что не стоит исопльзовать структуры
# которые не гарантируют последовательность типа set



# Конвертация zip в dict

fruits_dict = zip(fruits, quantities)
a = dict(fruits_dict)
print(a[True])