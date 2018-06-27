class Car:

    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        a = '{}{}\n{}{}\n{}{}\n{}{}'.format('name: ', self.model, 'color: ', self.color , 'year: ', self.year, 'price: '
                                            , self.price)
        return str(a)


car1 = Car('Audi', 'Red', '1999', '$1200')
print(car1)


class CarShowroom:
    # location = "Kiev 143"
    # name = "Expo"
    # cars = []
    def __init__(self, location, name):
        self.location = location
        self.name = name
        self._cars = []

        # print('/n/n'join.(map(str, self._cars)))

    def available_car(self):
        for i in range(len(self._cars)):
            print(self._cars[i])

    def buy_car(self, car):
        for i in range(len(self._cars)):
            if self._cars[i] == car:
                del self._cars[i]
            return self._cars

    # def __eq__(self, other):
    #     [self.model, self.color, self. year] == [other.model, other.color, other. year]

    def add_car(self, car):
        self._cars.append(car)






