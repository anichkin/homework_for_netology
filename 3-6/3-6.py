class Animal():
    def __init__(self, body=1, head=1, paws=4, tail=1, weight=50, height=50):
        self.body = body
        self.head = head
        self.paws = paws
        self.tail = tail
        self.weight = weight
        self.height = height


class Livestock(Animal):
    def __init__(self, nose=1, body=1, head=1, paws=4, tail=1, weight=50, height=50):
        self.nose = nose
        self.hooves = paws
        super().__init__(body, head, paws, tail, weight, height)


class HomeBirds(Animal):
    def __init__(self, wingspan=50, beak=1, wings=2, feathers='Перья', body=1, head=1, paws=2, tail=1, weight=50,
                 height=50):
        self.wingspan = wingspan
        self.beak = beak
        self.wings = wings
        self.feathers = feathers
        super().__init__(body, head, paws, tail, weight, height)


cow = Livestock(weight=1000, height=140)
goat = Livestock(weight=100, height=50)
sheep = Livestock(weight=80, height=70)
pig = Livestock(weight=90, height=80)

duck = HomeBirds(wingspan=80, weight=2)
chicken = HomeBirds(wingspan=40, weight=1, height=40)
goose = HomeBirds(wingspan=160, weight=3, height=90)

