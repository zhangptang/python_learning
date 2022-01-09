# -*-coding:utf-8-*-

"""
@property装饰器
"""
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s 正在玩飞行棋' % self._name)
        else:
            print('%s 正在玩斗地主' % self._name)


if __name__ == '__main__':
    person = Person('zs', 23)
    person.play()
    person.age = 15
    person.play()
    # person.name = 'ww'   # AttributeError: can't set attribute
