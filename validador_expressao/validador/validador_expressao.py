OPERADORES = "+-*/" # Constante movida para cá

def validador_expressao(expressao):
    """
    1. Verifica se os parênteses na expressão estão balanceados.
    Retorna True se está válido, False caso contrário.
    """
    contador = 0
    ultimo_char_valido = ""
    for char in expressao:

        if char == ' ':
            continue

        if char in OPERADORES and ultimo_char_valido in OPERADORES:
            return False

        if char == "(":
            contador += 1
        elif char == ")":
            contador -= 1
            # Fecha mais do que abriu
            if contador < 0:
                return False
            
        ultimo_char_valido = char

    # Se todos os parênteses foram fechados corretamente 
    # o contator deve estar zerado
    return contador == 0
