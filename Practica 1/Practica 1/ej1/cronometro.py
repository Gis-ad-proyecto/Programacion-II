class Cronometro:
        def __init__(self):
            self.__inicia=0
            self.__termina=0
            
        def obtener_inicia(self):
            return self.__inicia
        
        def obtener_termina(self):
            return self.__termina
        
        def inicia(self, horactual):
            self.__inicia = horactual
            self.__termina = 0 


        def detener(self, detener):
            self.__termina = detener
        
        def lapsoDeTiempo(self):
            t=self.__termina-self.__inicia
            tiempo=t*1000
            return tiempo
        
reloj1=Cronometro()
reloj1.inicia(5)
reloj1.detener(20)
print(reloj1.lapsoDeTiempo())
