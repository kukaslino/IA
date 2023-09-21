# Função para ler o grafo a partir de um arquivo .txt
def load_graph_from_file(file_name):
    graph = {}
    locations = []

    with open(file_name, 'r') as file:
        num_locations = int(file.readline().strip())
        locations = file.readline().strip().split(',')

        for _ in range(num_locations):
            line = file.readline().strip().split(',')
            src = locations[_]
            graph[src] = []

            for i in range(num_locations):
                if i != _:
                    dest = locations[i]
                    distance = int(line[i])
                    graph[src].append((dest, distance))

    return graph, locations

# Função para encontrar todos os caminhos entre dois vértices em um grafo ponderado
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node[0] not in path:
            new_paths = find_all_paths(graph, node[0], end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Função para calcular o custo de um caminho
def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        src, dest = path[i], path[i + 1]
        for connection in graph[src]:
            if connection[0] == dest:
                cost += connection[1]
    return cost

# Ler o grafo a partir do arquivo N1.txt
graph, locations = load_graph_from_file('N1.txt')

# Vértice de origem é o primeiro nome da lista e o vértice de destino é o último nome da lista
start_location = locations[0]
end_location = locations[-1]

# Encontrar todos os caminhos entre os vértices de origem e destino
all_paths = find_all_paths(graph, start_location, end_location)

if not all_paths:
    print(f"Não existe caminho entre {start_location} e {end_location}.")
else:
    # Calcular o custo de cada caminho
    path_costs = [calculate_path_cost(graph, path) for path in all_paths]

    # Encontrar o caminho com o menor custo
    min_cost_index = path_costs.index(min(path_costs))
    shortest_path = all_paths[min_cost_index]

    # Imprimir o caminho mais curto e seu custo
    print(f"Caminho mais curto entre {start_location} e {end_location}:")
    print(shortest_path)
    print(f"Custo do caminho: {min(path_costs)}")
