import random
import heapq
class _Vertice:
    def __init__(self, id = None, valor = None):
        self.id = id
        self.valor = valor
        self.adyacencias = {}
        self.label = id

class _IteradorGrafo:
    def __init__(self, vertices, ids):
        self.ids = ids
        self.actual = 0
        self.vertices = vertices;

    def __next__(self):
        try:
            id = ids[actual]
            actual += 1
            return self.vertices[id].valor
        except IndexError:
            raise StopIteration()


class Grafos:
    def __init__(self, es_dirigido = False):
        self.vertices = {}
        self.adyacencias = {}
        self.largo = 0
        self.diri = es_dirigido

    def __len__(self):
        return self.largo

    def keys(self):
        return self.vertices.keys()

    def __getitem__(self, id):
        return self.vertices[id].valor

    def __setitem__(self, id, valor):
        if(self.vertices.get(id)==None):
            self.largo += 1
            self.vertices[id] = _Vertice(id, valor,)
        else:
            self.vertices[id].valor = valor

    def __delitem__(self, id):
        if(self.vertices.get(id)!=None):
            self.largo -= 1
            del self.vertices[id]
            for i in self.vertices:
                try:
                    del self.vertices[i].adyacencias[id]
                except KeyError:
                    pass
    def __contains__(self, id):
        return self.vertices.get(id)!=None


    def agregar_arista(self, desde, hasta, peso = 1):
        if (not self.__contains__(hasta)): raise KeyError
        self.vertices[desde].adyacencias[hasta] = peso
        if(not self.diri):
            self.vertices[hasta].adyacencias[desde] = peso

    def borrar_arista(self, desde, hasta):
        if (not self.__contains__(desde)): raise KeyError
        if (not self.__contains__(hasta)): raise KeyError
        try:
            del self.vertices[desde].adyacencias[hasta]
            if(not self.diri): del self.vertices[hasta].adyacencias[desde]
        except KeyError:
            raise ValueError

    def obtener_peso_arista(self, desde, hasta):
        try:
            return self.vertices[desde].adyacencias[hasta]
        except KeyError:
            return None

    def adyacentes(self, id):
        return self.vertices[id].adyacencias.keys()

    def random_walk(self, largo, origen = None):
        if(largo==0): return []
        camino = []
        adyacentes = []
        if(origen == None): origen = random.choice(list(self.vertices.keys()))
        camino.append(origen)
        for x in (self.vertices[origen].adyacencias):
            for i in range (self.vertices[origen].adyacencias[x]):
                adyacentes.append(x)
        return camino + self.random_walk(largo-1, random.choice(adyacentes))

    def cantidad(self):
        return len(self.vertices)

    def ver_label(self, id):
        return self.vertices[id].label

    def cambiar_label(self, id, label):
        self.vertices[id].label = label

    def pseudo_dijstra(grafo, origen, destino):
        vecinos = []
        camino = []
        padre = {}
        costo = {}
        padre[origen] = []
        costo[origen] = 0
        heapq.heappush(vecinos,(0,origen))
        while (len(vecinos)!=0):
            actual = heapq.heappop(vecinos)[1]
            for vecino_actual in grafo.adyacentes(actual):
                nuevo_costo = (costo[actual] + 1/grafo.obtener_peso_arista(actual, vecino_actual))
                if (vecino_actual not in costo or  nuevo_costo < costo[vecino_actual]):
                    costo[vecino_actual] = nuevo_costo
                    heapq.heappush(vecinos,(nuevo_costo,vecino_actual))
                    padre[vecino_actual] = actual
        return padre
