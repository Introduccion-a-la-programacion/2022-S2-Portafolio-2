# 2022 S1 Portafolio 3

El archivo debe llamarse **Portafolio3.py**, además respetar el nombre de las funciones que más adelante se describen
Recordar hacer las validaciones de cada una de las restricciones

## invertirNumero(num)
Dado un parámetro **num** diferente a cero, la función debe revertir el orden de sus dígitos
No utilizar funciones como **reverse** o similares
Se permite número negativos y la respueste debe conservar su signo
```python
>>>invertirNumero(24)
42
>>>invertirNumero(-123)
-321
>>>invertirNumero(120)
21
>>>invertirNumero(9)
9
```

## divisores(num)
Imprimir los divisores de un número de manera **descendente**.
Solo números enteros positivos.
Para esta forma de impresión hacer uso de la función print() con el parámetro adicional **end**

```python
>>>divisores(24)
[24, 12, 8, 6, 4, 3, 2, 1]
```

## multiplicacion(num, factor)  
Multiplicación de un número  a un factor sin utilizar el operador de multiplicación.
Para ambos parámetros solo números enteros positivos.

```python
>>>multiplicacion(5, 2)
10
```

## division(dividendo, divisor)
Resultado de la división entera un número “dividendo” entre un número “divisor” sin utilizar el operador de división.
Para ambos parámetros solo números enteros positivos.
Tomar en cuenta la divisón entre cero no es permitido.

```python
>>>division(25, 5)
5
>>>division(25, 0)
'Error: División entre cero'  
```

## corrimientoAEntero(num)
Corrimientos al entero, pasar los números de la parte decimal a la parte entera.
Mantener el signo en el caso que sea negativo.
Máximo dos digitos en el decimal
No usar str() ni convertir a lista u otra función pre construida por python

```python
>>>corrimientoAEntero(133.5)   
1335
>>>corrimientoAEntero(133888.51)   
13388851
>>>corrimientoAEntero(-133.5)   
-1335
```
## contarDigitosFlotante(num)
Devolver la cantidad de dígitos que tiene esta representación numérica, pero esta vez tomando en cuenta los dígitos de la parte de los decimales. 
El número puede ser positivos o negativos.
```python
>>>contarDigitosFlotante(133.58)
5
>>>contarDigitosFlotante(-133.5)
4
>>>contarDigitosFlotante(-13.0)
2
```
## indiceNumero(num, indice)
Retorna el dígito del número según índices.
Para ambos parámetros solo números enteros positivos.
```python
>>>indiceNumero(1335, 3)  	
5
>>>indiceNumero(1389735, 3)  	
9
>>>indiceNumero(1335, 8)
'Error: Indice fuera del rango del número'
```
## cortarNumero(num, ini, fin)
Construir una función que reciba un número y ordenados de manera ascendente.
Para ambos parámetros solo números enteros positivos.
Verificar que los parámtros **ini** y **fin** no sobre pasen el largo del número.
```python
>>>cortarNumero(1335, 1, 2)
33
>>>cortarNumero(1335, 8, 2)
'Error: Indices fuera del rango del número'
```

## textoPalindromo(texto)
Construir una función que reciba un texto cualquiera.
El texto debe ser diferente a vacio
Verificar que el texto sea idéntico si al ser leido de izquierda a derecha o de derecha a izquierda suene igual
```python
>>>textoPalindromo("OSO")
True
>>>textoPalindromo("CASA")
False
```

## multiplicarElmentosLista(lista)
Construir una función que reciba lista 
La lista debe ser diferente a vacio
Se multiplicará los elementos de la lista que sean **pares**, los demás elementos que no cumpla serán omitidos

```python
>>> multiplicarElementosLista([2, 8, 5, 10])
160
>>> multiplicarElementosLista([2, 3, 5, 18.3, 100.5])
2
>>> multiplicarElementosLista([2, 8, 5, 10, 0])
0
>>> multiplicarElementosLista([2])
2
>>> multiplicarElementosLista([2, 8, True, [], "Hola", 5])
16
```
