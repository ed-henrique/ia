# Vizinhos de cada cidade e suas respectivas distâncias
adjacency_list = {
    'Arad'          : [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Bucharest'     : [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)],
    'Craiova'       : [('Pitesti', 138), ('Rimnicu Vicea', 146), ('Dobreta', 120)],
    'Dobreta'       : [('Craiova', 120), ('Mehadia', 75)],
    'Eforie'        : [('Hirsova', 86)],
    'Fagaras'       : [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu'       : [('Bucharest', 90)],
    'Hirsova'       : [('Eforie', 86), ('Urziceni', 98)],
    'Lugoj'         : [('Mehadia', 70), ('Timisoara', 111)],
    'Iasi'          : [('Neamt', 87), ('Vaslui', 92)],
    'Mehadia'       : [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt'         : [('Iasi', 87)],
    'Oradea'        : [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti'       : [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vicea', 97)],
    'Rimnicu Vicea' : [('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)],
    'Sibiu'         : [('Fagaras', 99), ('Rimnicu Vicea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara'     : [('Arad', 118), ('Lugoj', 111)],
    'Urziceni'      : [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui'        : [('Iasi', 92), ('Urziceni', 142)],
    'Zerind'        : [('Arad', 75), ('Oradea', 71)]
}

# Distâncias em linha reta de Bucareste à todas as cidades do mapa
heuristic = {
    'Arad':          366,
    'Bucharest':     0,
    'Craiova':       160,
    'Dobreta':       242,
    'Eforie':        161,
    'Fagaras':       178,
    'Giurgiu':       77,
    'Hirsova':       151,
    'Iasi':          226,
    'Lugoj':         244,
    'Mehadia':       241,
    'Neamt':         234,
    'Oradea':        380,
    'Pitesti':       98,
    'Rimnicu Vicea': 193,
    'Sibiu':         253,
    'Timisoara':     329,
    'Urziceni':      80,
    'Vaslui':        199,
    'Zerind':        374
}

# Obter vizinhos da cidade
def get_neighbors(v):
    return adjacency_list[v]

# Obter heurística da cidade específica (Sua distância em linha reta até Bucareste)
def h(n):
    return heuristic[n]

# Algoritmo A*
def a_star_algorithm():
    # Lista aberta para cidades onde os vizinhos ainda não foram visitados
    open_list = set(['Arad'])
    # Lista fechada para cidades onde os vizinhos já foram visitados
    closed_list = set([])

    # Guarda as distâncias da cidade inicial à todas as outras
    g = {}

    # Distância da cidade inicial à ela mesma é zero
    g['Arad'] = 0

    # Mapa de adjacência de todas as cidades
    parents = {}
    parents['Arad'] = 'Arad'

    while len(open_list) > 0:
        n = None

        # Procura a cidade com a menor pontuação na função de avaliação g(x) + h(x)
        for v in open_list:
            if n == None or g[v] + h(v) < g[n] + h(n):
                n = v;

        # Verifica se algum vizinho foi encontrado
        if n == None:
            print('Path does not exist!')
            return None

        # Verifica se o destino (Bucareste) já foi alcançado
        if n == 'Bucharest':
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append('Arad')

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path

        # Itera sobre os vizinhos das cidades e suas respectivas distâncias
        for (m, weight) in get_neighbors(n):
            # Se a cidade não estiver nem na lista aberta, nem na fechada, ela é adicionada à aberta
            # e a cidade atual é tomada como seu pai
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            # Em caso negativo, se o caminho mais curto for visitando a cidade atual, e em seguida a
            # cidade que se está iterando, as listas g e parents são atualizadas e a cidade vai para
            # a lista aberta
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # A cidade atual é removida da lista aberta e adicionada à lista fechada
        open_list.remove(n)
        closed_list.add(n)

    # Caso a lista aberta esteja vazia, não há cidades a serem exploradas e o destino não pode ser alcançado
    print('Path does not exist!')
    return None
    
# Execução do programa para achar uma rota ótima de Arad a Bucareste
a_star_algorithm()