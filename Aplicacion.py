import sqlite3
conexion = sqlite3.connect("navarro_almacen.db")

menu = ("Menu opciones: \n 1. Registrar\n 2. Eliminar\n 3. Editar\n 4. Listar\n 5. Salir")

# En una cadena guardaremos el script de creacion de la tabla pais
tabla_producto = """CREATE TABLE producto(
                    idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo INTEGER,
                    nombre TEXT,
                    precio INTEGER
                    )
            """


cursor = conexion.cursor()
cursor.execute(tabla_producto)


while True:
    print("\n" + menu)
    opcion = input("Ingrese una opcion: ")
    print("Opcion incorrecta")




conexion.close()