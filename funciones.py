

def nombres(lista:list, key:str):
    for heroe in lista:
        print(f"Nombre: {heroe[key]}")
        print("------------------------")

def nombres_con_alturas(lista:list):
    for heroe in lista:
        print(f"Nombre: {heroe['nombre']}")
        print(f"Altura: {float(heroe['altura']):.2f}")
        print("------------------------")

def mayor_altura(lista:list):
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["altura"]) > max_altura:
            bandera = False
            max_altura = float(heroe["altura"])
            nombre_max_altura = heroe["nombre"]

    for heroe in lista:
        if heroe["altura"] == max_altura:
            print(heroe)
    
    print(f"El heroe mas alto es: {nombre_max_altura} {max_altura:5.2f}")
    print("------------------------------------------------------------")

# mayor_altura()

def menor_altura(lista:list):
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["altura"]) < men_altura:
            bandera = False
            men_altura = float(heroe["altura"])
            nombre_men_altura = heroe["nombre"]

    for heroe in lista:
        if heroe["altura"] == men_altura:
            print(heroe)
    
    print(f"El heroe mas bajo es: {nombre_men_altura} {men_altura:5.2f}")
    print("------------------------------------------------------------")

# menor_altura()

def promedio_altura(lista:list):
    total_altura = 0
    cant_heroes = len(lista)

    for superheroe in lista:
        total_altura += float(superheroe["altura"])

    prom_altura = total_altura / cant_heroes

    print("La altura promedio de los superheroes es: {}".format(prom_altura))
    print("------------------------------------------------------------")

def menos_pesado(lista:list):
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["peso"]) < menos_pesado:
            bandera = False
            menos_pesado = float(heroe["peso"])
            nombre_menos_pesado = heroe["nombre"]

    for heroe in lista:
        if heroe["peso"] == menos_pesado:
            print(heroe)
    
    print(f"El heroe menos pesado es: {nombre_menos_pesado} {menos_pesado:5.2f}")
    print("------------------------------------------------------------")

# menos_pesado()

def mas_pesado(lista:list):
    bandera = True
    for heroe in lista:
        if bandera or float(heroe["peso"]) > mas_pesado:
            bandera = False
            mas_pesado = float(heroe["peso"])
            nombre_mas_pesado = heroe["nombre"]

    for heroe in lista:
        if heroe["peso"] == mas_pesado:
            print(heroe)
    
    print(f"El heroe mas pesado es: {nombre_mas_pesado} {mas_pesado:5.2f}")
    print("------------------------------------------------------------")

# mas_pesado()

def menu():
    print("      *** Menu de Opciones ***   ")
    print("------------------------------------------------------------")
    print("  1- Cargar lista")
    print("  2- Mostrar nombres")
    print("  3- Mostrar nombres y alturas")
    print("  4- Mostrar el superheroe mas alto")
    print("  5- Mostrar el superheroe mas bajo")
    print("  6- Mostrar la altura promedio")
    print("  7- Mostrar el superheroe mas y menos pesado")
    print("  0- STARK 01")
    print("  s- salir")
    opcion = input("Ingrese opcion: ").lower().strip()
    print("------------------------------------------------------------")
    return opcion

# menu()

def cargar_lista(lista_destino:list, lista_origen:list):
    for item in lista_origen:
        lista_destino.append(item)
    print("Se cargo la lista con exito...")
    print("------------------------------------------------------------")

# cargar_lista()

def menu_stark01():
    print("  *** STARK 01 ***  ")
    print("------------------------------------------------------------")
    print("  1- cargar lista")
    print("  2- mostrar heroes masculinos")
    print("  3- mostrar heroes femeninos")
    print("  4- mostrar heroe masculino mas alto")
    print("  5- mostrar heroe femenino mas alto")
    print("  6- mostrar el promedio de altura del genero masculino")
    print("  7- mostrar el promedio de altura del genero femenino")
    print("  8- Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("  9- Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("  10- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print("  11- Listar todos los superhéroes agrupados por color de ojos.")
    print("  12- Listar todos los superhéroes agrupados por color de pelo.")
    print("  13- Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("  s- salir")
    opcion = input("Ingrese opcion: ").lower().strip()
    print("------------------------------------------------------------")
    return opcion

def mostrar_nombres_por_genero(lista:list, key:str, key2:str, key3:str):
    for item in lista:
        if item[key] == key2:
            print("Nombre: {}".format(item[key3]))
            print("------------------------------------------------------------")

# mostrar_nombres_por_genero()

def mayor_altura_por_genero(lista:list, key:str, key2:str):
    bandera = True
    for heroe in lista:
        if heroe[key] == key2:
            if bandera or float(heroe["altura"]) > mas_altura:
                bandera = False
                mas_altura = float(heroe["altura"])
                nombre_mas_altura = heroe["nombre"]

    for heroe in lista:
        if heroe["altura"] == mas_altura:
            print(heroe)
    
    print(f"El heroe mas alto es: {nombre_mas_altura} {mas_altura:5.2f}")
    print("------------------------------------------------------------")

def promedio_altura_por_genero(lista:list, key:str, key2:str):
    total_altura = 0
    cant_heroes = len(lista)
    for superheroe in lista:
        if superheroe[key] == key2:
            total_altura += float(superheroe["altura"])

    prom_altura = total_altura / cant_heroes

    print("La altura promedio de los superheroes es: {}".format(prom_altura))
    print("------------------------------------------------------------")

def determinar_cantidad_tipos(lista:list, key:str):
    lista_aux = []
    for i in lista:
        if i[key] == "":
            lista_aux.append("No tiene")
        else:
            lista_aux.append(i[key])

    cuenta_tipos = {}
    for elemento in lista_aux:
        if elemento in cuenta_tipos:
            cuenta_tipos[elemento] += 1
        else:
            cuenta_tipos[elemento] = 1
    for tipo, cantidad in cuenta_tipos.items():
        print(f"Tipo {tipo}, Cantidad: {cantidad}")

def listar_superheores_tipo(list: list, key: str, key_nombre: str):
    lista_aux = []
    for i in list:
        if i[key] == "":
            lista_aux.append("No tiene")
        else:
            lista_aux.append(i[key])

    dict_aux = {}
    for i in range(len(lista_aux)):
        tipo = lista_aux[i]
        nombre = list[i][key_nombre]
        if tipo in dict_aux:
            dict_aux[tipo].append(nombre)
        else:
            dict_aux[tipo] = [nombre]
    
    for tipo, nombres in dict_aux.items():
        print(f"Tipo {tipo}: {', '.join(nombres)}")






# print(cuantos_heroes_tienen_mismo_color_ojos(lista_personajes, 'color_pelo'))
