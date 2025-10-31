# tests/test_validador.py
import pytest
from validador.validador_expressao import validador_expressao

def teste_parenteses_balenceados():
    # valida se os parênteses estão corretamente balanceados.
    # válidos
    assert validador_expressao("(1+2)") == True
    # inválidos
    assert validador_expressao ("(1+2") == False
    assert validador_expressao (")1)") == False
    assert validador_expressao ("(1))*((2)") == False
    assert validador_expressao (")()") == False
    assert validador_expressao("(") == False
    assert validador_expressao(")") == False

def teste_nao_permite_operadores_seguidos():
    # Casos inválidos (deve retornar False)
    assert validador_expressao("1++2") == False
    assert validador_expressao("1--2") == False
    assert validador_expressao("1+-2") == False
    assert validador_expressao("5*/2") == False
    assert validador_expressao("(1**2)") == False # Dentro de parênteses

    # Casos de regressão (válidos que não devem quebrar)
    assert validador_expressao("1+2") == True
    assert validador_expressao("(1-2)*3") == True

    # CICLO 03 - Regra 3
def teste_nao_comeca_ou_termina_com_operador():
    # Casos inválidos (deve retornar False)
    assert validador_expressao("*1+2") == False       # Começa com operador
    assert validador_expressao("1+2-") == False       # Termina com operador

    # Testando com espaços (Regra 6)
    assert validador_expressao(" /5-1") == False      # Começa com operador
    assert validador_expressao("(1+2)* ") == False    # Termina com operador

    # Testes de regressão (válidos que não devem quebrar)
    assert validador_expressao("(1+2)") == True
    assert validador_expressao("1") == True
    assert validador_expressao("1 + 2") == True

def teste_numero_nao_pode_ser_seguido_por_abre_parenteses():
    assert validador_expressao("5(1+1)") == False
    assert validador_expressao("5 (1+1)") == False
    assert validador_expressao("(1+2(2*3))") == False

def teste_operador_nao_pode_ser_seguido_por_fecha_parenteses():
    assert validador_expressao("(1 + )") == False
    assert validador_expressao("(1 + (2 * ))") == False