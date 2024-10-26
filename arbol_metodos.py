import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
        print(f"Insertando {valor}:")
        self.mostrar_arbol()

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def mostrar_arbol(self):
        print("Árbol actual:")
        self._mostrar_arbol_recursivo(self.raiz, 0)

    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print('    ' * nivel + str(nodo.valor))
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def recorrido_preorden(self):
        return self._recorrido_preorden_recursivo(self.raiz)

    def _recorrido_preorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return [nodo.valor] + self._recorrido_preorden_recursivo(nodo.izquierda) + self._recorrido_preorden_recursivo(nodo.derecha)

    def recorrido_inorden(self):
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return self._recorrido_inorden_recursivo(nodo.izquierda) + [nodo.valor] + self._recorrido_inorden_recursivo(nodo.derecha)

    def recorrido_postorden(self):
        return self._recorrido_postorden_recursivo(self.raiz)

    def _recorrido_postorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return (self._recorrido_postorden_recursivo(nodo.izquierda) + 
                self._recorrido_postorden_recursivo(nodo.derecha) + 
                [nodo.valor])

    def eliminar_nodo_predecesor(self, valor):
        print(f"Eliminando nodo predecesor {valor}:")
        self.raiz = self._eliminar_nodo_predecesor_recursivo(self.raiz, valor)
        self.mostrar_arbol()

    def _eliminar_nodo_predecesor_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_nodo_predecesor_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_nodo_predecesor_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._maximo(nodo.izquierda)
            nodo.valor = temp.valor
            nodo.izquierda = self._eliminar_nodo_predecesor_recursivo(nodo.izquierda, temp.valor)
        return nodo

    def _maximo(self, nodo):
        while nodo.derecha is not None:
            nodo = nodo.derecha
        return nodo

    def eliminar_nodo_sucesor(self, valor):
        print(f"Eliminando nodo sucesor {valor}:")
        self.raiz = self._eliminar_nodo_sucesor_recursivo(self.raiz, valor)
        self.mostrar_arbol()

    def _eliminar_nodo_sucesor_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_nodo_sucesor_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_nodo_sucesor_recursivo(nodo.derecha, valor)
        else:
            if nodo.derecha is None:
                return nodo.izquierda
            elif nodo.izquierda is None:
                return nodo.derecha
            temp = self._minimo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar_nodo_sucesor_recursivo(nodo.derecha, temp.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    def recorrido_por_niveles(self):
        if not self.raiz:
            return []
        resultado = []
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.valor)
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
        return resultado

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierda), self._altura_recursiva(nodo.derecha))

    def cantidad_hojas(self):
        return self._cantidad_hojas_recursiva(self.raiz)

    def _cantidad_hojas_recursiva(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self._cantidad_hojas_recursiva(nodo.izquierda) + self._cantidad_hojas_recursiva(nodo.derecha)

    def cantidad_nodos(self):
        return self._cantidad_nodos_recursiva(self.raiz)

    def _cantidad_nodos_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._cantidad_nodos_recursiva(nodo.izquierda) + self._cantidad_nodos_recursiva(nodo.derecha)

    def es_arbol_binario_completo(self):
        if not self.raiz:
            return True
        nodos = self.cantidad_nodos()
        return self._es_completo(self.raiz, 0, nodos)

    def _es_completo(self, nodo, index, nodos):
        if nodo is None:
            return True
        if index >= nodos:
            return False
        return (self._es_completo(nodo.izquierda, 2 * index + 1, nodos) and
                self._es_completo(nodo.derecha, 2 * index + 2, nodos))

    def es_arbol_binario_lleno(self):
        if not self.raiz:
            return True
        return self._es_lleno(self.raiz)

    def _es_lleno(self, nodo):
        if nodo is None:
            return True
        if nodo.izquierda is None and nodo.derecha is None:
            return True
        if nodo.izquierda is not None and nodo.derecha is not None:
            return self._es_lleno(nodo.izquierda) and self._es_lleno(nodo.derecha)
        return False

    def eliminar_arbol(self):
        self.raiz = None
        print("Árbol eliminado.")
        self.mostrar_arbol()

    def graficar_arbol(self):
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        ax.set_title("Árbol Binario")
        ax.set_xlim(-10, 10)
        ax.set_ylim(-1, 7)
        self._graficar_recursivo(ax, self.raiz, 0, 0)
        plt.axis('off')
        plt.show()

    def _graficar_recursivo(self, ax, nodo, x, y, dx=2):
        if nodo is not None:
            ax.text(x, y, str(nodo.valor), fontsize=12, ha='center', va='center', bbox=dict(boxstyle='circle', facecolor='lightblue'))
            if nodo.izquierda is not None:
                ax.plot([x, x - dx], [y - 0.5, y - 1.5], color='black')
                self._graficar_recursivo(ax, nodo.izquierda, x - dx, y - 1.5, dx / 2)
            if nodo.derecha is not None:
                ax.plot([x, x + dx], [y - 0.5, y - 1.5], color='black')
                self._graficar_recursivo(ax, nodo.derecha, x + dx, y - 1.5, dx / 2)

arbol = Arbol()

arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(18)

arbol.graficar_arbol()

print("Buscar 7:", arbol.buscar(7))  
print("Recorrido PreOrden:", arbol.recorrido_preorden())  
print("Recorrido InOrden:", arbol.recorrido_inorden())  
print("Recorrido PostOrden:", arbol.recorrido_postorden())  
print("Recorrido por niveles:", arbol.recorrido_por_niveles())  
print("Altura del árbol:", arbol.altura())  
print("Cantidad de hojas:", arbol.cantidad_hojas())  
print("Cantidad de nodos:", arbol.cantidad_nodos())  
print("¿Es un árbol binario completo?", arbol.es_arbol_binario_completo())  
print("¿Es un árbol binario lleno?", arbol.es_arbol_binario_lleno())  

arbol.eliminar_nodo_predecesor(15)  
arbol.graficar_arbol()
arbol.eliminar_arbol()  
