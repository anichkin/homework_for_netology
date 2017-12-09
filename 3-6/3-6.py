class Animal():
    def __init__(self, name='животное', body=1, head=1, paws=4, tail=1, weight=50, height=50):
        self.name = name
        self.body = body
        self.head = head
        self.paws = paws
        self.tail = tail
        self.weight = weight
        self.height = height


class Livestock(Animal):
    def __init__(self, nose=1, name='Домашний скот', body=1, head=1, paws=4, tail=1, weight=50, height=50):
        self.nose = nose
        self.hooves = paws
        super().__init__(name, body, head, paws, tail, weight, height)


class HomeBirds(Animal):
    def __init__(self, wingspan=50, beak=1, wings=2, feathers='Перья', name='Домашние птицы', body=1, head=1, paws=2,
                 tail=1, weight=50,
                 height=50):
        self.wingspan = wingspan
        self.beak = beak
        self.wings = wings
        self.feathers = feathers
        super().__init__(name, body, head, paws, tail, weight, height)


class Cow(Livestock):
    def __init__(self, nose=1, name='Корова', body=1, head=1, paws=4, tail=1, weight=1000, height=140):
        super().__init__(nose, name, body, head, paws, tail, weight, height)


class Goat(Livestock):
    def __init__(self, nose=1, name='Коза', body=1, head=1, paws=4, tail=1, weight=100, height=50):
        super().__init__(nose, name, body, head, paws, tail, weight, height)


class Sheep(Livestock):
    def __init__(self, nose=1, name='Овца', body=1, head=1, paws=4, tail=1, weight=80, height=70):
        super().__init__(nose, name, body, head, paws, tail, weight, height)


class Pig(Livestock):
    def __init__(self, nose=1, name='Свинья', body=1, head=1, paws=4, tail=1, weight=90, height=80):
        super().__init__(nose, name, body, head, paws, tail, weight, height)


class Duck(HomeBirds):
    def __init__(self, wingspan=80, beak=1, wings=2, feathers='Перья', name='Утка', body=1, head=1, paws=2,
                 tail=1, weight=2, height=50):
        super().__init__(wingspan, beak, wings, feathers, name, body, head, paws, tail, weight, height)


class Chicken(HomeBirds):
    def __init__(self, wingspan=40, beak=1, wings=2, feathers='Перья', name='Курица', body=1, head=1, paws=2,
                 tail=1, weight=1, height=40):
        super().__init__(wingspan, beak, wings, feathers, name, body, head, paws, tail, weight, height)


class Goose(HomeBirds):
    def __init__(self, wingspan=160, beak=1, wings=2, feathers='Перья', name='Гусь', body=1, head=1, paws=2,
                 tail=1, weight=3, height=90):
        super().__init__(wingspan, beak, wings, feathers, name, body, head, paws, tail, weight, height)

