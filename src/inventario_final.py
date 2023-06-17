import time
from datetime import datetime 


def leerInventario():
# Esta funcion escribe los producto en una lista "Invent"
    archivo = open('inventario.txt', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    invent = []
    
    for linea in lineas:
        invent.append(linea[:len(linea)-1].split('----@----'))
    
    for i in range(len(invent)):
        invent[i][1] = float(invent[i][1])
        invent[i][2] = int(invent[i][2])
        
    return invent

def leerVentasxVendedor():
# Esta funcion escribe los producto en una lista "ventasVendedores"
    archivo = open('ventasxvendedor.txt', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    ventasVendedores = []
    
    for linea in lineas:
        ventasVendedores.append(linea[:len(linea)-1].split('--@--'))
    
    for i in range(len(ventasVendedores)):
        ventasVendedores[i][1] = int(ventasVendedores[i][1])
        ventasVendedores[i][2] = float(ventasVendedores[i][2])
        
    return ventasVendedores

def leerVentas():
# Esta funcion escribe los producto en una lista "ventas"
    archivo = open('ventas.txt', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    ventas = []
    
    for linea in lineas:
        ventas.append(linea[:len(linea)-1].split('--@--'))
    
    for i in range(len(ventas)):
        ventas[i][3] = int(ventas[i][3])
        ventas[i][4] = float(ventas[i][4])
        
    return ventas

def indice():
# Esta funcion maneja todo el indice de opciones
    print('\n','Tu inventario APP'.center(40, '-'))
    print('''
Bienvenido a tu herramienta de inventario. \n¿Qué deseas hacer?\n
a) Consultar el inventario (Producto/Cantidad)
b) Hacer una venta
c) Registrar producto
d) Consultar Datos de Ventas
e) Reporte de venta por vendedor
''')

    while True: 
    
        inciso = input('Inserte el inciso de la acción que quieres realizar: ')

        if inciso.isalpha():
            if inciso.upper() == 'A': 
                Inventario(inventario)
                time.sleep(1)
                regresar()
                
            elif inciso.upper() == 'B':
                Venta(inventario, ventxven, ventas)
                time.sleep(1)
                regresar()
                
            elif inciso.upper() == 'C':
                RegistrarProducto(inventario)
                time.sleep(1)
                regresar()
            
            elif inciso.upper() == 'D':
                DataVentas(ventas)
                time.sleep(1)
                regresar()
            
            elif inciso.upper() == 'E':
                DataVende(ventxven, ventas)
                time.sleep(1)
                regresar()
                
            else:
                print("\nInserte una letra válida\n")
        else:
            
            print('\nIntente con un caracter válido\n')

def regresar():
# Esta funcion pregunta al usuario si quiere realizar otra accion, en caso contrario actualiza el .txt y cierra el programa
    print('\n\nSi tecleas "s" regresas al inicio, si tecleas "n" se cierra el programa \nSi cierras el programa, el inventario se actualiza automáticamente')
    while True:  
        opcion = input('\n¿Deseas regresar al inicio? (s/n) : ')
        if opcion.isalpha():
            if opcion.upper() == 'S':
                indice()
                break
            
            elif opcion.upper() == 'N':
                EscribeArchivo(inventario,ventxven,ventas)
                exit()
            
            else:
                print('Introduce una letra válida')
                continue
        else:
            print('Introduce una letra')

def Inventario(inv):
# Esta funcion lee e imprime el inventario para el usuario mostrando disponibles y agotados
    print('\n' + ' Articulos en el inventario(Cantidad) '.center(40, '=') + '\n')
    
    agotados = []
    
    for i in range(len(inv)):
        if inv[i][2] == 0:
            agotados.append(inv[i])
        else:   
            print(inv[i][0].ljust(25, '.') + str(inv[i][2]).rjust(15, ' '))
            
    print('\n' + ' Articulos en el inventario(Agotados) '.center(40, '=') + '\n')        
    for i in range(len(agotados)):
        print(agotados[i][0].ljust(25, '.') + str(agotados[i][2]).rjust(15, ' '))

def EscribeArchivo(inv,vxv,vent):
# Esta funcion actualiza el archivo .txt
    for i in range(len(inv)):
        inv[i][1] = str(inv[i][1])
        inv[i][2] = str(inv[i][2])
        
    archivo = open('inventario.txt', 'w')
    
    for reg in inv:
        archivo.write('----@----'.join(reg) + '\n')
    archivo.close()
    
    for i in range(len(vxv)):
        vxv[i][1] = str(vxv[i][1])
        vxv[i][2] = str(vxv[i][2])
    
    archivo = open('ventasxvendedor.txt', 'w')
    
    for reg in vxv:
        archivo.write('--@--'.join(reg) + '\n')
    archivo.close()
    
    for i in range(len(vent)):
        vent[i][0] = str(vent[i][0])
        vent[i][3] = str(vent[i][3])
        vent[i][4] = str(vent[i][4])
    
    archivo = open('Ventas.txt', 'w')
    
    for reg in vent:
        archivo.write('--@--'.join(reg) + '\n')
    archivo.close()

def Venta(inv, vxv, ventas):
# Esta funcion registra las ventas y las asigna a al/a la vendedor/a correspondiente
    print('\n' + ' Ventas '.center(40, '=') + '\n')
    
    print('¿Quién realiza la venta?\n')
    
    for i in range(len(vxv)):
        print(i+1, '\t', vxv[i][0])
        
    while True:
        num_vendedor = input('\nInserta el número correspondiente al/a la actual vendedor/a: ')
        
        if num_vendedor.isnumeric():
            if int(num_vendedor) > 0 and int(num_vendedor) <= len(vxv):
                vendedor = vxv[int(num_vendedor)-1][0]
                break
            else:
                print('Introduce un número válido')
        else:
            print('Introduce un número')
     
    print('\n¿Qué articulo se venderá?\n')
    
    for i in range(len(inv)):
        print(i+1, '\t', inv[i][0])
    
    while True:
        num_producto = input('\nSelecciona el producto a vender: ')
        
        if num_producto.isnumeric():
            if int(num_producto) > 0 and int(num_producto) <= len(inv):
                if inv[int(num_producto)-1][2] > 0:
                    producto = inv[int(num_producto)-1][0]
                    break
   
                else:
                    print('\nEse producto esta agotado')
                       
                    while True:
                        n_opcion = input('Teclea "s" si deseas seleccionar otro articulo o teclea "n" si quieres regresar al menú:')
                        if n_opcion.isalpha():
                            if n_opcion.upper() == 'S':
                                break
                            elif n_opcion.upper() == 'N':
                                indice()
                            else:
                                print('Escoge una letra válica')          
                        else:
                            print('Inserta una letra')
            else:
                print('Introduce un número válido')
        else:
            print('Introduce un número')
    
    while True:
        
        print('Inserta la cantidad de', producto, 'a vender: ', end='')
        cantidad = input()
        
        if cantidad.isnumeric():
            if int(cantidad) > 0:
                if int(cantidad) <= inv[int(num_producto)-1][2]:
                    costo = int(cantidad)*inv[int(num_producto)-1][1]
                    break
                else:
                    print('Solo hay', inv[int(num_producto)-1][2], producto, 'disponible/s. Inserte una cantidad válida')
            else:
                print('Inserte una cantidad mayor a 0')
        else:
            print('Inserte un número')
    
    print('\nTOTAL A PAGAR: ', costo)
    
    inv[int(num_producto)-1][2] -= int(cantidad)
    vxv[int(num_vendedor)-1][1] += 1
    vxv[int(num_vendedor)-1][2] += costo
    
    fecha = datetime.now()
    str_fecha = fecha.strftime("%d/%m/%Y %H:%M:%S")
    
    regVenta = [str_fecha,vendedor,producto,cantidad,costo]
    
    ventas.append(regVenta)
    
def RegistrarProducto(inv):
    # Esta funcion registra productos entrantes nuevos o existentes
    print('\n' + ' Registro de productos '.center(40, '=') + '\n')
    
    print('¿Quieres registrar un nuevo producto o registrar sobre un producto existente?\n')
    print('Ingresa "n" para un nuevo producto o "e" para un producto existente. \n')
    
    while True:
        opcion = input('Ingresa tu opción: ')
    
        if opcion.isalpha():
            if opcion.upper() == 'E':
                print('\n' + ' Inventario Actual '.center(40, '=') + '\n')
                for i in range(len(inv)):
                    print(i+1, '\t', inv[i][0])
    
                while True:
                    num_producto = input('\nSelecciona el producto a registrar: ')
                    
                    if num_producto.isnumeric():
                        
                        if int(num_producto) > 0 and int(num_producto) <= len(inv):
                            while True:
                                cant_ag = input('¿Cuántas unidades vas a agregar?: ')
                            
                                if cant_ag.isnumeric():
                                    if int(cant_ag) >= 0:
                                        inv[int(num_producto)-1][2] += int(cant_ag)
                                        break
                                    else:
                                        print('Ingresa un número válido')
                                else:
                                    print('Ingrese un número, número entero o número positivo')
                            break  
                        else:
                            print('Ingresa un número válido')
                    
                    else:
                        print('Ingresa un número')
                break
            
            elif opcion.upper() == 'N':
                producto = input('Inserta el nombre del producto: ')
                
                while True:
                    precio = input('Inserta el precio del producto: ')
                    if precio.isalpha() or float(precio) <= 0:
                        print('El precio debe ser numérico o positivo.')
                    else:
                        precio = float(precio)
                        break
                
                while True:
                    cant = input('Inserte la cantidad del nuevo producto: ')
                    if cant.isnumeric():
                            cant = int(cant)
                            break
                    else:
                        print('Ingrese un número, número entero o número positivo')
                
                marca = input('Ingrese marca del producto: ')
                
                nuevoProducto = [producto.upper(), precio, cant, marca.upper()]
                inv.append(nuevoProducto)
                
                break
            
            else:
                print('Ingresa una letra válida')
        else:
            print('Ingresa una letra')
    
def DataVentas(vent):
    # Esta funcion muestra al usuario las ventas
    print('\n' + ' Consulta de Datos de Ventas '.center(40, '=') + '\n')

    print('Fecha'.ljust(28, ' ') + 'Vendedor/a'.ljust(20, ' ') + 'Producto'.ljust(24, ' ') + 'Cantidad'.ljust(19, ' ') + 'Precio Total (MXN)'.rjust(8, ' '))
    print('---'.center(110,'-'))
    total_venta = 0
    for venta in range(len(vent)):
        print(vent[venta][0].ljust(28, ' ') + str(vent[venta][1]).ljust(20, ' ') + str(vent[venta][2]).ljust(31, ' ') + str(vent[venta][3]).ljust(19, ' ') + '$' + str(round(vent[venta][4],2)).rjust(9, ' '))
        total_venta += vent[venta][4]
    print('\n' + 'Venta total de la tienda (MXN)'.center(40,'='))
    print('La tienda hizo una venta total equivalente a: ' + '$' + str(round(total_venta,2)))
    
def DataVende(vxv, ventas):
# Esta funcion muestra las ventas individuales por vendedor/a
    print('\n' + ' Consulta de Datos de Ventas por Vendedor '.center(60, '=') + '\n')
    
    print('¿De quién deseas consultar las ventas?\n')
    
    for i in range(len(vxv)):
        print(i+1, '\t', vxv[i][0])
    
    while True:
        num_vendedor = input('\nInserta el número correspondiente al/a la actual vendedor/a: ')
        
        if num_vendedor.isnumeric():
            if int(num_vendedor) > 0 and int(num_vendedor) <= len(vxv):
                vendedor = vxv[int(num_vendedor)-1][0]
                break
            else:
                print('Introduce un número válido')
        else:
            print('Introduce un número')
    
    ventasVend = []
    
    for x in range(len(ventas)):
        v = ventas[x][1]
        if v == vendedor:
            ventasVend.append(ventas[x])
            
    for y in range(len(vxv)):
        if vendedor in vxv[y]:
            total_ventas = vxv[y][1]
            total_costo = vxv[y][2]

    if ventasVend == []:
        print(vendedor, 'no ha realizado ninguna venta')
        
    else:
        vende = ' ' + vendedor + ' '
        print('\n' + vende.center(110,'='))
        print('Fecha'.ljust(28, ' ') + 'Vendedor/a'.ljust(20, ' ') + 'Producto'.ljust(24, ' ') + 'Cantidad'.ljust(19, ' ') + 'Precio Total (MXN)'.rjust(8, ' '))
        print('---'.center(110,'-'))
    
        for venta in range(len(ventasVend)):
           print(ventasVend[venta][0].ljust(28, ' ') + str(ventasVend[venta][1]).ljust(20, ' ') + str(ventasVend[venta][2]).ljust(31, ' ') + str(ventasVend[venta][3]).ljust(19, ' ') + '$' + str(round(ventasVend[venta][4],2)).rjust(9, ' '))
        
        print('\n' + 'Total'.center(40,'='))
        print(vendedor, 'hizo un total de', total_ventas, 'ventas, con un monto total de', round(total_costo,2))
        
inventario = leerInventario()
ventxven = leerVentasxVendedor()
ventas = leerVentas()
indice()

# Esto
# Es
# Para
# Completar
# 400
# Lineas