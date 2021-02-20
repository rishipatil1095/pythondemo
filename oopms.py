class fighters:
    type = 'fighters'

    @staticmethod
    def info():
        print('This is an aircraft class')

    @classmethod
    def class_info(cls):
        cls.type = fighters.type
        print('The type of this aircraft is', fighters.type)

    def __init__(self, name, design, origin):
        self.name = name
        self.design = design
        self.origin = origin

    def get_name(self):
        return self.name

    def get_design(self):
        return self.design

    def get_origin(self):
        return self.origin

    def set_name(self, name):
        self.name = name

    def set_design(self, design):
        self.design = design

    def set_origin(self, origin):
        self.origin = origin

    def show(self):
        print(self.name, 'is designed by', self.design, 'and of', self.origin, 'origin.')

    def compare(self, other):
        if self.design == other.design:
            print(self.name, 'and', other.name, 'are from same designers')
        else:
            print(self.name, 'and', other.name, 'are not from same designers')

        if self.origin == other.origin:
            print(self.name, 'and', other.name, 'are of same origin')
        else:
            print(self.name, 'and', other.name, 'are not of same origin')


try:
    fighter1 = fighters('Su-30MKI', 'Sukhoi', 'Russian')
    fighter2 = fighters('Tejas MK1', 'HAL', 'Indian')
    fighter3 = fighters('Rafale', 'Dassault', 'French')
    fighter4 = fighters('MiG-29', 'Mikoyan', 'Russian')



    fighters.info()
    fighters.class_info()
    fighters.type = 'Attack aircraft'
    fighters.class_info()

    fighter1.compare(fighter4)
except NameError as e:
    print(e)
except TypeError as e:
    print(e)