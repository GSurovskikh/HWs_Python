class Device:
    def __init__(self, priceUSD, manufacturer, color, height,weight,type):
        self.priceUSD = float(priceUSD)
        self.manufacturer = manufacturer
        self.color = color
        self.height = float(height)
        self.weight = float(weight)
        self.type = type

class CoffeMachine(Device):
    def __init__(self,priceUSD, manufacturer, color, height,weight,type, volume,type_coffee):
        super(CoffeMachine, self).__init__(priceUSD, manufacturer, color, height,weight,type)


class Blender(Device):
    def __init__(self,priceUSD, manufacturer, color, height,weight,type,volume,power):
        super(Blender, self).__init__(priceUSD, manufacturer, color, height,weight,type)


class MeatGrinder(Device):
    def __init__(self,priceUSD, manufacturer, color, height,weight,type,type_meat):
        super(MeatGrinder, self).__init__(priceUSD, manufacturer, color, height,weight,type)


if __name__ == '__main__':
    d = Device(50, "Samsung", "black", 15,1,"unknown-device")
    print(isinstance(d,Device))
    print(d.type)
    print('---------')

    c = CoffeMachine(100,"Tefal","Metalic",40,4,"drip",1,"ground")
    print(isinstance(c,CoffeMachine))
    print(c.priceUSD)
    print('---------')

    b = Blender(200,"Bosch","yellow",13,0.7,"electricity",1,0.7)
    print(isinstance(b,Blender))
    print(b.manufacturer)
    print("---------")

    m = MeatGrinder(20, "Moulinex", "black", 25,0.5,"mechanical","beef")
    print(isinstance(m,MeatGrinder))
    print(m.color)