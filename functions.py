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

        numero_barras = sum(receita[i] for i in receita)

        return numero_barras