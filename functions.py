# numero de blocos por pack
blocos_pack = 64
barras_bloco = 9
escada_bloco = 6

def calculo_packs(n_blocos):
    n_packs = n_blocos / blocos_pack
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

lista_items = {"barreira": "barrier"}
lista_efeitos = {"visão nocturna": "night_vision"}

def comando_minecraft(item):
    comando_items = "/give @s minecraft:"
    comando_efeitos = "/effect @s minecraft:"

    if item in lista_items:
        commando = comando_items + lista_items[item]
    elif item in lista_efeitos:
        commando = comando_efeitos + lista_efeitos[item]
    else:
        return

    return commando