# Создание класса
# self - указание на кокнретный экземпляр
# экземпляры наследуют методы класса, эти методы не принадлежат экземпляру


class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")

    test = 'good'

my_car = Car()

print(type(my_car))

print(isinstance(my_car, Car))

# self передаётся автоматически первым аргументом
print(my_car.move())

print(my_car.__dict__)

my_second_car = Car()

print(my_car == my_second_car)



# __init__
class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

first_comment = Comment("First comment")
first_comment.a = 1
print(first_comment.a)

# Узнать собственные атрибуты экземпляра
print(first_comment.__dict__)