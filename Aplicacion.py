import sqlite3

conexion = sqlite3.connect("navarro_almacen.db")
cursor = conexion.cursor()

menu = ("Menu opciones: \n 1. Registrar\n 2. Eliminar\n 3. Editar\n 4. Listar\n 5. Salir")

# En una cadena guardaremos el script de creacion de la tabla pais
"""tabla_producto = CREATE TABLE producto(
                    idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo INTEGER,
                    nombre TEXT,
                    precio INTEGER
                    )
"""


# ursor.execute(tabla_producto)



while True:
    print("\n" + menu)
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")

        cursor.execute("INSERT INTO producto (codigo, nombre, precio) VALUES (?, ?, ?)", (codigo, nombre, precio))
        conexion.commit()
        print("Producto registrado con éxito.")

    elif opcion == "2":
        print("Operacion no implementada")

    elif opcion == "3":
        print("Operacion no implementada")

    elif opcion == "4":
        cursor.execute("SELECT * FROM producto")
        productos = cursor.fetchall()
        print("\nID\tCodigo\t\tNombre\t\tPrecio\t")
        for producto in productos:
            print(f"{producto[0]}\t{producto[1]}\t\t{producto[2]}\t\t{producto[3]}")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción incorrecta")



conexion.close()