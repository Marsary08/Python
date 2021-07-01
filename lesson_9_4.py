class Car:
    ''' Автомобиль '''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        print(f'{self.name}: Скорость автомобиля {self.speed}.')


class WorkCar(Car):
    ''' Грузовой автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: Скорость автомобиля {self.speed}'


class SportCar(Car):
    ''' Спортвный автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 120 else f'{self.name}: Скорость автомобиля {self.speed}'


class TownCar(Car):
    ''' Городской автомобиль '''

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f'{self.name}: Скорость автомобиля {self.speed}'


class PoliceCar(Car):
    ''' Спортивный автомобиль '''

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('Police Chevrolet Silverado SSV', 'белый', 90)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('Work Volvo FH', 'красный', 39)
work_car.go()
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

town_car = TownCar('Audi RS6', 'красный', 59)
town_car.go()
print(town_car.show_speed())
town_car.turn(0)
town_car.turn(1)
town_car.stop()
print()

sport_car = SportCar('Sport car Nissan R390', 'черный', 240)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.turn(0)
sport_car.stop()
print()
