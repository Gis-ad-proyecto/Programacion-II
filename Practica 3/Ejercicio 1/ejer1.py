import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
        self.vidasIniciales = numeroDeVidas
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print("Nuevo record:", self.record)
    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1
        if self.numeroDeVidas > 0:
            return True
        else:
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero entre el 0 y el 10")
        bandera = True
        while bandera == True:
            num = int(input("Ingresa tu numero: "))
            if num == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                bandera = False
            else:
                quedan = self.quitaVida()
                if quedan == True:
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor. Intenta de nuevo")
                    else:
                        print("El numero es menor. Intenta de nuevo")
                else:
                    print("Ya no tienes vidas!")
                    bandera = False
class Aplicacion:
    def main(self):
        j = JuegoAdivinaNumero(3)
        j.juega()
a = Aplicacion()
a.main()