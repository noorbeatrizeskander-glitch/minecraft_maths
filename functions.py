# numero de blocos por pack
from numpy.ma.core import divide

blocos_pack = 64
barras_bloco = 9
escada_bloco = 6

def calculo_packs(n_blocos):
    """
    Esta função calcula o numero de packs completos mais blocos extra, dado um numero total de
    blocos

    :param n_blocos: numero inteiro,
    :return: tuple em formato (numero de packs completos, numero de blocos extre)
    """

    # num pack é igual ao numero de blocos a dividir pelo numero de blocos por pack
    n_packs = n_blocos / blocos_pack
    # queremos o numero de packs completos, ou seja, a parte inteira da divisao
    n_packs_completos = int(n_packs)

    n_blocos_extra = (n_packs - n_packs_completos) * blocos_pack

    return (n_packs_completos, int(n_blocos_extra))

def calculo_barras(n_blocos):
    n_barras = n_blocos * barras_bloco

    return n_barras

def calculo_blocos_escadas(n_escadas):
    return n_escadas * escada_bloco


livro_de_receitas ={"armadura":
                        {"capacete":5,
                         "peitoral":8,
                         "calcas": 7,
                         "botas":4}
 }

def calcular_material(item, numero_items=1):
    if item in livro_de_receitas:
        receita = livro_de_receitas[item]

        numero_barras = sum(receita[i] for i in receita) * numero_items

        return numero_barras

lista_items = {"barreira": "barrier",
               "machado de diamante": "diamond_axe",
               "fogueira": "campfire",
               "fogueira das almas": "soul_campfire",
               "moldura": "item_frame",
               "moldura brilhante": "glow_item_frame",
               "prateleira": "shelf",
               "cascalho suspeito": "suspicious_gravel",
               "areia suspeita": "suspicious_sand",
               "cofre": "vault",
               "barco de acácia": "acacia_boat",
               "barco  de acácia com baú": "acacia_chest_boat",
               "jangada": "bamboo raft",
               "jangada com baú": "bamboo_chest_raft",
               "suporte de armaduras": "armor_stand",
               "barco de bétula": "birch:boat",
               "barco de bétula com báu": "birch_chest_boat",
               "almofada preta": "black_cushion"}

lista_efeitos = {"visão nocturna": "night_vision infinite",
                 "invisibilidade": "invisibility",
                 "velocidade": "speed infinite",
                 "super velocidade": "speed"}

def comando_minecraft(item):
    comando_items = "/give @s minecraft:"
    comando_efeitos = "/effect give @s minecraft:"

    if item in lista_items:
        commando = comando_items + lista_items[item]
    elif item in lista_efeitos:
        commando = comando_efeitos + lista_efeitos[item]
    else:
        return "Não conheeço esse comando"

    return commando

def calculadora(num1, num2, operacacao:str):
    if operacacao == "multiplicação":
        return round(num1 * num2, 4)
    elif operacacao == "divisão":
        return  round(num1 / num2,4)
    else:
        return None