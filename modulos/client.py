import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_clientes():

    st.header("👤 Clientes")

    con = obtener_conexion()
    cursor = con.cursor()

    # Insertar cliente
    with st.form("form_cliente"):
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo")

        guardar = st.form_submit_button("Guardar")

        if guardar:
            cursor.execute(
                "INSERT INTO Clientes (Nombre, Correo) VALUES (%s,%s)",
                (nombre, correo)
            )
            con.commit()
            st.success("Cliente guardado")

    # Mostrar clientes
    cursor.execute("SELECT * FROM Clientes")
    datos = cursor.fetchall()

    st.subheader("Listado de clientes")
    st.dataframe(datos)

    cursor.close()
    con.close()
