OPERADORES = "+-*/" 

def _eh_operador(char):
    return char in OPERADORES

def _eh_numero(char):
    return char.isdigit()

def validador_expressao(expressao):
    contador = 0
    ultimo_char_valido = ""
    primeiro_char_valido = ""
    for char in expressao:

        if char == ' ':
            continue

        if primeiro_char_valido == "":
            primeiro_char_valido = char

        
        if _eh_numero(ultimo_char_valido):
            if char == '(':
                return False

        if _eh_operador(ultimo_char_valido):
            if not _eh_numero(char) and char != '(':
                return False
                
        if char == "(":
            contador += 1
        elif char == ")":
            contador -= 1
            if contador < 0:
                return False 
            
        ultimo_char_valido = char
    
    if primeiro_char_valido == "":
        return False 

    
    return (
        contador == 0 and 
        not _eh_operador(primeiro_char_valido) and 
        not _eh_operador(ultimo_char_valido)  
    )
