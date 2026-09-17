import streamlit as st

# numero de blocos por pack
blocos_pack = 64

#funçao para calcular numero de packs + blocos extra

def calculo_packs(n_blocos):
    n_packs = n_blocos / blocos_pack
    n_packs_completos = int(n_packs)
    n_blocos_extra = (n_packs - n_packs_completos) * blocos_pack

    return f"Precisas de {n_packs_completos} packs e {int(n_blocos_extra)} blocos"

blocos = st.slider("Quantos blocos", min_value=0, max_value=10000)

st.write(calculo_packs(blocos))
    