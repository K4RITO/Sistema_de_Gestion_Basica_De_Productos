indice = 0

productos = []
producto = []

with open("base.txt", "r") as base:
    for linea in base:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre = partes[0]
            categoria = partes[1]
            try:
                precio = int(partes[2])
            except ValueError:
                precio = 0
            productos.append([nombre, categoria, precio])

def actualizar_base():
    with open("base.txt", "w") as base:
        for producto in productos:
            base.write(f"{producto[0]},{producto[1]},{producto[2]}\n")

operacion= int(input("¿que operacion desea realizar? \n 1=Agregar producto:  \n 2=Mostrar productos:  \n 3=Buscar producto:  \n 4=Eliminar producto:  \n 5=Salir: "))


while(operacion >= 1 and operacion <= 5):
    if(operacion == 1):
            producto = []
            producto.append((input("ingrese el nombre del producto: ")))
            producto[0] = producto[0].capitalize()
            producto.append(input("ingrese la categoria del producto: "))
            producto[1] = producto[1].capitalize()
            producto.append(int(input("ingrese el precio del producto: ")))
            productos.append(producto)
            actualizar_base()
            
    elif(operacion == 2):
        indice = 0
        for producto in productos:
            indice += 1
            nombre = producto[0]
            categoria = producto[1]
            precio = producto[2]
            print("===================================================")
            print(f"{indice}- Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
            
            
    elif(operacion == 3):
        buscador = input("Ingrese el producto que quiere buscar: ")
        buscador = buscador.capitalize()
        encontrar = False
        for producto in productos:
            if producto[0] == buscador:
                print("===================================================")
                print(f"Nombre del producto: {producto[0]}\nCategoria del producto: {producto[1]}\nPrecio del producto: ${producto[2]}")
                print("===================================================")
                encontrar = True                 
        if encontrar == False:
             print("No se encontraron coincidencias con ese producto.")

    elif(operacion == 4):
        borrar = input("Ingrese el indice del producto que quiere borrar: ")
        while True:
            if borrar.isdigit():
                borrar = int(borrar)
                borrar = borrar - 1
                del productos[borrar]
                actualizar_base()
                break
            else:
                print("Error: no ingreso un valor correcto.")
                borrar = input("Ingrese el indice del producto que quiere borrar: ")
             
    elif(operacion == 5):
         break
    operacion = int(input("\n¿Qué otra operación desea realizar?\n1=Agregar producto\n2=Mostrar productos\n3=Buscar producto\n4=Eliminar producto\n5=Salir "))