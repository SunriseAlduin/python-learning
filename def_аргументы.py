# Объединение аргументов в tuple
def sum_nums(*args):
    print(args)
    print(type(args))

    print(args[0])
    return sum(args)


print(sum_nums(2, 3, 7))


# Аргументы с ключевыми словами
def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


print(get_posts_info(posts_qty=25, name="Nikita"))



# Объединение аргументов в Dict
def get_post_info(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )

    return info


print(get_post_info(name="Nikita", posts_qty=25))



# дз

def merge_list_to_dict(a, b):
    merged = zip(a, b)
    itog = dict(merged)
    return itog


al = ['nikita', 'hello', 'au']
bl = [123, 15, 5]

print(merge_list_to_dict(a=al, b=bl))
print(merge_list_to_dict(al, b=bl))

# дз2

def update_car_info(**person):
    person['is_available'] = True
    return person

print(update_car_info(brand='Suzuki', price=300000))
