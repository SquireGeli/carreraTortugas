class ClasesConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        '''cuando se ponen dos guiones bajos delante de la propiedad, la hacemos privada
        y solo es accedible desde su propia clase y si se intenta desde fuera dara error'''
    def setPropiedadPrivada(self,valor):
        self.__propiedad_privada = valor
        '''setter nos asigna el valor de la propiedad'''
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
        '''getter nos devuelve el valor de la propiedad'''
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
        
        
if __name__ == '__main__':
    c = ClasesConGetterySetter()
    
print(c, " es su valor con getter")

cambio = input("En cuanto quieres cambiar el valor de propiedad privada con setter?")
c.setPropiedadPrivada(cambio)
print(c, " es su valor cambiado con setter")