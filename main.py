import os
from data_stark import lista_personajes
from funciones import *

lista_heroes = []
flag_lista = False

while True:
    os.system("cls")
    print("------------------------------------------------------------")
    match(menu()):
        case "1":
            cargar_lista(lista_heroes, lista_personajes)
            flag_lista = True
        case "2":
            if flag_lista:
                nombres(lista_heroes, "nombre")
            else:
                print("Primero cargue la lista...")
        case "3":
            if flag_lista:
                nombres_con_alturas(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "4":
            if flag_lista:
                mayor_altura(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "5":
            if flag_lista:
                menor_altura(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "6":
            if flag_lista:
                promedio_altura(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "7":
            if flag_lista:
                mas_pesado(lista_heroes)
                menos_pesado(lista_heroes)
            else:
                print("Primero cargue la lista...")
        case "s":
            salir = input("Confirma salida? s/n: ").lower().strip()
            if salir == "s":
                break
        case "0":
            no_se = input("Esta seguro que quiere entrar a STARK 01? s/n: ").lower().strip()
            if no_se == "s":
                input("Bienvenido a STARK 01...")
                while True:
                    os.system("cls")
                    print("------------------------------------------------------------")
                    match(menu_stark01()):
                        case "s":
                            salir = input("Confirma salida? s/n: ").lower().strip()
                            if salir == "s":
                                break
                        case "1":
                            if not flag_lista:
                                cargar_lista(lista_heroes, lista_personajes)
                                flag_lista = True
                            else:
                                print("La lista ya esta cargada...")
                        case "2":
                            if flag_lista:
                                mostrar_nombres_por_genero(lista_heroes, "genero", "M", "nombre")
                            else:
                                print("Primero cargue la lista...")
                        case "3":
                            if flag_lista:
                                mostrar_nombres_por_genero(lista_heroes, "genero","F", "nombre")
                            else:
                                print("Primero cargue la lista...")
                        case "4":
                            if flag_lista:
                                mayor_altura_por_genero(lista_heroes, "genero", "M")
                            else:
                                print("Primero cargue la lista...")
                        case "5":
                            if flag_lista:
                                mayor_altura_por_genero(lista_heroes, "genero", "F")
                            else:
                                print("Primero cargue la lista...")
                        case "6":
                            if flag_lista:
                                promedio_altura_por_genero(lista_heroes, "genero", "M")
                            else:
                                print("Primero cargue la lista...")
                        case "7":
                            if flag_lista:
                                promedio_altura_por_genero(lista_heroes, "genero", "F")
                            else:
                                print("Primero cargue la lista...")
                        case "8":
                            if flag_lista:
                                determinar_cantidad_tipos(lista_heroes, "color_ojos")
                            else:
                                print("Primero cargue la lista...")
                        case "9":
                            if flag_lista:
                                determinar_cantidad_tipos(lista_heroes, "color_pelo")
                            else:
                                print("Primero cargue la lista...")
                        case "10":
                            if flag_lista:
                                determinar_cantidad_tipos(lista_heroes, "inteligencia")
                            else:
                                print("Primero cargue la lista...")
                        case "11":
                            if flag_lista:
                                listar_superheores_tipo(lista_heroes, "color_ojos", "nombre")
                            else:
                                print("Primero cargue la lista...")
                        case "12":
                            if flag_lista:
                                listar_superheores_tipo(lista_heroes, "color_pelo", "nombre")
                            else:
                                print("Primero cargue la lista...")
                        case "13":
                            if flag_lista:
                                listar_superheores_tipo(lista_heroes, "inteligencia", "nombre")
                            else:
                                print("Primero cargue la lista...")
                
                
                    os.system("pause")
    

    input("Presione enter para continuar...")
