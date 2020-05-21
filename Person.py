from random import randint


class Person:
    GENRE = 'H'
    IDEAL_WEIGHT = -1
    UNDER_WEIGHT = 0
    OVER_WEIGHT = 1

    def __init__(self, name=None, age=None, identification_card=None, genre=None, weight=None, height=None, **kwargs):
        # Name
        if name is None:
            try:
                self.__name = kwargs.get('name')
            except Exception as e:
                print('No se ha especificado la clave \'name\'')
            else:
                self.__name = ''
        else:
            self.__name = name
        # Age
        if age is None:
            try:
                self.__age = kwargs.get('age')
            except Exception as e:
                print('No se ha especificado la clave \'age\'')
            else:
                self.__age = 1
        else:
            self.__age = age
        # Identification card
        if identification_card is None:
            try:
                self.__identification_card = kwargs.get('identification_card')
            except Exception as e:
                print('No se ha especificado la clave \'identification_card\'')
            else:
                self.__identification_card = self.generate_identification_card()
        else:
            self.__identification_card = identification_card
        # Genre
        if genre is None:
            try:
                self.__genre = kwargs.get('genre')
            except Exception as e:
                print('No se ha especificado la clave \'genre\'')
            else:
                self.__genre = self.GENRE
        else:
            self.__genre = genre
        # Weight
        if weight is None:
            try:
                self.__weight = kwargs.get('weight')
            except Exception as e:
                print('No se ha especificado la clave \'weight\'')
            else:
                self.__weight = 0
        else:
            self.__weight = weight
        # Height
        if height is None:
            try:
                self.__height = kwargs.get('height')
            except Exception as e:
                print('No se ha especificado la clave \'height\'')
            else:
                self.__height = 0
        else:
            self.__height = height

    def set_age(self, age):
        self.__age = age

    def set_genre(self, genre):
        self.__genre = genre

    def set_height(self, height):
        self.__height = height

    def set_name(self, name):
        self.__name = name

    def set_weight(self, weight):
        self.__weight = weight

    def calculate_imc(self):
        try:
            result = self.__weight / (self.__height ** 2)

            if result < 20:
                return self.IDEAL_WEIGHT
            elif 20 <= result <= 25:
                return self.UNDER_WEIGHT
            elif result < 25:
                return self.OVER_WEIGHT
        except Exception as e:
            print('Se presentó un error: {}. Reestablece el peso y la altura de la persona'.format(
                e.__str__()))

    def is_adult(self):
        return self.__age > 18

    def check_genre(self):
        return True if (self.__genre == self.GENRE) else 'H'

    def __str__(self):
        return """\
    __name:                {}
    __identification_card: {}
    __age:                 {}
    __genre:               {}
    __weight:              {}
    __height:              {} """.format(self.__name, self.__identification_card, self.__age, self.__genre,  self.__weight, self.__height)

    def generate_identification_card(self):
        return randint(999999999, 10000000000)


persona = Person(name='Johan Alexander', genre='H',
                 age=24, height=170, weight=85)
print(persona.__str__())
persona.set_age = 25
persona.set_height = 173
persona.set_weight = 80
persona.set_name = 'Alexander Londoño'
print(persona.__str__())
print('¿Es adulto?', persona.is_adult())
print('¿Es hombre?', persona.check_genre())
print('IMC:', persona.calculate_imc())
