class Vehicle:
    def __init__(self, color, wheel):
        self.color = color
        self.wheel = wheel

    def __str__(self):
        return "Clase Vehículo: \n-->Color: {} \n-->Rueda(s): {} \n".format(self.color, self.wheel)


class Bike(Vehicle):
    def __init__(self, color, wheel, kind):
        self.color = color
        self.kind = kind
        self.wheel = wheel

    def __str__(self):
        return "Clase Bike: \n-->Color: {} \n-->Rueda(s): {} \n-->Modelo: {} \n".format(self.color, self.wheel, self.kind)


class Motorbike(Bike):
    def __init__(self, color, wheel, displacement, speed, kind):
        self.color = color
        self.displacement = displacement
        self.kind = kind
        self.speed = speed
        self.wheel = wheel

    def __str__(self):
        return "Clase MotorBike: \n-->Color: {} \n-->Rueda(s): {} \n-->Cilindraje: {} \n-->Km/h: {}\n-->Modelo: {} \n".format(self.color, self.wheel, self.kind, self.speed, self.displacement)


class Car(Vehicle):
    def __init__(self, color, wheel, displacement, speed):
        self.color = color
        self.displacement = displacement
        self.speed = speed
        self.wheel = wheel

    def __str__(self):
        return "Clase Car: \n-->Color: {} \n-->Rueda(s):{} \n-->Cilindraje: {} \n-->Km/h: {} \n".format(self.color, self.speed, self.wheel, self.displacement)


class Van(Car):
    def __init__(self, color, wheel, displacement, speed, load):
        self.color = color
        self.displacement = displacement
        self.load = load
        self.speed = speed
        self.wheel = wheel

    def __str__(self):
        return "Clase Van: \n-->Color: {} \n-->Rueda(s): {} \n-->Cilindraje: {} \n-->Km/h: {} \n-->Cargamento: {} \n".format(self.color, self.speed, self.wheel, self.displacement, self.load)


car = Car('rojo', 4, 120, 1100)
bike = Bike("negro-blanco", 2, "sport")
motorbike = Motorbike("negro-rojo", 2, 150, 110, "doble propósito")
van = Van("steel", 4, 2300, 100, 500)

print(str(car))
print(str(bike))
print(str(motorbike))
print(str(van))

vehicles = [car, bike,  motorbike, van]


def catalog(vehicles, wheels=4):
    counter = 0
    for vehicle in vehicles:
        if vehicle.wheel == wheels:
            counter += 1

    if counter == 0:
        print("No hay vehículos con {} ruedas en el catálogo \n".format(wheels))
    else:
        print("Se han encontrado {} vehículos con {} ruedas \n".format(counter, wheels))


catalog(vehicles, 2)
