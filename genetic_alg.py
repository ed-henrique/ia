import sys
import time
import math
import random

PATH = './flights.txt'

pessoas = [
    ('Lisbon', 'LIS'),
    ('Madri', 'MAD'),
    ('Paris', 'CDG'),
    ('Dublin', 'DUB'),
    ('Brussels', 'BRU'),
    ('London', 'LHR'),
]

destino = 'FCO' # Roma

voos = {}

for line in open(PATH):
    v_origem, v_destino, h_partida, h_chegada, preco = line.split(',')
    voos.set((v_origem, v_destino), [])
    voos[(v_origem, v_destino)].append(h_partida, h_chegada, preco)

# Imprime indivíduo/cromossomo, que é um calendário para esse programa
def imprime_calendario(calendario):
    voo_id = -1
    preco_total = 0

    for i in range(len(calendario)//2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        
        voo_id += 1
        voo_ida = voos[origem, destino][calendario[voo_id]]
        preco_total += voo_ida[2]

        voo_id += 1
        voo_volta = voos[destino, origem][calendario[voo_id]]
        preco_total += voo_ida[2]
        print(f'{nome:<{10}}{origem:<{10}} {voo_ida[0]:<{5}}-{voo_ida[1]:<{5}} U${voo_ida[2]:<{3}} {voo_volta[0]:<{5}}-{voo_volta[1]:<{5}} U$ {voo_volta[2]:<{3}}')

    print(preco_total)

def tempo_para_minutos(hora):
    t = time.strptime(hora, '%H:%M')
    return t[3] * 60 + t[4]

# Calendário é o indivíduo/cromossomo
def funcao_avaliativa(calendario):
    preco_total = 0
    ultima_chegada = 0 # Primeiro horário do dia
    primeira_partida = tempo_para_minutos('23:59') # Último horário do dia
    voo_id = -1

    for i in range(len(calendario)//2):
        origem = pessoas[i][2]

        voo_id += 1
        voo_ida = voos[origem, destino][calendario[voo_id]]
  
        voo_id += 1
        voo_volta = voos[destino, origem][calendario[voo_id]]

        preco_total += voo_ida[2]
        preco_total += voo_volta[2]

        if ultima_chegada < tempo_para_minutos(voo_ida[1]):
            ultima_chegada = tempo_para_minutos(voo_ida[1])

        if primeira_partida < tempo_para_minutos(voo_volta[0]):
            primeira_partida = tempo_para_minutos(voo_volta[0])

    voo_id = -1
    espera_total = 0
    for i in range(calendario//2):
        origem = pessoas[i][1]
        
        voo_id += 1
        voo_ida = voos[origem, destino][calendario[voo_id]]
        
        voo_id += 1
        voo_volta = voos[destino, origem][calendario[voo_id]]

        espera_total += ultima_chegada - tempo_para_minutos(voo_ida[1])
        espera_total += tempo_para_minutos(voo_volta[0]) - primeira_partida

    return espera_total + preco_total

imprime_calendario([1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3])