class Vehicle:

    def __init__(self, owner, _model, _endine_power, _color):
        self.owner = str(owner)  # владелец трансп. ср-ва (может меняться)
        self._model = str(_model)  # модель/марка транспорта (не может меняться)
        self._endine_power = int(_endine_power) # мощность двигателя (не может меняться)
        self._color = str(_color) # название цвета (не можем менять сами)

    _COLOR_VARIANTS = ['red', 'whate', 'black'] # список допустимых цветов для окрашивания

    def get_model(self):
        print(f'Модель: {self._model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self._endine_power}')

    def get_color(self):
        print(f'Цвет: {self._color}')

    def print_info(self):
        self.get_model(), self.get_horsepower(), self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        new_color = new_color.lower()
        self.new_color = str(new_color)

        if self.new_color in self._COLOR_VARIANTS:
            self._color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5 # Вместимость машины 5 человек


vehicle1 = Sedan('Anna', 'Volga', 140, 'blue')
vehicle1.print_info()
print('-----------------------------')
vehicle1.set_color('pink')
vehicle1.set_color('red')
vehicle1.owner = 'liza'
vehicle1.print_info()
print('-----------------------------')
vehicle1.set_color('BLACK')
vehicle1.print_info()