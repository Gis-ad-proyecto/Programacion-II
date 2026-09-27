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
    def validaNumero(self, n):
        if n >= 0 and n <= 10:
            return True
        else:
            return False
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero entre 0 y 10")
        sigue = True
        while sigue == True:
            n = int(input("Ingresa numero: "))
            if self.validaNumero(n) == True:
                if n == self.numeroAAdivinar:
                    print("Acertaste!!")
                    self.actualizaRecord()
                    sigue = False
                else:
                    quedan = self.quitaVida()
                    if quedan == True:
                        if n < self.numeroAAdivinar:
                            print("El numero es mayor")
                        else:
                            print("El numero es menor")
                    else:
                        print("Ya no te quedan vidas!")
                        sigue = False
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
    def validaNumero(self, n):
        if n >= 0 and n <= 10:
            if n % 2 == 0:
                return True
            else:
                print("Error: El numero ingresado no es par")
                return False
        else:
            print("Error: El numero no esta entre 0 y 10")
            return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
    def validaNumero(self, n):
        if n >= 0 and n <= 10:
            if n % 2 != 0:
                return True
            else:
                print("Error: El numero ingresado no es impar")
                return False
        else:
            print("Error: El numero no esta entre 0 y 10")
            return False
class Aplicacion:
    def main(self):
        print("--- JUEGO NORMAL ---")
        j1 = JuegoAdivinaNumero(3)
        j1.juega()
        print("--- JUEGO PAR ---")
        j2 = JuegoAdivinaPar(3)
        j2.juega()
        print("--- JUEGO IMPAR ---")
        j3 = JuegoAdivinaImpar(3)
        j3.juega()
app = Aplicacion()
app.main()