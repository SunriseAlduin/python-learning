def sum(a, b):
    c = a + b
    return c

print(sum(5, 3))


# самая короткая именованная функция
def my_fn():
    pass

print(my_fn())


# тут такой прикол что функция не видит внешний hello
hello = 12
def ad(ar):
    ar = 1
    hello = ar
    print(hello)


ad(13)
print(hello)


# Если передать в функцию внешний изменяемый объект
# то его можно изменить (вау)
dictic = {
    'a': 1,
}

def dictos(dict):
    dict['a'] += 1
    return dict


print(dictos(dictic))
print(dictic)
# Внутри функции не рекомендуется изменять внешние объекты


# Чтобы избежать изменения объекта можно воспользовать копированием
# как до функции так и внутри неё

def dictos2(dict):
    dict = dict.copy()
    dict['a'] += 2
    return dict

print(dictos2(dictic))
print(dictic)




def merge_list_to_dict(a, b):
    merged = zip(a, b)
    itog = dict(merged)
    return itog


al = ['nikita', 'hello', 'au']
bl = [123, 15, 5]

print(merge_list_to_dict(al, bl))