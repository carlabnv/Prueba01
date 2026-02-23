import streamlit as st
import numpy as np

st.title("Clase 3")

st.sidebar.image("python.png")
st.sidebar.title("Parámetros")

#st.image("python.png")

#valor = st.number_input("Ingrese un valor")

#lista = list(range(int(valor)))

#st.write(lista)

elementos = st.sidebar.slider("Ingrese la cantidad de elementos", 1 , 100 )

arreglo = np.arange(elementos)

st.write(arreglo)

st.write("Elaborado por:")