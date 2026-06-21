import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='boolp1guq0ll73nmkpju-mysql.services.clever-cloud.com',
            user='uivryem8x5qu1939',
            password='WS57wOSCHfYNnvL758bk',
            database='boolp1guq0ll73nmkpju',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
