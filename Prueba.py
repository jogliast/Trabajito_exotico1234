from Grafo import GrafoListaConPesos

# Crear el grafo
grafo1 = GrafoListaConPesos()

# Adicionar vértices
grafo1.adicionarVertice("Barranquilla")
grafo1.adicionarVertice("Bogota")
grafo1.adicionarVertice("Medellin")

# Adicionar arcos
grafo1.adicionarArco("Barranquilla", "Bogota", 20)
grafo1.adicionarArco("Barranquilla", "Medellin", 240)
grafo1.adicionarArco("Bogota", "Medellin", 80)

# Imprimir el grafo
print("El grafo es:\n", grafo1, sep="")

# Imprimir el recorrido BFS desde 'Barranquilla'
print("Recorrido en anchura (BFS) desde Barranquilla:", grafo1.recorrerAnchura("Barranquilla"))

# Calcular e imprimir el camino más corto desde 'Barranquilla' hasta 'Bogota'
camino, distancia = grafo1.caminoMasCorto("Barranquilla", "Bogota")
print("\nEl camino más corto de Barranquilla a Bogota es:", camino)
print("La distancia más corta es:", distancia)

# Calcular e imprimir el camino más corto desde 'Barranquilla' hasta 'Medellin'
camino, distancia = grafo1.caminoMasCorto("Barranquilla", "Medellin")
print("\nEl camino más corto de Barranquilla a Medellin es:", camino)
print("La distancia más corta es:", distancia)
