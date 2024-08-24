"""
Este módulo ha sido enteramente creado por Jorge Maraver
"""

import JM_ModuloBasico as mb
#Importación de mi propio módulo

"""
Funciones para declarar los valores a usar en cada uno de los cálculos
"""
#Función para que el usuario introduzca un valor para n (la cantidad total de elementos)
def Elegir_n():
    n=0
    #Limitamos que n no pueda ser menor a 2
    while(n<2):
        n=mb.DevolverInt("\n¿Qué valor contiene n? (la cantidad total de elementos)")
        if(n<2):
            print("n debe ser al menos 2")
    return(n)

#Función para que el usuario introduzca un valor para p (la cantidad de elementos por grupo)
def Elegir_p():
    p=0
    #Limitamos que p no pueda ser menor a 1
    while(p<1):
        p=mb.DevolverInt("\n¿Qué valor contiene p? (la cantidad de elementos por grupo)")
        if(p<1):
            print("p debe ser al menos 1")
    return(p)

#Función para calcular el factorial de un número pasado
def Factorial(num):
    #Variable que contendrá el resultado final
    #Inicializado como 1 para aplicar multiplicaciones
    factorial = 1

    #Bucle dependiente del número pasado
    #En cada iteración se le restará 1 hasta llegar a 1
    while(num > 1):
        factorial *= num    
        #Ahora, restamos 1 a número para obtener el siguiente que debemos multiplicar
        num-=1
    
    return(factorial)

"""
Funciones para todos los cáculos en sí mismos

Permiten tanto dar valores ya predefinidos pasados a la función como declararlos en el momento
"""
#Función para calcular la permutación
def Permutacion(n=None):
    if(n==None):
        n=Elegir_n()
    return(Factorial(n))

#Función para calcular la permutación con repetición
def PermutacionR(n=None,repeticiones=None):
    if(n==None):
        n=Elegir_n()
    #repeticiones guarda la cantidad de veces que se repite cada elemento
    #Se almacena como lista
    #Si no se pasa como argumento, se piden hasta que se alcance la cantidad de repeticiones total equivalga a la de n
    if(repeticiones==None):
        sumaRepeticiones=0
        i=1
        repeticiones=[]
        while(sumaRepeticiones<n):
            repeticion=mb.DevolverInt(f"Introduzca la cantidad de veces que se repite el elemento {i}")
            repeticiones.append(repeticion)
            sumaRepeticiones+=repeticion
            i+=1
        #Si el usuario ha introducido mayor cantidad de repeticiones que la de la cantidad total de elementos (n) se le avisa
        if(sumaRepeticiones>n):
            print("\nLa cantidad de repeticiones total introducida es mayor que la de elementos, probablemente el resultdo no sea correcto")
    divisor=1
    for i in repeticiones:
        divisor*=Factorial(i)
    return(Factorial(n)/divisor)

#Función para calcular la variación
def Variacion(n=None,p=None):
    if(n==None):
        n=Elegir_n()
    if(p==None):
        p=Elegir_p()
    return(Factorial(n)/Factorial(n-p))

#Función para calcular la variación con repetición
def VariacionR(n=None,p=None):
    if(n==None):
        n=Elegir_n()
    if(p==None):
        p=Elegir_p()
    return(n**p)

#Función para calcular la combinación
def Combinacion(n=None,p=None):
    if(n==None):
        n=Elegir_n()
    if(p==None):
        p=Elegir_p()
    return(Factorial(n)/(Factorial(n-p)*Factorial(p)))

#Función para calcular la variación con combinación
def CombinacionR(n=None,p=None):
    if(n==None):
        n=Elegir_n()
    if(p==None):
        p=Elegir_p()
    return(Factorial(n+p-1)/(Factorial(n-1)*Factorial(p)))
