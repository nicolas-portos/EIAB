import re

def validar_dni(dni: str):
        PATRON = "[0-9]{8}[A-Z]"
        LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
        DNI_INVALIDOS = {"00000000T", "00000001R", "99999999R"}

        # Al realizar la comprobacion del dni, si no esta bien estructurado re.match -> None
        # Realizamos un modulo del numero del dni y eso nos da la letra que debe de tener el DNI
        return dni is not DNI_INVALIDOS \
            and re.match(PATRON, dni) is not None \
            and dni[-1] == LETRAS[int(dni[0:len(dni)-1]) % 23] 

class Persona:
    
    _nombre = ""
    _edad = 0
    _dni = ""

    def __init__(self, nombre: str, edad: int, dni: str):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad: int):
        self._edad = edad

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni: str):
        self._dni = dni

    def mostrar(self):
        print(f"Su nombre es: {self._nombre}, su edad es {self._edad} y su DNI es: {self._dni}")

    def esMayorDe_Edad(self):
        if self._edad >= 18: return True
        else: return False

p = Persona("Pepe", 18, "12345678Z")
print(f"Es {p.nombre} mayor de edad? --> ",p.esMayorDe_Edad())
print(f"Es el dni de {p.nombre} valido? --> ",validar_dni(p.dni))
p.mostrar()

class Cuenta:

    _titular = Persona("Nombre Indefinido", 0, "00000000A")
    _cantidad = 0

    def __init__(self, titular: Persona, cantidad = 0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, persona: Persona):
        self._titular = persona

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad: int):
        self._cantidad = cantidad
    
    def ingresar(self, cantidad: int):
        if cantidad >0: self._cantidad += cantidad
        else: print("No se puede añadir una cantidad negativa")

    def retirar(self, cantidad: int):
        self._cantidad -= cantidad

    def mostrar(self):
        print(f"El titular de la cuenta es {self._titular._nombre} y la cantidad es {self._cantidad}")

print("CUENTA-----------------------")
cantidad = Cuenta(Persona("Pepito", 18, "12345678Z"), 20000)
cantidad.ingresar(-1200)
cantidad.retirar(50000)
cantidad.mostrar()

class CuentaJoven(Cuenta):

    _bonificacion = 0

    def __init__(self, bonificacion: int, titular: Persona, cantidad=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion: int):
        self._bonificacion = bonificacion

    def esTitularValido(self):
        if self._titular._edad >= 18 and self._titular._edad <= 25: return True
        else: return False 

    def retirar(self, cantidad: int):
        if self.esTitularValido(): 
            if self._cantidad - cantidad >= 0: return super().retirar(cantidad)
            else: print("No se puede retirar mas dinero del que posee")
        else: print("El titular no es valido")

    def mostrar(self):
        print(f"Cuenta Joven - El titular de la cuenta es {self._titular._nombre} y la cantidad es {self._cantidad} - la bonificacion es de {self._bonificacion}%")

print("CUENTA JOVEN-----------------------")
cantidad = CuentaJoven(10, Persona("Pepito", 20, "12345678Z"), 10000)
print(cantidad.esTitularValido())
cantidad.retirar(11000)
cantidad.mostrar()