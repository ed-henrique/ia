import random

# define the size of the board and the population size
N = 11
POPULATION_SIZE = 1000
ELITISM_SIZE = 20
MUTATION_RATE = 0.2

# define the fitness function
def fitness(individual):
    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if individual[i] == individual[j]:
                conflicts += 1
            offset = j - i
            if individual[i] == individual[j] - offset or individual[i] == individual[j] + offset:
                conflicts += 1
    return 1 / (conflicts + 1)

# define the selection function
def selection(population):
    return random.choices(population, weights=[fitness(p) for p in population], k=2)

# define the crossover function
def crossover(parent1, parent2):
    child1 = [0] * N
    child2 = [0] * N
    for i in range(N):
        if random.random() < 0.5:
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        else:
            child1[i] = parent2[i]
            child2[i] = parent1[i]
    return child1, child2

# define the mutation function
def mutation(individual):
    mutated_individual = list(individual)
    for i in range(N):
        if random.random() < MUTATION_RATE:
            mutated_individual[i] = random.randint(1, N)
    return mutated_individual

# initialize the population
population = [[random.randint(1, N) for i in range(N)] for j in range(POPULATION_SIZE)]

# run the genetic algorithm
for generation in range(10000):
    # select the best individuals to survive
    population = sorted(population, key=fitness, reverse=True)[:POPULATION_SIZE-ELITISM_SIZE]
    elites = sorted(population, key=fitness, reverse=True)[:ELITISM_SIZE]
    # add the elites to the next generation
    next_generation = elites
    # breed the rest of the population
    while len(next_generation) < POPULATION_SIZE:
        parent1, parent2 = selection(population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        next_generation.append(child1)
        next_generation.append(child2)
    # update the population
    population = next_generation
    # check if a solution has been found
    if fitness(population[0]) == 1:
        print("Solution found after", generation, "generations.")
        print(population[0])
        break
