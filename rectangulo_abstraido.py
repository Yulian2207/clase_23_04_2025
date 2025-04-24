class Rectangulo:
    def __init__ (self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def area (self):
    # Propiedad que va a calcular el area del rectangulo sin exponer la formula
        return self._ancho * self._alto
    
    @property
    def perimetro (self):
        # Va a calcular el perimetro de un rectangulo (calculando todo los lados)
        return 2 * (self._ancho + self._ancho)

    def escalar (self, factor):
        # Metodo publico para cambiar el tamaño sin exponer como se modifican los atributos.
        if factor <= 0:
            raise ValueError ("El factor debe ser mayor a cero")
        self._ancho *= factor
        self._alto *= factor

r = Rectangulo (4, 3)
print ("Area: ", r.area)
print ("Perimetro: ", r.perimetro)

r.escalar (2)
print ("Area tras escalar: ", r.area)