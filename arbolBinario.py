# Clase que define un nodo en el árbol
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

# Clase que representa un árbol binario
class ArbolBinario:
    def __init__(self):
        self.raiz = None  # Inicialización de la raíz del árbol

    # Método para insertar un dato en el árbol
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    # Método privado para insertar recursivamente un dato en el árbol
    def _insertar_recursivo(self, nodo, nuevo_dato):
        if nuevo_dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.izquierda, nuevo_dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.derecha, nuevo_dato)

    # Método para mostrar el árbol en forma visual
    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz, 0)

    # Método privado para mostrar recursivamente el árbol
    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print("      " * nivel + str(nodo.dato))  # Visualización del nodo
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    # Método para buscar un dato en el árbol
    def buscar(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    # Método privado para buscar recursivamente un dato en el árbol
    def _buscar_recursivo(self, nodo, dato):
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierda, dato)
        return self._buscar_recursivo(nodo.derecha, dato)

    # Método para eliminar un dato del árbol
    def eliminar(self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    # Método privado para eliminar recursivamente un dato del árbol
    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo

    # Método auxiliar para encontrar el mínimo en un subárbol
    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.dato

    # Métodos para recorrer el árbol en preorden, inorden y postorden
    # Devuelven una lista con los elementos en el orden respectivo
    def recorrer_preOrden(self):
        resultado = []
        self.preOrden(self.raiz, resultado)
        return resultado

    def preOrden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.preOrden(nodo.izquierda, resultado)
            self.preOrden(nodo.derecha, resultado)

    def recorrer_inOrden(self):
        resultado = []
        self.inOrden(self.raiz, resultado)
        return resultado

    def inOrden(self, nodo, resultado):
        if nodo is not None:
            self.inOrden(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self.inOrden(nodo.derecha, resultado)

    def recorrer_postOrden(self):
        resultado = []
        self.postOrden(self.raiz, resultado)
        return resultado

    def postOrden(self, nodo, resultado):
        if nodo is not None:
            self.postOrden(nodo.izquierda, resultado)
            self.postOrden(nodo.derecha, resultado)
            resultado.append(nodo.dato)


# Creación de un objeto árbol
arbol = ArbolBinario()

# Función que muestra un menú interactivo para operar con el árbol
def menu():
    opcion = 0
    while opcion != 8:
        print("1.- AGREGAR UN ELEMENTO AL ARBOL")
        print("2.- BUSCAR UN ELEMNTO DEL ARBOL")
        print("3.- ELIMINAR UN ELEMENTO AL ARBOL")
        print("4.- MOSTRAR ARBOL COMPLETO")
        print("5.- RECORRER ARBOL EN PREORDEN")
        print("6.- RECORRER ARBOL EN INORDER")
        print("7.- RECORRER ARBOL EN POSTORDEN")
        print("8.- SALIR")

        opcion = int(input("ELIGE UNA OPCIÓN: "))
        print("\n")

        if opcion == 1:
            # INSERTAR ELEMENTOS
            elemento_para_insertar = int(input("INGRESA EL ELEMENTO: "))
            arbol.insertar(elemento_para_insertar)
            print("\n")
        elif opcion == 2:
            # BUSCAR ELEMENTOS
            dato_buscar = int(input("¿QUÉ NÚMERO QUIERES BUSCAR? "))
            nodo_encontrado = arbol.buscar(dato_buscar)
            if nodo_encontrado:
                print(f"EL ELEMENTO {dato_buscar} EXISTE EN EL ÁRBOL.")
            else:
                print(f"EL ELEMENTO {dato_buscar} NO EXISTE EN EL ÁRBOL")
                print("\n")
        elif opcion == 3:
            # ELIMINAR ELEMENTOS
            dato_eliminar = int(input("¿QUÉ NÚMERO QUIERES BORRAR? "))
            arbol.eliminar(dato_eliminar)
            print(f"SE ELIMINÓ EL ELEMENTO {dato_eliminar} CORRECTAMENTE DEL ÁRBOL")
            print("\n")
        elif opcion == 4:
            # MOSTRAR ARBOL COMPLETO
            arbol.mostrar_arbol()
            print("\n")
        elif opcion == 5:
            # RECORRIDO EN PREORDEN
            print("RECORRIDO EN PREORDEN ES: ", arbol.recorrer_preOrden())
            print("\n")
        elif opcion == 6:
            # RECORRIDO EN INORDER
            print("RECORRIDO EN INORDER ES: ", arbol.recorrer_inOrden())
            print("\n")
        elif opcion == 7:
            # RECORRIDO EN POSTORDEN
            print("RECORRIDO EN POSTORDEN ES: ", arbol.recorrer_postOrden())
            print("\n")
        elif opcion == 8:
            # SALIR
            print("ADIOS, VUELVE PRONTO :)")

# Ejecución del menú
menu()
