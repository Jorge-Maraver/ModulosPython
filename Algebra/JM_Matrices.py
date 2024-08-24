"""
Este módulo ha sido enteramente creado por Jorge Maraver
"""

import JM_ModuloBasico as mb
#Importación de mi propio módulo

"""
Funciones para declarar matrices
"""
#Función para declarar una dimensionalidad válida para las matrices
def DimensionesMatriz(preguntaF="Introduzca la cantidad de filas de la matriz:",preguntaC="Introduzca la cantidad de columnas de la matriz:"):
    filas=0
    #Se exige que por lo menos sea 1
    while(filas<1):
        filas=mb.DevolverInt(preguntaF)
        if(filas<1):
            print("ERROR: Debe introducir un valor no menor a 1")
            
    columnas=0
    #Se exige que por lo menos sea 1
    while(columnas<1):
        columnas=mb.DevolverInt(preguntaC)
        if(columnas<1):
            print("ERROR: Debe introducir un valor no menor a 1")
    return(filas,columnas)

#Función para declarar una dimensionalidad válida para las matrices cuando son concretamente cuadradas
def DimensionesMatrizCuadrada(pregunta="Introduzca la cantidad de filas y columnas de la matriz:"):
    dimensiones=0
    #Se exige que por lo menos sea 2
    while(dimensiones<2):
        dimensiones=mb.DevolverInt(pregunta)
        if(dimensiones<2):
            print("ERROR: Debe introducir un valor no menor a 2")
    return(dimensiones)

#Función para crear una matriz (lista 2D)
def CrearMatriz(filas,columnas):
    matriz=[]
    for i in range(0,filas):
        fila=[]
        for e in range(0,columnas):
            fila.append(mb.DevolverFloat(f"Introduzca el valor correspondiente a la fila {i+1}, columna {e+1}:"))
        matriz.append(fila)
        print()
    return(matriz)

#Función para mostrar una matriz
def MostrarMatriz(matriz):
    for i in matriz:
        for e in i:
            print(f"| {e} ",end="")
        print("|")

"""
Funciones para todos los cáculos en sí mismos

Permiten tanto dar valores ya predefinidos pasados a la función como declararlos en el momento
"""
#Funciones para calcular determinates; en este caso, dado que trabajar con la matriz se va repetir mucho, se le llama solo m
 #En ambos casos, se usará Sarrus
#Función para calcular el determinante de una matriz 2x2
def Determinante2x2(m=None):
    #Creación de la matriz por si no ha sido pasada
    if(m==None):
        dim=2
        print("\nCreando matriz...")
        m=CrearMatriz(dim,dim)

    return(m[0][0]*m[1][1]-m[0][1]*m[1][0])

#Función para calcular el determinante de una matriz 3x3
def Determinante3x3(m=None):
    #Creación de la matriz por si no ha sido pasada
    if(m==None):
        dim=3
        print("\nCreando matriz...")
        m=CrearMatriz(dim,dim)
        
    #Con la intención de hacer el código más legible y entendible, calcularemos el minuendo y el sustraendo por separado
    r1=m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]
    r2=m[0][2]*m[1][1]*m[2][0] + m[0][1]*m[1][0]*m[2][2] + m[0][0]*m[1][2]*m[2][1]
    
    return(r1-r2)

#Función para calcular la transpuesta
def Transpuesta(matriz=None):
    #Creación de la matriz por si no ha sido pasada
    if(matriz==None):
        filas,columnas=DimensionesMatriz("Introduzca la cantidad de filas de la matriz a transponer:","Introduzca la cantidad de columnas de las matrices a transponer:")
        print("\nCreando matriz...")
        matriz=CrearMatriz(filas,columnas)
    
    #Lista que contendrá la transpuesta
    matrizTranspuesta=[]
    
    #Bucle que calcula la matriz resultante
    for i in range(len(matriz[0])):
        fila=[]
        for e in range(len(matriz)):
            fila.append(matriz[e][i])
        matrizTranspuesta.append(fila)
        
    return(matrizTranspuesta)

#Función para calcular la multiplicación por un número
def MultiplicacionPorEscalar(matriz=None,escalar=None):
    #Creación de la matriz ningún valor ha sido pasado
    if(matriz==None):
        filas,columnas=DimensionesMatriz("Introduzca la cantidad de filas de la matriz a multiplicar:","Introduzca la cantidad de columnas de las matrices a multiplicar:")
        print("\nCreando matriz...")
        matriz=CrearMatriz(filas,columnas)
    if(escalar==None):
        escalar=mb.DevolverInt("Introduzca el escalar por el que quiere multiplicar la matriz:")
        
    #Lista que contendrá la transpuesta
    matrizMultiplicacion=[]
    
    #Bucle que calcula la matriz resultante
    for i in matriz:
        fila=[]
        for e in i:
            fila.append(e*escalar)
        matrizMultiplicacion.append(fila)
        
    return(matrizMultiplicacion)

#Función para calcular la divisióm entre un número
def DivisionPorEscalar(matriz=None,escalar=None):
    #Creación de la matriz ningún valor ha sido pasado
    if(matriz==None):
        filas,columnas=DimensionesMatriz("Introduzca la cantidad de filas de la matriz a multiplicar:","Introduzca la cantidad de columnas de las matrices a multiplicar:")
        print("\nCreando matriz...")
        matriz=CrearMatriz(filas,columnas)
    if(escalar==None):
        escalar=mb.DevolverInt("Introduzca el escalar por el que quiere multiplicar la matriz:")
    
    #Se calcula la división usando la multiplicación con el inverso del escalar
    matrizDivision=MultiplicacionPorEscalar(matriz,1/escalar)
    return(matrizDivision)

#Función para calcular la suma de varias matrices
def Suma(matrices=None):
    #Creación de matrices por si no han sido pasadas
    if(matrices==None):
        cantidad=mb.DevolverInt("Introduzca la cantidad de matrices a sumar:")
        filas,columnas=DimensionesMatriz("Introduzca la cantidad de filas de las matrices:","Introduzca la cantidad de columnas de las matrices:")
        matrices=[]
        for i in range(0,cantidad):
            print(f"\nCreando matriz {i}...")
            matrices.append(CrearMatriz(filas,columnas))
            
    #Lista que contendrá la suma
    matrizSuma=[]
    
    #Bucle que calcula la matriz resultante
    for i in range(0,len(matrices[0])):
        fila=[]
        for e in range(0,len(matrices[0][0])):
            elemento=0
            for o in range(0,len(matrices)):
                elemento+=matrices[o][i][e]
            fila.append(elemento)
        matrizSuma.append(fila)
        
    return(matrizSuma)

#Función para calcular la resta de 2 matrices
def Resta(matrices=None):
    #Creación de matrices por si no han sido pasadas
    if(matrices==None):
        filas,columnas=DimensionesMatriz("Introduzca la cantidad de filas de las matrices a restar:","Introduzca la cantidad de columnas de las matrices a restar:")
        matrices=[]
        print("\nCreando matriz 1...")
        matrices.append(CrearMatriz(filas,columnas))
        print("\nCreando matriz 2...")
        matrices.append(CrearMatriz(filas,columnas))
        
    #Lista que contendrá la resta
    matrizResta=[]
    
    #Bucle que calcula la matriz resultante
    for i in range(0,len(matrices[0])):
        fila=[]
        for e in range(0,len(matrices[0][0])):
            fila.append(matrices[0][i][e]-matrices[1][i][e])
        matrizResta.append(fila)
        
    return(matrizResta)

#Función para calcular la multiplicación de 2 matrices
def Multiplicacion(matrices=None):
    #Creación de matrices por si no han sido pasadas
    if(matrices==None):
        filas,columnas=DimensionesMatriz("Introduzca la cantidad de filas de la primera matriz/la cantidad de columnas de la segunda matriz de la multiplicación:",
                                         "Introduzca la cantidad de columnas de la primera matriz/la cantidad de filas de la segunda matriz de la multiplicación:")
        matrices=[]
        print("\nCreando matriz 1...")
        matrices.append(CrearMatriz(filas,columnas))
        print("\nCreando matriz 2...")
        matrices.append(CrearMatriz(columnas,filas))
        
    #Lista que contendrá el producto
    matrizMultiplicacion=[]
    
    #Bucle que calcula la matriz resultante
    for i in range(0,len(matrices[0])):
        fila=[]
        for e in range(0,len(matrices[0])):
            elemento=0
            for o in range(0,len(matrices[1])):
                elemento+=matrices[0][i][o]*matrices[1][o][e]
            fila.append(elemento)
            print(elemento)
        matrizMultiplicacion.append(fila)
        print(fila)
        
    return(matrizMultiplicacion)

#Función para calcular la adjunta de una matriz 3x3
def Adjunta3x3(matriz=None):
    #Dado que en este caso será muy necesario saber las dimensiones de la matriz, se guardará en una variable en lugar de usar siempre len()
    dim=3
    
    #Creación de la matriz por si no ha sido pasada
    if(matriz==None):
        print("\nCreando matriz...")
        matriz=CrearMatriz(dim,dim)
        
    #Lista que contendrá la adjunta
    matrizAdjunta=[]
    
    #Bucle que calcula la matriz resultante
    for i in range(0,dim):
        filaAdjunta=[]
        for e in range(0,dim):
            #Se generan los menores que constituyen la adjunta
            menor=[]
            for o in range(0,dim):
                filaMenor=[]
                guardarFila=False
                for a in range(0,dim):
                    if(o!=i):
                        if(a!=e):
                            filaMenor.append(matriz[o][a])
                            guardarFila=True
                if(guardarFila):
                    menor.append(filaMenor)
            
            #Cálculo de los determinantes
            #Si la suma de las posiciones (en fila y columna) es impar, se añade como negativo
            if((i+e) % 2 == 0):
                filaAdjunta.append(Determinante2x2(menor))
            else:
                filaAdjunta.append(-(Determinante2x2(menor)))
        matrizAdjunta.append(filaAdjunta)
    return(matrizAdjunta)

#Función para calcular la inversa de una matriz 3x3
def Inversa3x3(matriz=None):
    dim=3
    #Creación de la matriz por si no ha sido pasada
    if(matriz==None):
        print("\nCreando matriz...")
        matriz=CrearMatriz(dim,dim)
    
    #Devolverá la inversa usando usando las funciones para calcular su determinante, adjunta, transpuesta y división por un número
    return(Transpuesta(DivisionPorEscalar(Adjunta3x3(matriz),Determinante3x3(matriz))))
