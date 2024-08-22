"""
Álgebra Lineal
"""
import JM_ModuloBasico as mb
#Importación de mi propio módulo
from math import sqrt as rc
import math
#Importación de math para los cálculos con ángulos

"""
Funciones para declarar los valores a usar en cada uno de los cálculos
"""
#Función para declarar una dimensionalidad válida para los vectores
def DevolverDimension(pregunta="\nIntroduzca la dimensionalidad del vector:"):
    dim=0
    #Se exige que por lo menos sea 2D
    while(dim<2):
        dim=mb.DevolverInt(pregunta)
        if(dim<2):
            print("ERROR: La dimensionalidad debe ser al menos 2")
    return(dim)

#Función para crear un vector (una lista con los valores correspondientes)
def CrearVector(dim):
    vector=[]
    for i in range(0,dim):
        vector.append(mb.DevolverInt(f"Introduzca el valor del vector para la dimensión {i+1}"))
    return(vector)

#Función para crear una lista de vectores con la misma dimensionalidad
def CreacionVectores(cantidad):
    vectores=[]
    dim=DevolverDimension("Introduzca la dimensionalidad de los vectores:")
    for i in range(0,cantidad):
        print(f"\nCreando vector {i+1}...")
        vectores.append(CrearVector(dim))
        
    return(vectores)

"""
Funciones para todos los cáculos en sí mismos

Permiten tanto dar valores ya predefinidos pasados a la función como declararlos en el momento
"""
#Función para sumar vectores
def Sumar(vectores=None):
    #Lista que almacenará el vector resultante
    vectorSuma=[]
    #Cración de los vectores en caso de que no se hayan pasado
    if(vectores==None):
        cantidad=mb.DevolverInt("¿Cuántos vectores quiere sumar?")
        vectores=CreacionVectores(cantidad)
    for i in range(0,len(vectores[0])):
        #Variable que alcenará cada uno de los factores del vector
        factorModulo=0
        for e in vectores:
            factorModulo+=e[i]
        vectorSuma.append(factorModulo)
    return(vectorSuma)

#Función para restar 2 vectores
def Restar(vectores=None):
    vectorResta=[]
    if(vectores==None):
        vectores=CreacionVectores(2)
    for i in range(0,len(vectores[0])):
        factorModulo=vectores[0][i]-vectores[1][i]
        vectorResta.append(factorModulo)
    return(vectorResta)

#Función para multiplicar un vector por un escalar
def ProductoVectorPorEscalar(vector=None,escalar=None):
    if(vector==None):
        vector=CrearVector(DevolverDimension())
    #Se limita a 1 la cantidad de escalares
    if(escalar==None):
        escalar=mb.DevolverInt(f"Introduzca el factor por el que quiere multiplicar al vector")
    for i in range(0,len(vector)):
        vector[i]*=escalar
    return(vector)

#Función para multiplicar escalarmente 2 vectores
def ProductoEscalar(vectores=None):
    vectorProducto=0
    if(vectores==None):
        vectores=CreacionVectores(2)
    for i in range(0,len(vectores[0])):
        factorModulo=1
        for e in vectores:
            factorModulo*=e[i]
        vectorProducto+=factorModulo
    return(vectorProducto)

#Función para calcular el módulo de un vector
def Modulo(vector=None):
    modulo=0
    if(vector==None):
        vector=CrearVector(DevolverDimension())
    for i in vector:
        modulo+=i**2
    return(rc(modulo))

#Función para calcular el ángulo formado entre 2 vectores
def Angulo(vectores=None):
    if(vectores==None):
        vectores=CreacionVectores(2)
    radianes=math.acos(ProductoEscalar(vectores)/(Modulo(vectores[0])*(Modulo(vectores[1]))))
    return(radianes)

#Función para multiplicar vectorialmente 2 vectores
#Limitado a vectores de 3D
def ProductoVectorial(vectores=None):
    if(vectores==None):
        vectores=[]
        print("Es obligatorio que los vectores tengan 3 dimensiones")
        dim=3
        print("\nCreando vector 1...")
        vectores.append(CrearVector(dim))
        print("\nCreando vector 2...")
        vectores.append(CrearVector(dim))
    factor1=(vectores[0][1]*vectores[1][2])-(vectores[0][2]*vectores[1][1])
    factor2=(vectores[0][0]*vectores[1][2])-(vectores[0][2]*vectores[1][0])
    factor3=(vectores[0][0]*vectores[1][1])-(vectores[0][1]*vectores[1][0])
    return([factor1,-factor2,factor3])

#Función para calcular la proyección de un vector sobre otro
def Proyeccion(vectorU=None,vectorV=None):
    if(vectorU==None):
        dim=DevolverDimension("Introduzca la dimensionalidad de los vectores u y v:")
        print("\nCreando vector u (el proyectado)...")
        vectorU=CrearVector(dim)
        print("\nCreando vector v (sobre el que será proyectado)...")
        vectorV=CrearVector(dim)
    return(ProductoVectorPorEscalar(vectorV,ProductoEscalar([vectorU,vectorV])/ProductoEscalar([vectorV,vectorV])))

def Ortogonal(vectorU=None,vectorV=None):
    if(vectorU==None):
        dim=DevolverDimension("Introduzca la dimensionalidad de los vectores u y v:")
        print("\nCreando vector u (el proyectado)...")
        vectorU=CrearVector(dim)
        print("\nCreando vector v (sobre el que será proyectado)...")
        vectorV=CrearVector(dim)
    return(Restar([vectorU,Proyeccion(vectorU,vectorV)]))