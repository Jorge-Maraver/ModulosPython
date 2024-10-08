# Módulos de Python

Este repositorio almacena todos los módulos que he creado para importar en python.

## Módulo Básico

Este módulo es el principal, pues es el que uso siempre en todos mis proyectos.
Además, el resto del módulos también dependen de éste.

Contiene las siguienetes funciones:

1. Funciones que devuelven variables con control de excepciones y mensajes:
   1. DevolverInt()
   2. DevolverFloat()
   3. DevolverBool()
3. Funciones para trabajar con listas o tuplas:
   1. ComprobarPosicionLista()
   2. DevolverPosicionLista()
   3. MostrarLista()
4. Funciones para usar en un menú:
   1. EleccionOpcionMenu()
   2. PreguntaContinuar()

---

## Combinatoria

Almacena todos los módulos relacionados con la combinatora

### Módulo Combinatoria

> Depende del módulo básico

Contiene las siguientes funciones:

1. Funciones que devuelven valores válidos para los cálculos:
   1. Elegir_n()
   2. Elegir_p()
2. Función para devolver el factorial de un número:
   1. Factorial()
3. Funciones realizar permutaciones, variaciones y combinaciones con sus respectivos cambios en caso de que sean con repetición:
   1. Permutacion()
   2. PermutacionR()
   3. Variacion()
   4. VariacionR()
   5. Combinacion()
   6. CombinacionR()

---

## Álgebra

Almacena todos los módulos relacionados con el álgebra

### Módulo Vectores

> Depende del módulo básico

Contiene las siguientes funciones:

1. Funciones que devuelven valores válidos para los cálculos:
   1. DevolverDimension()
   2. CrearVector()
   3. CreacionVectores()
2. Funciones realizar cálculos con vectores:
   1. Sumar()
   2. Restar()
   3. ProductoVectorPorEscalar()
   4. ProductoEscalar()
   5. Modulo()
   6. Angulo()
   7. ProductoVectorial()
   8. Proyeccion()
   9. Ortogonal()

### Módulo Matrices

> Depende del módulo básico

Contiene las siguientes funciones:


1. Funciones que devuelven valores válidos para los cálculos:
   1. DimensionesMatriz()
   2. DimensionesMatrizCuadrada()
   3. CrearMatriz()
   4. MostrarMatriz()
2. Funciones realizar cálculos con una sola matriz:
   1. Determinante2x2()
   2. Determinante3x3()
   3. Transpuesta()
   4. Adjunta3x3()
   5. Inversa3x3()
3. Funciones realizar cálculos con una matriz y un escalar:
   1. MultiplicacionPorEscalar()
   2. DivisionPorEscalar()
4. Funciones realizar cálculos con con dos matrices:
   1. Suma()
   2. Resta()
   3. Multiplicacion()
