import heapq

class ListaAdyacenciasPonderado:
    def __init__(self) -> None:
        self.lista_adyacencia = {}
        
    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []
    
    def agregar_arista(self, vertice, arista, distancia):
        if vertice in self.lista_adyacencia:
            self.lista_adyacencia[vertice].append((arista, distancia))
    
    def mostrar_lista(self):
        for vertice in self.lista_adyacencia:
            print(f"{vertice}: {self.lista_adyacencia[vertice]}")
            
    def buscar_camino_minimo(self, hospitalpartida, hospitalllegada): #se busca mediante dfs y el algoritmo de dijkstra el camino minimo para el traslado de un pasiente de un hospital a otro
        distancias =  {nodo: float('inf') for nodo in self.lista_adyacencia}
        distancias[hospitalpartida] = 0
        cola_prioridad = [(0,hospitalpartida)]
        rutas = {hospitalpartida:[]}
        
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            
            if nodo_actual == hospitalllegada:
                return distancias[hospitalllegada], rutas[hospitalllegada]+[hospitalllegada]
            
            for vecino, peso in self.lista_adyacencia[nodo_actual]:
                distancia = distancia_actual + peso
                if distancia < distancia[vecino]:
                    distancias[vecino] = distancia
                    rutas[vecino] = rutas[nodo_actual] + [nodo_actual]
                    heapq.heappush(cola_prioridad, (distancia, vecino))
        
        return float('inf'), []
    
    def mostrar_camino_minimo(self, hospitalpartida, hospitalllegada):
        distancia, ruta = self.buscar_camino_minimo(hospitalpartida, hospitalllegada)
        
        print (f"La distancia mínima es {distancia} y el camino es {ruta}")