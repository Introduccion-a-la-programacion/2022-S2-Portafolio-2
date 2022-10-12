import Portafolio3;
import pytest;


def test_invertirNumero_1():
    assert Portafolio3.invertirNumero(24) == 42
    
def test_invertirNumero_2():
    assert Portafolio3.invertirNumero(-123) == -321
    
def test_invertirNumero_3():
    assert Portafolio3.invertirNumero(120) == 21
###########################################################################
    
def test_divisores_1():
    assert Portafolio3.divisores(24) == [24, 12, 8, 6, 4, 3, 2, 1]
      
###########################################################################

def test_multiplicacion_1():
    assert Portafolio3.multiplicacion(5, 2) == 10
    
###########################################################################    

def test_division_1():
    assert Portafolio3.division(25, 5) == 5
    
def test_division_2():
    assert isinstance(str(Portafolio3.division(25, 0)), str) == isinstance('Error: División entre cero', str)
    
###########################################################################    

def test_corrimientoAEntero_1():
    assert Portafolio3.corrimientoAEntero(133.5) == 1335
    
def test_corrimientoAEntero_2():
    assert Portafolio3.corrimientoAEntero(-133.5) == -1335    
    
###########################################################################    

def test_contarDigitosFlotante_1():
    assert Portafolio3.contarDigitosFlotante(133.578) == 6
    
def test_contarDigitosFlotante_2():
    assert Portafolio3.contarDigitosFlotante(-133.578) == 6    
    
###########################################################################    

def test_indiceNumero_1():
    assert Portafolio3.indiceNumero(1335, 3) == 5
    
def test_indiceNumero_2():
    assert isinstance(str(Portafolio3.indiceNumero(1335, 8)), str) == isinstance('Error: Indice fuera del rango del número', str)
    
###########################################################################    

def test_cortarNumero_1():
    assert Portafolio3.cortarNumero(1335, 1, 2) == 33

def test_cortarNumero_2():
    assert isinstance(str(Portafolio3.cortarNumero(1335, 8, 2)), str) == isinstance('Error: Indices fuera del rango del número', str)  

###########################################################################    

def test_textoPalindromo_1():
    assert Portafolio3.textoPalindromo("OSO") == True
    
def test_textoPalindromo_2():
    assert Portafolio3.textoPalindromo("CASA") == False
    
########################################################################### 

def test_multiplicarElmentosLista_1():
    assert Portafolio3.multiplicarElementosLista([2, 8, 5, 10]) == 160
    
def test_multiplicarElmentosLista_2():
    assert Portafolio3.multiplicarElementosLista([2, 3, 5, 10.5, 18.3]) == 2
    
def test_multiplicarElmentosLista_3():
    assert Portafolio3.multiplicarElementosLista([2, 8, 5, 10, 0]) == 0
    
def test_multiplicarElmentosLista_4():
    assert Portafolio3.multiplicarElementosLista([2, 8, True, [], "Hola", 5]) == 16    


    
    
