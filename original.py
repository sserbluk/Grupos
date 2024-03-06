#abro un archivo csv para trabajar
import csv
import os
import sys
import time
import datetime
import numpy as np
import pandas as pd
import smtplib, ssl
import getpass
def menu():
    os.system('cls')
    print("Menu")
    print("1. Cargar archivo")
    print("2. Listar datos")
    print("3. crear grupos")
    print("4. Listar por grupos")
    print("5. enviar correo")
    print("6. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion
def cargar_archivo(lista_p):
    os.system('cls')
    print("Cargar archivo")
    print("1. Cargar archivo")
    print("2. Regresar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        #creo un diccionario con los archivos csv de la carpeta csv clave orden y valor nombre del archivo, y los muestro
        diccionario = {}
        orden = 1
        for file in os.listdir("./csv"):
            diccionario[orden] = file
            orden += 1
        #muestro el diccionario
        for clave,valor in diccionario.items():
            print(clave,valor)
        #pido el numero de archivo
        numero_archivo = int(input("Ingrese el numero de archivo: "))
        global nombre_archivo
        #verifico que el numero de archivo exista
        if numero_archivo in diccionario:
            nombre_archivo = diccionario[numero_archivo]
        else:
            print("Numero de archivo no valido")
            time.sleep(2)
            return None
        #abro el archivo
        try:
            archivo = open("./csv/"+nombre_archivo, encoding="utf-8")
            #leo el archivo
            data = csv.reader(archivo, delimiter=',' )
        except:
            print(f"El archivo {nombre_archivo} no existe")
            time.sleep(2)
            return None

        
        #recorro el archivo y lo guardo en la lista, creando una lista interna por cada fila
        for row in data:
            lista_p.append(row)
        #cierro el archivo
        archivo.close()
        return lista_p
    elif opcion == 2:
        return None
    else:
        print("Opcion no valida")
        time.sleep(2)
        return None
def listar_datos(lista_p):
    os.system('cls')
    print("Listar datos")
    print("1. Listar datos")
    print("2. Regresar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        #recorro la lista
        for i in range(len(lista_p)):
            #recorro la lista interna
            for j in range(len(lista_p[i])):
                print(lista_p[i][j], end="\t")
            print()
        input("Presione una tecla para continuar...")
    elif opcion == 2:
        return None
    else:
        print("Opcion no valida")
        time.sleep(2)
        return None
def crear_grupos(lista_p):
    os.system('cls')
    print("Crear grupos")
    print("1. Crear grupos")
    print("2. Regresar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        #aca creo los grupos
        print("Creando grupos...")
        #Cuento la cantidad de filas divido 4 y redondeo para arriba
        cantidad = int(np.ceil(len(lista_p)/4))
        #creo una lista de grupos
        grupos = []
        for i in range(1,cantidad+1):
            grupos.append([f"grupo {i}",0])
        #asigno a cada estudiante un numero de grupo al azar, entre 1 y la cantidad de grupos, cuidando no supere 4 estudiantes por grupo
        for i in range(len(lista_p)):
            #obtengo un numero de grupo al azar
            grupo = np.random.randint(1,cantidad+1)
            #verifico que el grupo no tenga 4 estudiantes
            while grupos[grupo-1][1] == 4:
                grupo = np.random.randint(1,cantidad+1)
            #agrego el estudiante al grupo
            grupos[grupo-1][1] += 1

            #agrego el numero de grupo a la lista principal
            lista_p[i].append(grupo)
            #lista_p[i].append(np.random.randint(1,cantidad+1))
        print("Grupos creados con exito")
        input("Presione una tecla para continuar...")
        #guardo los cambios en el archivo
        archivo = open("./csv/"+nombre_archivo, "w", newline="", encoding="utf-8")
        data = csv.writer(archivo, delimiter=',')
        for row in lista_p:
            data.writerow(row)
        archivo.close()
        return lista_p
    elif opcion == 2:
        return None
    else:
        print("Opcion no valida")
        time.sleep(2)
        return None
    
def enviar_correo(lista_p):
    os.system('cls')
    print("Enviar correo")
    print("1. Enviar correo")
    print("2. Regresar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        #estableco credenciales
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        username = input("Ingrese su nombre de usuario: ")
        # cuenta sergiodserbluk password = "fdxj pbqi wcpe nxnn"
        password = getpass.getpass("Ingrese su contraseña: ")
        asunto = "Asignacion de grupo de trabajo Codo a Codo 4.0"
        #creo el contexto
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(username, password)
            print("Sesion iniciada con exito")
            time.sleep(2)
            ##
            for i in range(len(lista_p)):
                #armo el mensaje
                    
                mensaje = f"Estimado/a {lista_p[i][3]} {lista_p[i][4]},\n\nLe informamos que ha sido asignado al grupo {lista_p[i][-1]}.\n\nSaludos cordiales."
                #envio el correo
                destinatario = lista_p[i][7]
                print(f"Enviando correo a {lista_p[i][3]} {lista_p[i][4]}...")
                server.sendmail(username, destinatario,asunto, mensaje)
                time.sleep(2)
                print(f"Correo enviado a {lista_p[i][3]} {lista_p[i][4]}")
            ##
            print("Correos enviados con exito")
                
        input("Presione una tecla para continuar...")
    elif opcion == 2:
        return None
    else:
        print("Opcion no valida")
        time.sleep(2)
        return None
    
def listar_por_grupos(lista_p):
    os.system('cls')
    print("Listar por grupos")
    print("1. Listar por grupos")
    print("2. Regresar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        #creo una lista de grupos
        grupos = []
        for i in range(len(lista_p)):
            if lista_p[i][-1] not in grupos:
                grupos.append(lista_p[i][-1])
        #recorro la lista de grupos
        for i in range(len(grupos)):
            print(f"Grupo {grupos[i]}")
            #recorro la lista principal
            for j in range(len(lista_p)):
                if lista_p[j][-1] == grupos[i]:
                    print(lista_p[j][3],lista_p[j][4])
            print()
        input("Presione una tecla para continuar...")
    elif opcion == 2:
        return None
    else:
        print("Opcion no valida")
        time.sleep(2)
        return None
#aca inicia el programa
#creo una lista vacia
lista_principal = []
lista=None
while True:
    opcion = menu()
    if opcion == 1:
        lista = cargar_archivo(lista_principal)
    elif opcion == 2:
        if lista != None:
            listar_datos(lista_principal)
        else:
            print("Primero debe cargar un archivo")
            time.sleep(2)
    elif opcion == 3:
        if lista != None:
            crear_grupos(lista_principal)
        else:
            print("Primero debe cargar un archivo")
            time.sleep(2)
    elif opcion == 4:
        if lista != None:
            listar_por_grupos(lista_principal)
        else:
            print("Primero debe cargar un archivo")
            time.sleep(2)
    elif opcion == 5:
        if lista != None:
            enviar_correo(lista_principal)
        else:
            print("Primero debe cargar un archivo")
            time.sleep(2)
    elif opcion == 6:
        break
    else:
        print("Opcion no valida")
        time.sleep(2)
print("Gracias por usar el programa")
time.sleep(2)     
