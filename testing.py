import Portafolio2;
import pytest;


def test_susbistas_impares_1():
    assert Portafolio2.subListas_impares([23, 6756, 5533, 811]) == [[2,3], [5,5,3,3], [8, 1, 1]]
    
def test_susbistas_impares_2():
    assert Portafolio2.subListas_impares([152, 45, 60]) == [[4,5]]

def test_susbistas_impares_3():
    assert isinstance(str(Portafolio2.subListas_impares ([])), str) == isinstance("Error en la entrada, no se permite lista vacía", str)
###########################################################################

def test_es_computable_1():
    assert Portafolio2.es_computable(332) == True
    
def test_es_computable_2():
    assert Portafolio2.es_computable(6877) == True
    
def test_es_computable_3():
    assert Portafolio2.es_computable(33) == False
      
###########################################################################

matriz = [ [9, 2, 0, 3, 4], [3, 0, 0, 0, 9], [0, 0, 0, 0, 0], [4, 0, 0, 0, 3], [1, 3, 0, 9, 1] ]

def test_matriz_diamante_1():
    assert Portafolio2.matriz_diamante(matriz) == True

    
###########################################################################    

def test_max_profundidad_lista_1():
    assert Portafolio2.max_profundidad_lista([[["H"], [["M"],[[12]]], [13]], [[45]], []]) == [[["H"], [["M"], [[12]]], [13]], [["M"], [[12]]], [[12]], [12]]
    
def test_max_profundidad_lista_2():
    assert Portafolio2.max_profundidad_lista([[["Hola"]], "Mundo"]) == [[["Hola"]], ["Hola"]]

def test_max_profundidad_lista_3():
    assert Portafolio2.max_profundidad_lista([["Distanciamiento"], ["Social"]]) == [["Distanciamiento"]]


