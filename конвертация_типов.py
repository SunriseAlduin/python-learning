# Python НЕ произовдит неявной конвертации типов

# Функции для явной конвертации типов
str()
int()
float()
list()
tuple()
set()

print(int('10') + 5)

# Порядок операндов имеет значение
# print(5 + '10')

# В некоторых случаях ошибки не будет
print(4.1 + 5)
print(700 + True)


# Как выполняется сложение?
# Для объекта int вызывается магический метод __add__
# метод add вернёт NotImplemented на попытку сложить Int и Float
# И в таком случае вызовется метод __radd__ для float
# а вот float уже может присоединить к себе Int