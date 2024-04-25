my_nums = [10, 50, 0, 5, 100, 5]
res = my_nums.count(5)
print(res)

my_nums.append(25)
print(my_nums)

my_nums.insert(2, -5)
print(my_nums)

# Очистит список
# my_nums.clear()
# print(my_nums)

# расширит список элементами a, b, c
my_nums.extend('abc')
print(my_nums)


# Копирование по адресу
# other_nums = my_nums
# print(id(other_nums) == id(my_nums))

# Копирование правильное
other_nums = my_nums.copy()
print(id(other_nums) == id(my_nums))

print(len(other_nums))