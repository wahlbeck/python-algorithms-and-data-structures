"""
В пайтоне как в JS можно добавлять поля (атрибуты класса) в рантайме.
Пример 1:
"""
class RegularClass:
    pass

def ex1():
    r = RegularClass()
    # в рантайме добавляем как в js
    r.foo = "foo"
    print(r.foo)
    # python создает внутри класс объект __dict__ чтоб можно было легко удалять и добавлять атрибуты:
    print(r.__dict__)

"""
Это понижает скорость доступа к атрибутам и увеличивает расходы памяти!
Если нам не надо добавлять в рантайме ничего и мы заранее знаем, какие атрибуты будут у класса, то есть метод
__slots__, который позволяет отказаться от __dict__ .
Переделаем пример 1:
"""
class RegularClass2:
    __slots__ = ("foo")

def ex2():
    r = RegularClass2()
    r.foo = "foo"
    print(r.foo)
    r.bar = 5
    print(r.bar) # будет ошибка


"""
Не работает для наследования, если у родителя есть слотс. В этом случае надо ребенку тоже указать свой слотс.
Можно не дублировать у родителя слотс, просто добавить свой.
Пример 2.
"""

def ex3():
    class SlotsClass:
        __slots__ = ("foo")

    class ChildSlotsClass(SlotsClass):
        __slots__ = ("bar")

    s = ChildSlotsClass()
    s.foo = "foo"
    s.bar = "bar"
    s.baz = "baz"
    print(s.foo)
    print(s.bar)
    print(s.baz) # ошибка


def main():
    # ex1()
    # ex2()
    ex3()


if __name__ == '__main__':
    main()