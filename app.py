import streamlit as st

from modulos.venta import mostrar_venta
from modulos.clientes import mostrar_clientes
from modulos.productos import mostrar_productos
from modulos.login import login

if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:

    opciones = ["Ventas", "Clientes", "Productos"]

    seleccion = st.sidebar.selectbox(
        "Selecciona una opción",
        opciones
    )

    if seleccion == "Ventas":
        mostrar_venta()

    elif seleccion == "Clientes":
        mostrar_clientes()

    elif seleccion == "Productos":
        mostrar_productos()

else:
    login()
