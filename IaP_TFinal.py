# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:27:02 2021

@author: Nathaly
"""
import random
from datetime import date

def almacenArchivo():
    archivo= open("IaP_TrabajoFinal.txt","w")
    #diccionario:
    for i in diccionario():
        archivo.write(str(i))
        
    #nombreVacunas
    for i in nombreVacunas():
        cad= ""
        cad = str(i)+","
        archivo.write(cad)
        
    #fecha
    archivo.write("\n"+str(fechaAleatoria()))
    
    #lote
    archivo.write("\n"+str(lote()))
    
    #costos
    archivo.write("\n"+str(costos()))
    
    #codigos
    archivo.write("\n"+str(listaCodigos()))
    
    #pesos
    archivo.write("\n"+str(pesos()))
    
    archivo.close()
    return archivo
    
def binaria(codAplicacion,busquedaCodigo):
    indice=-1
    izq= 0
    der= len(codAplicacion)-1
    while izq<=der:
        medio=(izq+der)//2
        if codAplicacion[medio]==busquedaCodigo:
            indice=medio
            break
        else:
            if busquedaCodigo>codAplicacion[medio]:
                izq=medio +1
            else:
                der=medio -1
    return indice
     
def burbuja(codAplicacion):
    for i in range(len(codAplicacion) - 1):
        for j in range(i + 1, len(codAplicacion)):
            if(codAplicacion[i] > codAplicacion[j]):
                aux = codAplicacion[i]
                codAplicacion[i] = codAplicacion[j]
                codAplicacion[j] = aux
    return codAplicacion

def fechaAleatoria():
    inicio = date.today().replace(day=1, month=3, year= 2020).toordinal()
    final =  date.today().toordinal()
    fecha= date.fromordinal(random.randint(inicio,final))
    
    return fecha

def juntarlistas(vacunas,codAplicacion,costo,pesos):
	dicci = {}
	i = 0
    
	for tipo_vacuna in vacunas:
    
		cod=codAplicacion[i]
		cos=costo[i]
		pes=pesos[i]
        
		dicci[tipo_vacuna] = (cod, cos, pes)
		i += 1
        
	diccionarioFinal = [dicci]
	return diccionarioFinal    

def diccionario():
    # value=semilla()
    random.seed(5)
    codAplicacion=listaCodigos()
    burbuja(codAplicacion)
    random.seed(5)
    #pesos de personas de acuerdo a la aplicación de vacuna
    pesos=[random.randint(15,30),0,random.randint(22,48)]
    
    random.seed(5)
    #costo de aplicación
    costo=[random.randrange(131,560,2),random.randint(80,150),random.randrange(30,90,2)]
    
    #tipo de vacuna
    vacunas=("PFIZER","SINOPHARM","MODERNA")
    
    diccionarioFinal= juntarlistas(vacunas, codAplicacion, costo, pesos)
    return diccionarioFinal

def listaCodigos():
    random.seed(5)
    codAplicacion=[]
    for i in range(0,3):
        num= random.randrange(40000,90000,2)
        codAplicacion.append(num)
    return codAplicacion   

def codigos():
    codAplicacion=listaCodigos()
    # codigoAplicacion=codAplicacion
    # codigoAplicacion=
    burbuja(codAplicacion)
    vacunas=nombreVacunas()
    peso=pesos()
    loteVacu=lote()
    costo=costos()
    fecha=fechaAleatoria()
    i=0
    busquedaCodigo=int(input("Ingresar código: "))
    if binaria(codAplicacion,busquedaCodigo)==-1:
        print("No se encontró")
    else:
        i+=1
        if busquedaCodigo== codAplicacion[0]:
            print("Se encontró en la lista")
            print("\nVacuna aplicada fue", vacunas[0])
            print("\nPeso de persona que fue aplicada con",vacunas[0],"es", peso[0])
            print("\nEl costo de importación de cada vacuna del lote es", costo[0])
            print("\nEl número de lote de esta vacuna fue", loteVacu[0])
            print("\nPor finalizar, la vacuna fue aplicada el", fecha)
        elif busquedaCodigo== codAplicacion[1]:
            print("Se encontró en la lista")
            print("\nVacuna aplicada fue", vacunas[1])
            print("\nPeso de persona que fue aplicada con",vacunas[1],"es", peso[1])
            print("\nEl costo de importación de cada vacuna del lote es", costo[1])
            print("\nEl número de lote de esta vacuna fue", loteVacu[1])
            print("\nPor finalizar, la vacuna fue aplicada el", fecha)
        else:
        # elif busquedaCodigo== codAplicacion[2]:
            print("Se encontró en la lista")
            print("\nVacuna aplicada fue", vacunas[2])
            print("\nPeso de persona que fue aplicada con",vacunas[2],"es", peso[2])
            print("\nEl costo de importación de cada vacuna del lote es", costo[2])
            print("\nEl número de lote de esta vacuna fue", loteVacu[2])
            print("\nPor finalizar, la vacuna fue aplicada el", fecha)
        
    print("\nA continuación se presenta la lista de códigos ")
    return (codAplicacion)
        
def busqueda_secuencial(loteVacu,num):
    for i in range(0,len(loteVacu)):
        if num==loteVacu[i]:
            print("\nLa posición de esta cantidad en la lista de lote es ", i)    
            
def pesos():
    random.seed(5)
    peso=[random.randint(15,30),0,random.randint(22,48)]
    return peso

def busquedaLotes():
    vacunas=nombreVacunas()
    peso=pesos()
    loteVacu=lote()
    costo=costos()
    fecha=fechaAleatoria()
    num=int(input("Ingresar cantidad de lotes: "))
    if num in loteVacu:
        if num < 5:
            print("\nVacuna aplicada fue", vacunas[0])
            print("Peso de persona que fue aplicada con Pfizer ", peso[0])
            print("\nPor último, la vacuna Pfizer fue aplicada el ", fecha)
            print("\nEl costo de importación de cada vacuna del lote es ", costo[0])
        elif num > 5:
            print("\nVacuna aplicada fue ", vacunas[2])
            print("Peso de persona que fue aplicada con Moderna ", peso[2])
            print("\nPor último, la vacuna Moderna fue aplicada el ", fecha)
            print("\nEl costo de importación de cada vacuna del lote es ", costo[2])
        else:
            print("\nVacuna aplicada fue ", vacunas[1])
            print("Peso de persona que fue aplicada con Sinopharm ", peso[1])
            print("\nPor último, la vacuna Sinopharm fue aplicada el ", fecha)
            print("\nEl costo de importación de cada vacuna del lote es ", costo[1])
        busqueda_secuencial(loteVacu,num)
    print("\nLa lista de lotes de vacunas es")
    return loteVacu

def lote():
    random.seed(5)
    #para obtener números únicos en una lista
    loteVacu= random.sample(range(1,11), 10)
    # for i in range(0,10):
    #     num2= random.randint(1, 10)
    #     loteVacu.append(num2)
    return loteVacu
        

def quicksort(costo):
    if len(costo)<=1:
        return costo
    else:
        pivot=costo[0]
        costoMa=[]
        costoMe=[]
        costoIg=[]
        for i in range (0,len(costo)):
            if costo[i]>pivot:
                costoMa.append(costo[i])
            elif costo[i]<pivot:
                costoMe.append(costo[i])
            else:
                costoIg.append(costo[i])
        costoMa= quicksort(costoMa)
        costoMe= quicksort(costoMe)
        return costoMe + costoIg + costoMa

def ordenCostos():
    costo=costos()
    costoOrdenados= quicksort(costo)
    print("Costo de importaciones ordenados")
    return costoOrdenados

def costos():
    random.seed(5)
    costo=[random.randrange(131,560,2),random.randint(80,150),random.randrange(30,90,2)]
    return costo

def posicionLista():
    vacunas=nombreVacunas()
    print("0: Pfizer\n1:Sinopharm\n2:Moderna")
    n=int(input("Ingrese posición de aquella lista de la que quiera informarse: "))
    i=0
    codAplicacion =listaCodigos()
    costo=costos()
    loteVacu=lote()
    fecha=fechaAleatoria()
    if n==0:
        i+=1
        print("\nVacuna aplicada: ", vacunas[0])
        print("\nCódigo de vacuna aplicada: ", codAplicacion[0])
        print("\nEl costo de importación de la vacuna aplicada es ", costo[0])
        print("\nNúmero de lote: ", loteVacu[i])
        print("\nFecha aplicada: ", fecha)
        
    if n==1:
        i+=1
        print("\nVacuna aplicada: ", vacunas[1])
        print("\nCódigo de vacuna aplicada: ", codAplicacion[1])
        print("\nEl costo de importación de la vacuna aplicada es ", costo[1])
        print("\nNúmero de lote: ", loteVacu[i])
        print("\nFecha aplicada: ", fecha)
        
    if n==2:
        i+=1
        print("\nVacuna aplicada: ", vacunas[2])
        print("\nCódigo de vacuna aplicada:", codAplicacion[2])
        print("\nEl costo de importación de la vacuna aplicada es ", costo[2])
        print("\nNúmero de lote: ", loteVacu[i])
        print("\nFecha aplicada: ", fecha)
    print("\nOpción ingresada: ")
    return n

def nombreVacunas():
    vacunas=("PFIZER","SINOPHARM","MODERNA")
    return vacunas

def vacuna():
    # codAplicacion=[]
    # for i in range(0,3):
    #     num= random.randrange(40000,90000,2)
    #     codAplicacion.append(num)
    vacunas=nombreVacunas()
    i=0
    nombreVacuna=str(input("Ingrese vacuna: "))
    nombreVacuna=nombreVacuna.lower()
    nombreVacuna=nombreVacuna.upper()  

    if nombreVacuna in vacunas:
        codAplicacion =listaCodigos()
        burbuja(codAplicacion)
        costo=costos()
        loteVacu=lote()
        fecha=fechaAleatoria()
        i += 1
        if vacunas.index(nombreVacuna)==0:
            print("La vacuna ingresada sí está registrada")
            print("\nEl código de aplicación para la vacuna", nombreVacuna, "es", codAplicacion[0])
            print("\nEl costo de importación de la vacuna aplicada es", costo[0])
            print("\nEl número de lote de esta vacuna fue", loteVacu[i])
            print("\nPor último, esta vacuna,", nombreVacuna ,"fue aplicada el", fecha)
            
        if vacunas.index(nombreVacuna)==1:
            print("La vacuna ingresada sí está registrada")
            print("\nEl código de aplicación para la vacuna", nombreVacuna, "es", codAplicacion[1])
            print("\nEl costo de importación de la vacuna aplicada es", costo[1])
            print("\nEl número de lote de esta vacuna fue", loteVacu[i])
            print("\nPor último, esta vacuna,", nombreVacuna ,"fue aplicada el", fecha)
            
        if vacunas.index(nombreVacuna)==2:
            print("La vacuna ingresada sí está registrada")
            print("\nEl código de aplicación para la vacuna", nombreVacuna, "es", codAplicacion[2])
            print("\nEl costo de importación de la vacuna aplicada es ", costo[2])
            print("\nEl número de lote de esta vacuna fue ", loteVacu[i])
            print("\nPor último, esta vacuna, ", nombreVacuna ," fue aplicada el ", fecha)
            
    else:
        print("ERROR, vacuna ingresada NO está registrada")
        
    print("Vacuna ingresada fue:")
    return nombreVacuna
  
def main():
    numero = int(input("Ingrese el numero 10 (para prender) o 0 (para apagar): "))
    ON = 10
    OFF = 0
    
    if (numero == ON):
        
        print("Opciones de menu:")
        
        print("1) Ingresar la aplicacion de una vacuna")
        print("2) Busqueda por codigo") #Por codigo de aplicacion
        print("3) Ordenar la lista por costo de importacion")#utilizando algoritmo Quicksort
        print("4) Buscar una aplicacion de vacuna respecto a cantidad de lotes") #Por numero de lote y mostrar todos sus datos(usar busqueda secuencial)
        print("5) Ingresar una aplicación en una posición determinada de la lista de vacunas")#posi lista vacu
        print("6) Mostrar todas las vacunas con su respectiva información") #mostrar datos
        print("7) Almacenar y actualizar archivo") #almacenaar archivo txt
        
        Opcion = int(input("Ingrese el numero de opcion que desee: "))
        
        while Opcion!=0:
            Ingresar = 1
            Busqueda_por_codigo = 2
            Ordenar_costos = 3
            Busqueda_por_Lote = 4
            Ingresar_posicion = 5
            Datos = 6
            Almacenar = 7
                
            if (Opcion == Ingresar):
                print("En proceso 1\n")
                print(vacuna())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            elif (Opcion == Busqueda_por_codigo):
                print("En proceso 2\n")
                print(codigos())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            elif (Opcion == Ordenar_costos):
                print("En proceso 3\n")
                print(ordenCostos())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            elif (Opcion == Busqueda_por_Lote):
                print("En proceso 4\n")
                print(busquedaLotes())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            elif (Opcion == Ingresar_posicion):
                print("En proceso 5\n")
                print(posicionLista())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            elif (Opcion == Datos):
                print("En proceso 6\n")
                print("A continuación se mostrará la información de las 3 vacunas\n", diccionario())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            elif (Opcion == Almacenar):
                print("En proceso 7\n")
                print(almacenArchivo())
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
                
            else:
                print("Hubo un error, intente otra vez")
                Opcion = int(input("Ingrese otro número de opcion que desee: "))
        
    elif (numero == OFF):
        print("Sistema apagado")
        
    else:
        print("Hubo un error, pruebe otra vez")
        numero = int(input("Ingrese el numero 1(para prender) o 0(para apagar): "))
    
main()