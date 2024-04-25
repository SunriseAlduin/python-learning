a = [1, True, [1], {'a': 2}, 'hi']
# a.pop[2]
del a[2]

print(len(a))

a.reverse()
print(a)

b = ['bitch', 66]

a.extend(b)

print(a)

c = [1, 2, 3]
d = ['hello']

e = c + d
print(e)

f = c.__add__(d)
print(f)