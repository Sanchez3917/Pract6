import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_productos():

    st.header("📦 Productos")

    con = obtener_conexion()
    cursor = con.cursor()

    # Insertar producto
    with st.form("form_producto"):
        nombre = st.text_input("Nombre producto")
        precio = st.number_input("Precio", min_value=0.0)

        guardar = st.form_submit_button("Guardar")

        if guardar:
            cursor.execute(
                "INSERT INTO Productos (Nombre, Precio) VALUES (%s,%s)",
                (nombre, precio)
            )
            con.commit()
            st.success("Producto guardado")

    # Mostrar productos
    cursor.execute("SELECT * FROM Productos")
    datos = cursor.fetchall()

    st.subheader("Listado de productos")
    st.dataframe(datos)

    cursor.close()
    con.close()
