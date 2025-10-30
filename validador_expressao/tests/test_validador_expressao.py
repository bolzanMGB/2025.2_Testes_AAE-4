# tests/test_validador.py
import pytest
from validador.validador_expressao import validador_expressao

def teste_parenteses_balenceados():
    # valida se os parênteses estão corretamente balanceados.
    # válidos
    assert validador_expressao("(1+2)") == True
    assert validador_expressao("(1+2(2*3))") == True
    # inválidos
    assert validador_expressao ("(1+2") == False
    assert validador_expressao (")1)") == False
    assert validador_expressao ("(1))*((2)") == False
    assert validador_expressao (")()") == False
    assert validador_expressao("(") == False
    assert validador_expressao(")") == False

def teste_doiscolocarnomeaqui():
