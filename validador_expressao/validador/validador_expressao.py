OPERADORES = "+-*/" # Constante movida para cá

def validador_expressao(expressao):
    """
    1. Verifica se os parênteses na expressão estão balanceados.
    Retorna True se está válido, False caso contrário.
    """
    contador = 0
    ultimo_char_valido = ""
    primeiro_char_valido = ""
    for char in expressao:

        if char == ' ':
            continue

        # NOVO: Captura o primeiro caractere válido (não-espaço)
        if primeiro_char_valido == "":
            primeiro_char_valido = char

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
    
    # Caso de string vazia ou só com espaços
    if primeiro_char_valido == "":
        return False 

    # Se todos os parênteses foram fechados corretamente 
    # o contator deve estar zerado

    # Retorna True APENAS SE todas as condições finais passarem
    return (
        contador == 0 and  # Regra 1
        primeiro_char_valido not in OPERADORES and # Regra 3
        ultimo_char_valido not in OPERADORES   # Regra 3
    )
