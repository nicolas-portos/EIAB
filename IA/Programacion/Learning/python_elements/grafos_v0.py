import pprint
import matplotlib.pyplot as plt
import numpy as np

class ErrNodoGrafo(Exception):
  def __init__(self, message='nodo no existe en el grafo'):
    super().__init__(message)


class Grafo:
  def __init__(self):
    self.nodos = {} 
    self.abiertos = []
    self.cerrados = []

  def add_node(self, nodo, **kargs):
    if nodo in self.nodos: raise ErrNodoGrafo(message="Nodo Ya Existe!!")
    self.nodos[nodo] = {"edges":{}}
    for k,v in kargs.items():
      self.nodos[nodo][k] = v

  def remove_node(self, nodo):
    if nodo not in self.nodos: raise ErrNodoGrafo
    # desconectarme de todos los nodos con los que tengo aristas
    for n in self.nodos[nodo]["edges"]:
      self.nodos[n]["edges"].pop(nodo)
    self.nodos.pop(nodo)

  def set_node_attributes(self, nodo, **kargs):
    for k,v in kargs.items():
      self.nodos[nodo][k] = v

  def get_node_attribute(self, nodo, attribute, default=None):
    ret = self.nodos[nodo].get(attribute, default)
    return ret

  def add_edge(self, nodo1, nodo2, **kargs):
    if nodo1 not in self.nodos or nodo2 not in self.nodos: raise ErrNodoGrafo
    self.nodos[nodo1]["edges"][nodo2] = kargs
    self.nodos[nodo2]["edges"][nodo1] = kargs

  def remove_edge(self, nodo1, nodo2):
    if nodo1 not in self.nodos or nodo2 not in self.nodos: raise ErrNodoGrafo
    self.nodos[nodo1]["edges"].pop(nodo2, None)
    self.nodos[nodo2]["edges"].pop(nodo1, None)

  def set_edge_attributes(self, nodo1, nodo2, **kargs):
    for k,v in kargs.items():
      self.nodos[nodo1]["edges"][nodo2][k] = v

  def get_edge_attribute(self, nodo1, nodo2, attribute, default=None):
    ret = self.nodos[nodo1]["edges"][nodo2].get(attribute, default)
    return ret

  # returna una lista con los nodos conectados
  def adj(self, nodo):
    adyacentes = [n for n in self.nodos[nodo]["edges"]]
    return adyacentes

  # quita y devuelve un nodo de abiertos,
  # si modo = profundidad devuelve el último en entrar LIFO
  # si modo = anchura devuelve el primero en entrar (FIFO)
  # .....
  def pop_abiertos(self, modo):
    ret = None
    if modo == "profundidad":
      ret = self.abiertos.pop()
    elif modo == "anchura":
      ret = self.abiertos.pop(0)
    elif modo == "dijktra":
      num = np.inf
      for nombre_nodo in self.abiertos:
        if self.nodos[nombre_nodo]["distanciaOrg"] < num:
          num = self.nodos[nombre_nodo]["distanciaOrg"]
          ret = nombre_nodo
      self.abiertos.remove(ret)
    return ret

  # si el nodo es una solución del problema devuelve TRUE
  def es_solucion(self, nodo_actual):
    print(f"Procesando nodo: {nodo_actual}")
    return False

  # devuelve una lista con todos los nodos conectados al nodo actual
  def genera_sucesores(self, nodo_actual):
    return self.adj(nodo_actual)

  # devuelve una lista con los hijos, decidiendo que hacer si ya están en abiertos o cerrados
  def procesa_repetidos(self, hijos_iniciales):
    # print(f"procesa_repetidos: {hijos_iniciales}")
    hijos = [h for h in hijos_iniciales if h not in self.abiertos and h not in self.cerrados]
    return hijos

  # hacer recorridos del grafo en profundidad, anchura, ....
  def recorre_grafo(self, nodo_inicial = None, modo="anchura"):
    self.abiertos = []
    self.cerrados = []

    # si no se proporciona inicial escojo el primero que se creó
    if nodo_inicial is None: nodo_inicial = list(self.nodos.keys())[0]
    # metemos en abiertos el nodo inicial
    self.abiertos.append(nodo_inicial)
    
    # si es el modo dijktra inicializamos el nodo inicial con coste 0 y el resto con coste infinito
    if modo == "dijktra":
      self.nodos[nodo_inicial]["distanciaOrg"] = 0
      for nodo in self.nodos:
        if nodo != nodo_inicial:
          self.nodos[nodo]["distanciaOrg"] = np.inf
     
    # calcular el valor de los nodos adyacentes 
    while len(self.abiertos) > 0: # mientras en abiertos existan nodos
      # quitar un nodo
      actual = self.pop_abiertos(modo)

      # mirar si es una solución
      # si tal break
      if self.es_solucion(actual):
        break

      # actual a cerrado
      self.cerrados.append(actual)

      # generar sucesores
      hijos = self.genera_sucesores(actual)

      # que hacer con los repetidos
      hijos = self.procesa_repetidos(hijos)         

      # insertar los hijos en abiertos
      for hijo in hijos:
        self.abiertos.append(hijo)
        if modo == "dijktra":
          if(self.nodos[actual]["distanciaOrg"] + self.nodos[actual]["edges"][hijo]["coste"] < self.nodos[hijo]["distanciaOrg"]):
            self.nodos[hijo]["distanciaOrg"] = (self.nodos[actual]["distanciaOrg"] + self.nodos[actual]["edges"][hijo]["coste"])


  def dibuja(self):
    fig, ax = plt.subplots()
    for n in self.nodos:
      
      x = self.get_node_attribute(n, "x", 0)
      y = self.get_node_attribute(n, "y", 0)
      ax.scatter(x, y, s=300)
      ax.text(x,y, n)
      
      # Dentro de cada arista[l] de cada nodo[n] mira con quien esta conectado y los junta
      for l in self.nodos[n].get("edges", None):
        ax.plot([self.get_node_attribute(n, "x", 0), self.get_node_attribute(l, "x", 0)],
                [self.get_node_attribute(n, "y", 0), self.get_node_attribute(l, "y", 0)])


    plt.show()

g = Grafo()
print(type(ErrNodoGrafo(message="Nodo Ya Existe!!")))
g.add_node("A", x=1, y=5)
g.add_node("B", x=3, y=6)
g.add_node("C", x=2, y=0)
g.add_node("D", x=4, y=2)
g.add_node("E", x=5, y=7)
g.add_edge("A", "B", coste=3)
g.add_edge("A", "C", coste=1)
g.add_edge("B", "C", coste=7)
g.add_edge("C", "D", coste=2)
g.add_edge("B", "D", coste=5)
g.add_edge("B", "E", coste=1)
g.add_edge("D", "E", coste=7)

g.recorre_grafo(modo="dijktra")
g.dibuja()
pprint.pprint(g.nodos)