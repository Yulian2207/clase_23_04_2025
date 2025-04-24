class CuentaSegura:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial # Metodo privado real.
        self._historial = historial [] # Metodo protegido.

        @property
        def saldo(self):
            # Propiedad de solo lectura para consultar el saldo.
            return self.__saldo

        @saldo.setter
        def saldo (self, valor):
            # Setter para asiganr saldo solo si es un número no negativo.
            if not isinstance (valor, (init, float)):
                raise ValueError ("El saldo debe ser un número")
            if valor < 0:
                raise ValueError ("El saldo no puede ser negativo")
            self.__saldo = valor

    def depositar (self, cantidad):
        if cantidad <= 0:
            raise ValueError ("La cantidad a depositar debe ser mayor a cero")
        self.__saldo += cantidad
        self.__historial.append (f"+{cantidad}")

    def retirar (self, cantidad):
        if cantidad <= 0:
            raise ValueError ("La cantidad a retirar debe ser mayor a cero")
        if cantidad > self.saldo:
            raise ValueError ("Saldo insuficiente")
        self.__saldo -= cantidad
        self.historial.append (f"-${cantidad}")
    
    def mostrar_historial (self):
        # Método público de abstraer el detalle de como se guarda el historial
        print ("Historial de transacciones:",", ". join (self._historial))

cuenta = CuentaSegura ("Maria", 100)
print ("Titular: ", cuenta.titular)
print ("Saldo inicial: ", cuenta.saldo)

cuenta.depositar (50)
cuenta.retirar (30)
print ("Saldo actual: ", cuenta.saldo)

try: 
    cuenta.saldo = -10
except ValueError as e:
    print ("Error al asiganr saldo", e)

cuenta.mostrar_historial ()
