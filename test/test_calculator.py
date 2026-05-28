# Importamos la función que vamos a probar desde el módulo principal
from app.calculator import sumar

# Test 1: suma de números positivos
def test_sumar_positivos():
    # Verificamos que 2 + 3 sea igual a 5
    assert sumar(2, 3) == 5


# Test 2: suma de números negativos
def test_sumar_negativos():
    # Verificamos que -2 + -3 sea igual a -5
    assert sumar(-2, -3) == -5


# Test 3: mezcla de positivo y negativo
def test_sumar_mixtos():
    # Verificamos que -2 + 3 sea igual a 1
    assert sumar(-2, 3) == 1


# Test 4: suma con cero
def test_sumar_cero():
    # Verificamos que 0 + 5 sea igual a 5
    assert sumar(0, 5) == 5