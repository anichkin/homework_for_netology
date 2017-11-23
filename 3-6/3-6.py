class Animal():
    def body(self, value):
        self.value = 1

    def head(self, value):
        self.value = 1

    def paws(self, value):
        self.value = 4

    def tail(self, value):
        self.value = 1


class Livestock(Animal):
    def nose(self, value):
        self.value = 1

    def hooves(self, value):
        self.value = 4



class HomeBirds(Animal):
    def beak(self, value):
        self.value = 1

    def feathers(self):
        print('Перья')

    def wings(self, value):
        self.value = 4



