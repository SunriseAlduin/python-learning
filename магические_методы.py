int__num = 10
float_num = 2.5
str_val = 'abc'

# print(str_val * int__num)
# умножит строку на число, потому что у строк есть такой метод
# так же и у float есть похожий метод для умножения на строку

# при этом строку на float умжножить нельзя

print(int__num.__mul__(str_val))
# NotImplemented


print(str_val.__rmul__(int__num))


# Магические методы - внутренние методы классов и обычно они
# не вызываются явно
# функция dir позволяет посмотреть все методы класса. или через точку
print(dir(bool))

# не все свойства являются методами
print(int.__doc__)


my_list = []
print(help(my_list.__eq__))