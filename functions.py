# numero de blocos por pack
blocos_pack = 64
barras_bloco = 9

def calculo_packs(n_blocos):
    n_packs = n_blocos / blocos_pack
    n_packs_completos = int(n_packs)
    n_blocos_extra = (n_packs - n_packs_completos) * blocos_pack

    return (n_packs_completos, int(n_blocos_extra))

def calculo_barras(n_blocos):
    n_barras = n_blocos * barras_bloco

    return n_barras