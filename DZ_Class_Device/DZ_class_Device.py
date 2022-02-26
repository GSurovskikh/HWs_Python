class Device:
    def __init__(self, price, manufacturer, color, height,weight,type):
        self.price = float(price)
        self.manufacturer = manufacturer
        self.color = color
        self.height = height
        self.weight = weight
        self.type = type

class CoffeMachine(Device):
    def __init__(self,*args, volume,type_coffee):
        super(CoffeMachine, self).__init__(*args)


class Blender(Device):
    def __init__(self,*args,volume,power):
        super(Blender, self).__init__(*args)


class MeatGrinder(Device):
    def __init__(self,*args,type_meat):
        super(MeatGrinder, self).__init__(*args)


