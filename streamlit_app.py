import streamlit as st

from functions import (calculo_packs, calculo_barras, calcular_material, calculo_blocos_escadas,
                       comando_minecraft, calculadora)

st.title("Cálculo de packs de blocos para o minecraft")

col1, col2, col3 = st.columns(3)

with col1:
    blocos = st.slider("Quantos blocos no total", min_value=0, max_value=10000)

    packs = calculo_packs(blocos)
    barras = calculo_barras(blocos)

    st.write(f"Precisas de {packs[0]} packs e {packs[1]} blocos")
    st.write(f"Precisas de {barras} barras para fazer um total de {blocos} blocos ")

with col2:
    escadas = st.slider("Quantas escadas no total", min_value=0, max_value=64*10)
    st.write(f"Precisas de {calculo_blocos_escadas(escadas)} blocos para fazer um total "
             f"de {escadas} escadas ")

with col3:
    armaduras = st.slider("Quantas armaduras no total", min_value=0, max_value=64*10)
    st.write(f"Precisas de {calcular_material("armadura",armaduras)} blocos para fazer um total "
             f"de {armaduras} armaduras ")

st.subheader("Comandos")
item = st.text_input("Item ou efeito")
st.write(comando_minecraft(item))

st.subheader("Calculadora")
col4, col5, col6, col7, col8 = st.columns(5, vertical_alignment="bottom")
with col4:
    num_1 = st.number_input("1º Numero")
with col5:
    operation = st.radio("Operação", ["multiplicação", "divisão"])
with col6:
    num_2 = st.number_input("2º Numero")
with col7:
    st.write("=")
with col8:
    st.write(str(calculadora(num_1, num_2, operation)))