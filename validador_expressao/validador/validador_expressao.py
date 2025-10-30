def validador_expressao(expressao):
    """
    1. Verifica se os parênteses na expressão estão balanceados.
    Retorna True se está válido, False caso contrário.
    """
    contador = 0
    for char in expressao:
        if char == "(":
            contador += 1
        elif char == ")":
            contador -= 1
            # Fecha mais do que abriu
            if contador < 0:
                return False

    # Se todos os parênteses foram fechados corretamente 
    # o contator deve estar zerado
    return contador == 0
