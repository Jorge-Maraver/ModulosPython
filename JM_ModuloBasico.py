"""
Este módulo ha sido enteramente creado por Jorge Maraver

La intención es tener funciones que son necesarias muchas veces en la mayoría de proyectos en un mismo lugar y poder acceder fácilmente
"""

#Funciones para el control de excepciones
#Para convertir un str introducido por el usuario en un int
def DevolverInt(pregunta):
    #bool para hacer la pregunta hasta que de una respuesta válida
    respuestaValida=False
    #Pregunta con excepción de errores
    while(not respuestaValida):
        try:
            num=int(input(pregunta))
            respuestaValida=True
        except:
            print("ERROR: Debe introducir un número entero\n")
            
    return num

#Para convertir un str introducido por el usuario en un float
def DevolverFloat(pregunta):
    #bool para hacer la pregunta hasta que de una respuesta válida
    respuestaValida=False
    #Pregunta con excepción de errores
    while(not respuestaValida):
        try:
            num=float(input(pregunta))
            respuestaValida=True
        except:
            print("ERROR: Debe introducir un número\n")
            
    return num

#Función para devolver un float según si el usuario introduce 1 (True) o 2 (False)
def DevolverBool(pregunta="¿Sí o no?",respuestaTrue="Sí",respuestaFalse="No"):
    #bool para hacer la pregunta hasta que de una respuesta válida
    respuestaValida=False
    
    while(not respuestaValida):
        sn=input(f"{pregunta}\nIntroduzca 1 para responder {respuestaTrue}\ny 2 para reponder {respuestaFalse}\n")
        if(sn=="1"):
            return(True)
        elif(sn=="2"):
            return(False)
        else:
            print(f"Comando introducido no válido: {sn}\nDebe escribir 1 o 2\n")
            
#Esta función servirá para comprobar que la posición introducida por el usuario en un momento dado es válida en una lista con control de excepciones
#En caso de que lo sea, devolverá True, y, en caso contrario, False
def ComprobarPosicionLista(lista,pos):
    #Comprobación con excepción de errores
    try:
        lista[pos]
        if(pos<0):
            return False
        else:
            return True
    except:
        return False

#Esta función servirá para que el usuario elija una posición de una lista y devolver la real (empezando en 0) a partir una pregunta pasada
def DevolverPosicionLista(pregunta,lista,tipoElementoLista=None):
    #bool para hacer la pregunta hasta que de una respuesta válida
    respuestaValida=False
    
    while(respuestaValida==False):
        pos=DevolverInt(pregunta)-1
        if(ComprobarPosicionLista(lista,pos)):
            respuestaValida=True
        else:
            if(tipoElementoLista==None):
                print("ERROR: Respuesta introducida no disponible\nPor favor, repita la respuesta\n")
            else:
                print(f"ERROR: {tipoElementoLista} introducido no disponible\nPor favor, repita la respuesta\n")
            
    return(pos)

#Función para visualizar cualquier lista (general)
def MostrarLista(lista, titulo=None):
    #Si se ha pasado un título a la lista, se imprime
    if(titulo!=None):
        print(titulo)
    #Impresión de cada elemento de la lista
    for i in range(0,len(lista)):
        print(f"{i+1}. {lista[i]}")

#Función que mostrará las opciones disponibles de un menú (pasadas como lista) y devolverá la posición que ocupa la elegida por el usuario
def EleccionOpcionMenu(opciones, titulo="Opciones disponibles:", pregunta="¿Qué quiere hacer?"):
    MostrarLista(opciones,titulo)
    #Se le pregunta al usuario qué quiere hacer (se devuelve lo que introduzca el usuario -1)
    opcion=DevolverPosicionLista(f"\n{pregunta}\nIntroduzca el número correspondiente a la opción que deseé:",opciones)
    
    return(opcion)
            
#Función específica para preguntar al usuario si quiere continuar en un menú usando la función DevolverBool
def PreguntaContinuar(pregunta="¿Quiere continuar o salir del programa?"):
    return(DevolverBool(pregunta,"Continuar","Salir"))