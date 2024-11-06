class Plane:
    def __init__(self, fuel_capacity=None, name=None, people=None, wingspan=None, pas_or_cargo=None):
        self.__fuel_capacity = fuel_capacity
        self.__name = name
        self.__people = people
        self.wingspan = wingspan
        self.pas_or_cargo = pas_or_cargo


    def get_fuel_capacity(self):
        return self.__fuel_capacity

    def get_name(self):
        return self.__name

    def get_people(self):
        return self.__people


    def __str__(self):
        return (f'\nНазва: "{self.__name}"'
                f'\nОб\'єм бака: {self.__fuel_capacity}'
                f'\nКількість людей: {self.__people}')

    def __repr__(self):
        return (f'\nНазва: "{self.__name}"\n'
                f'Об\'єм бака: {self.__fuel_capacity}\n'
                f'Кількість людей: {self.__people}\n'
                f'Розмах Крила: {self.wingspan}\n'
                f'Тип: {self.pas_or_cargo}')

    def __del__(self):
        print(f'{self.__str__()}')


def main():
    plane1 = Plane(216840, "Boeing 747-400", 660, 64.4, "Пасажирський")
    plane2 = Plane(139100, "Airbus A330-200F", 2, 60.3, "Вантажний")
    plane3 = Plane(13000, "Embraer E190", 100, 28.7, "Пасажирський")
    
    print(repr(plane1))
    print(repr(plane2))
    print(repr(plane3))



main()
