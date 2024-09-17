class Nodo:
    def __init__(self, datos: str) -> None:
        self.si = None
        self.no = None
        self.datos = datos

class ArbolBinarioHojas:
    def __init__(self) -> None:
        self.root = Nodo("¿Hojas con forma de aguja?")
        self.root.si = Nodo("¿Acículas largas?")
        self.root.si.si = Nodo("Pino")
        self.root.si.no = Nodo("¿Acículas verticiliadas?")
        self.root.si.no.si = Nodo("Cedro")
        self.root.si.no.no = Nodo("Abeto")
        self.root.no = Nodo("¿Hojas escamosas y imbricadas?")
        self.root.no.si = Nodo("¿Hojas compuestas?")
        self.root.no.si.si = Nodo("¿Hojas palmado?")
        self.root.no.si.si.si = Nodo("Castaño de indias")
        self.root.no.si.si.no = Nodo("¿Fruto en legumbre?")
        self.root.no.si.si.no.si = Nodo("Falsa acacia")
        self.root.no.si.si.no.no = Nodo("Fresno")
        self.root.no.si.no = Nodo("¿Hojas duras?")
        self.root.no.si.no.si = Nodo("¿Fruto de bellota?")
        self.root.no.si.no.si.si = Nodo("Encina")
        self.root.no.si.no.si.no = Nodo("Madroño")
        self.root.no.si.no.no = Nodo("¿Hoja Penninervia?'")
        self.root.no.si.no.no.si = Nodo("¿Es la hoja 2 veces más larga que ancha?")
        self.root.no.si.no.no.si.si = Nodo("Sauce llorón")
        self.root.no.si.no.no.si.no = Nodo("¿Es el borde inferior asimétrico?")
        self.root.no.si.no.no.si.no.si = Nodo("Olmo")
        self.root.no.si.no.no.si.no.no = Nodo("Chopo")
        self.root.no.si.no.no.no = Nodo("¿Es un fruto con dos alas que forman un ángulo?")
        self.root.no.si.no.no.no.si = Nodo("Arce")
        self.root.no.si.no.no.no.no = Nodo("Plátano de sombra")
        self.root.no.no = Nodo("Ciprés")
        
    def buscar(self) -> str:
        
        def buscar_recursivo(actual: Nodo) -> str:
            if actual.si is None and actual.no is None: return actual.datos
            
            if input(f"{actual.datos} si o cualquier otra palabra\n").lower() == 'si': return buscar_recursivo(actual.si)
            else: return buscar_recursivo(actual.no)
        
        return buscar_recursivo(self.root)

arbol = ArbolBinarioHojas()

tipo_de_hoja = arbol.buscar()
print(tipo_de_hoja)