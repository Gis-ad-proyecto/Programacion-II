class Sensor:
    tipo = "Generico"
    def __init__(self, id):
        self.id = id
        self.encendido = False
    def activar(self):
        self.encendido = True
        print("Sensor activado")
    def desactivar(self):
        self.encendido = False
        print("Sensor desactivado")
class Camara(Sensor):
    tipo = "Camara"
    def __init__(self, id, resolucion):
        super().__init__(id)
        self.resolucion = resolucion
class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"
    def __init__(self, id, alcance):
        super().__init__(id)
        self.alcance = alcance
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehiculo Autonomo"
    def __init__(self, id, resolucion, alcance):
        Sensor.__init__(self, id)
        self.resolucion = resolucion
        self.alcance = alcance
    def mostrar(self):
        print("ID:", self.id)
        print("Tipo:", VehiculoAutonomo.tipo)
        print("Resolucion:", self.resolucion)
        print("Alcance:", self.alcance)
        if self.encendido == True:
            print("Encendido: True")
        else:
            print("Encendido: False")
v = VehiculoAutonomo("V01", "1080p", 100)
v.mostrar()
v.activar()
v.desactivar()