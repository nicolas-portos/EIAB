class Vehiculo:
  edad = 10
  def __init__(self, nombre):
    self.sonido = "brrrrrrrr"
    self._nombre = nombre
    self.potencia = 10

  def asigna_potencia(self, pot):
    if isinstance(pot, int):
      self.potencia = pot
    elif isinstance(pot, str):
      self.potencia = int(pot)

  def haz_ruido(self):
    print("No sé hacer ruido")

  @property
  def nombre(self):
    return f"Nombre->{self._nombre}"
  @nombre.setter
  def nombre(self, s):
    self._nombre = "super-" + s

  def __add__(self, v_otro):
    nuevo = Vehiculo("kkkkk")
    nuevo.potencia = self.potencia + v_otro.potencia
    return nuevo



class Coche(Vehiculo):
  def __init__(self, nombre):
    super().__init__(nombre)
    self.sonido = "PIIIIIIIIIIIIII"
    self.ruedas = 4
  def haz_ruido(self):
    print("PIII PIIII PIIII")

c = Coche("seat")
c.asigna_potencia(30)
c.haz_ruido()
print(c._nombre)


