import matplotlib.pyplot as plt
import numpy as np
import json, pprint

class ErrNodoGrafo(Exception):
  def __init__(self, message='nodo no existe en el grafo'):
    super().__init__(message)

class GrafoBase:
  def __init__(self):
    self.nodos = {}

  def add_node(self, nodo, **kargs):
    if nodo in self.nodos: raise ErrNodoGrafo(message="Nodo Ya Existe!!")
    
    self.nodos[nodo] = {"edges":{}}
    
    for key,value in kargs.items():
      self.nodos[nodo][key] = value

  def remove_node(self, nodo):
    if nodo not in self.nodos: raise ErrNodoGrafo
    
    for n in self.nodos[nodo]["edges"]:
      self.nodos[n]["edges"].pop(nodo)
    
    self.nodos.pop(nodo)

  def set_node_attributes(self, nodo, **kargs):
    for key,value in kargs.items():
      self.nodos[nodo][key] = value

  def get_node_attribute(self, nodo, attribute, default=None):
    return self.nodos[nodo].get(attribute, default)

  def add_edge(self, nodo1, nodo2, **kargs):
    if nodo1 not in self.nodos or nodo2 not in self.nodos: raise ErrNodoGrafo
    self.nodos[nodo2]["edges"][nodo1] = kargs
    self.nodos[nodo1]["edges"][nodo2] = kargs
    
  def remove_edge(self, nodo1, nodo2, defaultValue=None):
    if nodo1 not in self.nodos or nodo2 not in self.nodos: raise ErrNodoGrafo
    self.nodos[nodo2]["edges"].pop(nodo1, defaultValue)
    self.nodos[nodo1]["edges"].pop(nodo2, defaultValue)

  def set_edge_attributes(self, nodo1, nodo2, **kargs):
    for key,value in kargs.items():
      self.nodos[nodo1]["edges"][nodo2][key] = value

  def get_edge_attribute(self, nodo1, nodo2, attribute, default=None):
    return self.nodos[nodo1]["edges"][nodo2].get(attribute, default)

  # returna una lista con los nodos conectados
  def adj(self, nodo):
    return [n for n in self.nodos[nodo]["edges"]]

  def save_grafo(self, filename):
      with open(filename, 'w') as f:
          json.dump(self.nodos, f, indent="\t")

  def load_grafo(self, filename):
      with open(filename) as f:
          # Cargar su contenido y crear un diccionario
          self.nodos = json.load(f)

  def dibuja(self):
    fig = plt.figure(figsize=(10,8))

  # para cada nodo, dibuja un circulo en la posicion x1, y1
    for n in self.nodos:
      x1 = self.get_node_attribute(n, "x", 0)
      y1 = self.get_node_attribute(n, "y", 0)
      plt.scatter(x1, y1, s=300)
      plt.text(x1,y1, n)
      # plt.text(x1,y1-0.2, str(self.get_node_attribute(n, "distanciaOrg", 0))) # muestra el valor de cada DistanciaOrg(dijsktra) en cada nodo

      # para cada arista
      # for arista in self.nodos[n]["edges"]:
      for arista in self.get_node_attribute(n, "edges"):
        # mira la posicion del nodo destino x2, y2
        x2 = self.get_node_attribute(arista, "x", 0)
        y2 = self.get_node_attribute(arista, "y", 0)
        plt.plot([x1, x2], [y1, y2], color="b", linewidth=0.5)
        # Escribe el weight en la mitad de camino entre los dos nodos
        plt.text((x1+x2)/2, (y1+y2)/2, self.get_edge_attribute(n, arista, "weight", 0), alpha=0.5)

  def dibuja_ruta(self, ruta):
    for i in range(len(ruta)):
      if i == 0: continue # forzamos al que entre a este codigo solo con el 2 valor (o sea el 1) ya que hacemos un i-1 y no puede haber numeros negativos en una lista
      x1 = self.get_node_attribute(ruta[i-1], "x")
      y1 = self.get_node_attribute(ruta[i-1], "y")
      x2 = self.get_node_attribute(ruta[i], "x")
      y2 = self.get_node_attribute(ruta[i], "y")
      plt.plot([x1, x2], [y1, y2], color="k", linewidth=3)

class Grafo(GrafoBase):
  def __init__(self):
    super().__init__()
    self.abiertos = []
    self.cerrados = []

 # quita y devuelve un nodo de abiertos,
  # si modo = profundidad devuelve el último en entrar LIFO
  # si modo = anchura devuelve el primero en entrar (FIFO)
  # si modo = dijkstra devuelve el nodo mas pequeño en base a la distanciaOrg
  # si modo = avaricioso devuelve el nodo mas pequeño en base a la distanciaDst
  def pop_abiertos(self, modo, f_astra=1, coste_max=10):
    ret = None
    if modo == "profundidad":
      ret = self.abiertos.pop()
    elif modo == "anchura":
      ret = self.abiertos.pop(0)
    elif modo == "dijkstra":
      num = np.inf
      for nombre_nodo in self.abiertos:
        if self.nodos[nombre_nodo]["distanciaOrg"] < num:
          num = self.nodos[nombre_nodo]["distanciaOrg"]
          ret = nombre_nodo
      self.abiertos.remove(ret)
      # idx_min = 0
      # for i, n in enumerate(self.abiertos):
      #   if self.get_node_attribute(n, "distanciaOrg") < self.get_node_attribute(self.abiertos[idx_min], "distanciaOrg"):
      #     idx_min = i
      # ret = self.abiertos.pop(idx_min)
    elif modo == "avaricioso":
      valorBorrar = min(self.abiertos, key=lambda x: self.get_node_attribute(x ,"distanciaDst"))
      self.abiertos.remove(valorBorrar)
      ret = valorBorrar
      # idx_min = 0
      # for i, n in enumerate(self.abiertos):
      #   if self.get_node_attribute(n, "distanciaDst") < self.get_node_attribute(self.abiertos[idx_min], "distanciaDst"):
      #     idx_min = i
      # ret = self.abiertos.pop(idx_min)
    elif modo == "A*":
      # valorBorrar = min(self.abiertos, key=lambda x: (self.get_node_attribute(x ,"distanciaDst") + self.get_node_attribute(x ,"distanciaOrg"))/2)
      valorBorrar = min(self.abiertos, key=lambda x: ((self.get_node_attribute(x ,"distanciaDst")*f_astra) + 
                                                      (self.get_node_attribute(x ,"distanciaOrg") * (1-f_astra))))
      self.abiertos.remove(valorBorrar)
      ret = valorBorrar
    elif modo == "IDA*":
      # TODO
      pass
    return ret

  # si el nodo es una solución del problema devuelve TRUE
  def es_solucion(self, nodo_actual):
    # print(f"Procesando nodo: {nodo_actual}")
    return False

  # devuelve una lista con todos los nodos conectados al nodo actual
  def genera_sucesores(self, nodo_actual):
    return self.adj(nodo_actual)

  # devuelve una lista con los hijos, decidiendo que hacer si ya están en abiertos o cerrados
  def procesa_repetidos(self, hijos_iniciales):
    # print(f"procesa_repetidos: {hijos_iniciales}")
    return [h for h in hijos_iniciales if h not in self.abiertos and h not in self.cerrados]

  # hacer recorridos del grafo en profundidad, anchura, dijkstra ....
  def recorre_grafo(self, nodo_inicial = None, nodo_destino = None, modo="anchura", factor_astar=1):
    self.abiertos = []
    self.cerrados = []

    # si no se proporciona inicial escojo el primero que se creó
    if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]

# poner en todos los nodos un atributo distanciaOrg = inf
# excepto en el inicial que es 0
    for n in self.nodos:
      self.set_node_attributes(n, distanciaOrg = np.inf)
      self.set_node_attributes(n, antecesor=None)
      self.set_node_attributes(n, distanciaDst=None)
    self.set_node_attributes(nodo_inicial, distanciaOrg = 0)
    self.set_node_attributes(nodo_inicial, distanciaDst = 0)
    #if modo == "dijkstra":
    #  self.nodos[nodo_inicial]["distanciaOrg"] = 0
    #  for nodo in self.nodos:
    #    if nodo != nodo_inicial: self.nodos[nodo]["distanciaOrg"] = np.inf

    # metemos en abiertos el nodo inicial
    self.abiertos.append(nodo_inicial)

    while len(self.abiertos) > 0: # mientras en abiertos existan nodos
      # quitar un nodo
      actual = self.pop_abiertos(modo, factor_astar)

      # mirar si es una solución
      # si tal break
      if self.es_solucion(actual):
        break

      # actual a cerrado
      self.cerrados.append(actual)

      # generar sucesores
      hijos = self.genera_sucesores(actual)

      # para cada hijo,
      # Si (distanciaOrg de actual + coste hacia el hijo )   <    distanciaOrg del hijo
      #       distanciaOrg del hijo = (distanciaOrg de actual + coste hacia el hijo )
      # djikstra
      d_actual = self.get_node_attribute(actual, "distanciaOrg", 0)
      for hijo in hijos:
        c_hijo = self.get_edge_attribute(actual, hijo, "weight", 0)
        d_hijo = self.get_node_attribute(hijo, "distanciaOrg", 0)
        if (c_hijo + d_actual) < d_hijo:
          self.set_node_attributes(hijo, distanciaOrg=(c_hijo+d_actual))
          self.set_node_attributes(hijo, antecesor=actual)
      # calcular la distancia a destino de cada hijo y anotarla en él
      # Avaricioso
        if nodo_destino:
          d_destino = self.calcula_distanciaDst(hijo, nodo_destino)
          # actualizar en hijo esta distancia
          self.set_node_attributes(hijo, distanciaDst=d_destino)

      # que hacer con los repetidos
      hijos = self.procesa_repetidos(hijos)

      # insertar los hijos en abiertos
      for hijo in hijos:
        self.abiertos.append(hijo)

  def calcula_distanciaDst(self, destino, origen):
    # retorna una heurística de la distancia...
    ret = 0
    return ret

  def genera_ruta(self, inicio, puntero="antecesor"):
      l = []
      nodo = inicio
      while nodo is not None and nodo not in l:
        l.append(nodo)
        nodo = self.get_node_attribute(nodo, puntero)
      return l
  
class Provincias(Grafo):
  def calcula_distanciaDst(self, nodo, nodo_destino):
    x1 = self.get_node_attribute(nodo, "x")
    y1 = self.get_node_attribute(nodo, "y")
    x2 = self.get_node_attribute(nodo_destino, "x")
    y2 = self.get_node_attribute(nodo_destino, "y")

    return (((x1 - x2)**2 + (y1 - y2)**2) ** 0.5) * 111
    # return (abs(x1-x2) + abs(y1-y2)) * 111
    # return np.sqrt((x2-x1)**2 + (y2-y1)**2) # Euclidean
    # return np.abs(x1 - x2) + np.abs(y1 - y2) # Manhattan
    
  
g = Provincias()
g.load_grafo("IA\Programacion\Ejercicios\grafo_provincias\\archives\gprovincias.json")
n_destino = "Cádiz"
# g.recorre_grafo(nodo_inicial = "A Coruña", modo = "profundidad")
# g.recorre_grafo(nodo_inicial = "A Coruña", modo = "anchura")
# g.recorre_grafo(nodo_inicial = "A Coruña", modo = "dijkstra",)
# g.recorre_grafo(nodo_inicial = "A Coruña", nodo_destino = n_destino, modo = "avaricioso")
# menor factor = dijkstra - mayor factor = avaricioso
g.recorre_grafo(nodo_inicial = "A Coruña", nodo_destino = n_destino, modo = "A*",factor_astar=0.9)
g.dibuja()
ruta = g.genera_ruta(n_destino)
g.dibuja_ruta(ruta)
plt.show()
print(ruta[::-1])