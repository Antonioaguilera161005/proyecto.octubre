import networkx as nx
import matplotlib.pyplot as plt

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre

class ArbolGenealogico:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.miembros = {}  # Mapa para almacenar miembros por nombre

    def agregar_raiz(self, nombre):
        """Define el miembro raíz y punto de partida del árbol genealógico"""
        if nombre in self.grafo:
            print(f"El miembro {nombre} ya existe en el árbol.")
            return
        self.grafo.add_node(nombre)
        self.miembros[nombre] = Miembro(nombre)
        print(f"Miembro raíz '{nombre}' añadido.")

    def agregar_padre(self, nombre_hijo, nombre_padre):
        """Agrega un padre a un miembro existente y lo conecta en el árbol"""
        if nombre_hijo not in self.grafo:
            print(f"El miembro {nombre_hijo} no existe en el árbol.")
            return
        if nombre_padre in self.grafo:
            print(f"El miembro {nombre_padre} ya existe.")
            return
        self.grafo.add_node(nombre_padre)
        self.grafo.add_edge(nombre_padre, nombre_hijo)
        self.miembros[nombre_padre] = Miembro(nombre_padre)
        print(f"Padre '{nombre_padre}' agregado para '{nombre_hijo}'.")

    def agregar_madre(self, nombre_hijo, nombre_madre):
        """Agrega una madre a un miembro existente y lo conecta en el árbol"""
        if nombre_hijo not in self.grafo:
            print(f"El miembro {nombre_hijo} no existe en el árbol.")
            return
        if nombre_madre in self.grafo:
            print(f"El miembro {nombre_madre} ya existe.")
            return
        self.grafo.add_node(nombre_madre)
        self.grafo.add_edge(nombre_madre, nombre_hijo)
        self.miembros[nombre_madre] = Miembro(nombre_madre)
        print(f"Madre '{nombre_madre}' agregada para '{nombre_hijo}'.")

    def agregar_hijo(self, nombre_padre, nombre_hijo):
        """Agrega un hijo a un miembro existente y lo conecta en el árbol"""
        if nombre_padre not in self.grafo:
            print(f"El miembro {nombre_padre} no existe en el árbol.")
            return
        if nombre_hijo in self.grafo:
            print(f"El miembro {nombre_hijo} ya existe.")
            return
        self.grafo.add_node(nombre_hijo)
        self.grafo.add_edge(nombre_padre, nombre_hijo)
        self.miembros[nombre_hijo] = Miembro(nombre_hijo)
        print(f"Hijo '{nombre_hijo}' agregado para '{nombre_padre}'.")

    def agregar_hermano(self, nombre, nombre_hermano):
        """Agrega un hermano para un miembro"""
        if nombre not in self.grafo:
            print(f"El miembro {nombre} no existe en el árbol.")
            return
        padres = list(self.grafo.predecessors(nombre))
        if not padres:
            print(f"El miembro {nombre} no tiene padres registrados, no se puede agregar hermano.")
            return
        for padre in padres:
            self.agregar_hijo(padre, nombre_hermano)

    def buscar_relacion(self, nombre1, nombre2):
        if nombre1 not in self.grafo or nombre2 not in self.grafo:
            return f"Ambos miembros deben existir en el árbol."

        try:
            camino = nx.shortest_path(self.grafo.to_undirected(), nombre1, nombre2)
            distancia = len(camino) - 1
            if distancia == 1:
                return "Son hermanos"
            elif distancia == 2:
                return "Son primos"
            else:
                return f"Relación distante: separados por {distancia} niveles"
        except nx.NetworkXNoPath:
            return "No hay relación directa entre ellos."

    def visualizar_arbol(self):
        pos = nx.spring_layout(self.grafo)
        labels = {nodo: nodo for nodo in self.grafo.nodes()}
        nx.draw(self.grafo, pos, labels=labels, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", arrows=False)
        plt.title("Árbol Genealógico")
        plt.show()

def menu():
    print("\n=== Menú del Árbol Genealógico ===")
    print("1. Agregar miembro raíz")
    print("2. Agregar padre")
    print("3. Agregar madre")
    print("4. Agregar hijo")
    print("5. Agregar hermano")
    print("6. Buscar relación")
    print("7. Visualizar árbol")
    print("8. Salir")

def main():
    arbol = ArbolGenealogico()
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del miembro raíz: ")
            arbol.agregar_raiz(nombre)

        elif opcion == "2":
            nombre_hijo = input("Nombre del miembro: ")
            nombre_padre = input("Nombre del padre: ")
            arbol.agregar_padre(nombre_hijo, nombre_padre)

        elif opcion == "3":
            nombre_hijo = input("Nombre del miembro: ")
            nombre_madre = input("Nombre de la madre: ")
            arbol.agregar_madre(nombre_hijo, nombre_madre)

        elif opcion == "4":
            nombre_padre = input("Nombre del miembro: ")
            nombre_hijo = input("Nombre del hijo: ")
            arbol.agregar_hijo(nombre_padre, nombre_hijo)

        elif opcion == "5":
            nombre = input("Nombre del miembro: ")
            nombre_hermano = input("Nombre del hermano: ")
            arbol.agregar_hermano(nombre, nombre_hermano)

        elif opcion == "6":
            nombre1 = input("Nombre del primer miembro: ")
            nombre2 = input("Nombre del segundo miembro: ")
            relacion = arbol.buscar_relacion(nombre1, nombre2)
            print(f"Relación entre {nombre1} y {nombre2}: {relacion}")

        elif opcion == "7":
            print("Visualizando el árbol genealógico...")
            arbol.visualizar_arbol()

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor selecciona una opción del menú.")

if __name__ == "__main__":
    main()
