import time
import random

# define os dados do problema da mochila 0-1
itens = [
    {"peso": 3,  "valor": 266},
    {"peso": 13, "valor": 442},
    {"peso": 10, "valor": 671},
    {"peso": 9,  "valor": 526},
    {"peso": 7,  "valor": 388},
    {"peso": 1,  "valor": 245},
    {"peso": 8,  "valor": 210},
    {"peso": 8,  "valor": 145},
    {"peso": 2,  "valor": 126},
    {"peso": 9,  "valor": 322},
]

limite_peso = 35

# define o tamanho da população, o número máximo de gerações e as probabilidades de crossover e mutação
POPULATION_SIZE = 1000
MAX_GENERATIONS = 1000
CROSSOVER_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.5

# define a função de fitness
def fitness(individual):
    peso_total = sum([itens[i]["peso"] for i in range(len(individual)) if individual[i] == 1])
    if peso_total > limite_peso:
        return 0
    else:
        return sum([itens[i]["valor"] for i in range(len(individual)) if individual[i] == 1])

# define a seleção por roleta
def selection(population):
    total_fitness = sum([fitness(p) for p in population])
    relative_fitness = [fitness(p) / total_fitness for p in population]
    cum_relative_fitness = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]
    selected = []
    for i in range(len(population)):
        r = random.random()
        for j in range(len(cum_relative_fitness)):
            if r < cum_relative_fitness[j]:
                selected.append(population[j])
                break
    return selected

# define o crossover de um ponto
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_PROBABILITY:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    else:
        return parent1, parent2

# define a mutação de um gene
def mutation(individual):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < MUTATION_PROBABILITY:
            mutated_individual[i] = 1 - mutated_individual[i]
    return mutated_individual

# inicializa a população aleatoriamente
population = [[random.randint(0, 1) for i in range(len(itens))] for j in range(POPULATION_SIZE)]
new_generation = []

# roda o algoritmo genético
for generation in range(MAX_GENERATIONS):
    # seleciona os pais
    parents = selection(population)
    # gera os filhos por crossover
    children = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        child1, child2 = crossover(parent1, parent2)
        children.append(child1)
        children.append(child2)
    # faz a mutação nos filhos
    mutated_children = [mutation(child) for child in children]
    # avalia a nova geração
    new_generation = parents + mutated_children
    new_generation = sorted(new_generation, key=fitness, reverse=True)[:POPULATION_SIZE]
    # checa se a solução foi encontrada
    print(f'Generation: {generation} | {fitness(new_generation[0])}', end="\r")
    time.sleep(1)
    # atualiza a população
    population = new_generation

if fitness(new_generation[0]) > 0:
    print("Solução encontrada após", MAX_GENERATIONS+1, "gerações.")
    print([i+1 for i in range(len(new_generation[0])) if new_generation[0][i] == 1])
else:
    print("Não foi possível encontrar uma solução.")
