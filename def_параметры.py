# наличие значения по умолчанию для параметра функции делает его необязательным

def test(a=None, b=2):
    return a * b



print(test(3)) 

# значением по умолчанию может быть результат вызова функции
def test2(a=test(2)):
    return a


print(test2())


# 
def create_new_post(post):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = True
    return post_copy


initial_post = {
    'id': 234,
    'author': 'Bogdan'
}

print(create_new_post(initial_post))
print(initial_post)

