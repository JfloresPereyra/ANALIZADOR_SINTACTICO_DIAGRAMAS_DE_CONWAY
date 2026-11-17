# Lista de ASIGNACION DE TOKENS
#   for     = 10
#   in         = 20
#   :            = 30
#   else    = 40
#   Newline    = 50
#   target_list  = 100
#   expression_list = 200
#   simple_stmt   = 300
#   suite         = 400
#   suite_else     = 500

vector_for = [10, 100, 20, 200, 30, 400, 400, 40, 30, 500]

def inicio(tokens):
    error = ''
    i = 0
    i, error = bucle_for(tokens, i)
    if error != '':
        return error
    if i < len(tokens):
        return f"ERROR SINTACTICO: NO SE ESPERABA ESE SIMBOLO '{tokens[i]}' EN LA POSICION {i}"
    return 'VALIDO'

def bucle_for(tokens, i):
    if i < len(tokens) and tokens[i] == 10:
        i += 1
    else:
        return i, "ERROR: SE ESPERABA LA PALABRA RESERVADA 'for'"

    i, error = lista_objetivos(tokens, i)
    if error != '':
        return i, error
      
    if i < len(tokens) and tokens[i] == 20:
        i += 1
    else:
        return i, "ERROR: SE ESPERABA LA PALABRA RESERVADA 'in'"

    i, error = lista_expresiones(tokens, i)
    if error != '':
        return i, error

    if i < len(tokens) and tokens[i] == 30:
        i += 1
    else:
        return i, "ERROR: SE ESPERABA ':' DESPUES DE LA EXPRESION"

    if i < len(tokens) and tokens[i] == 300:
        i, error = sentencia_simple(tokens, i)
        if error != '':
            return i, error
    elif i < len(tokens) and tokens[i] == 400:
        i, error = bloque_suite(tokens, i)
        if error != '':
            return i, error
        while i < len(tokens) and tokens[i] == 400:
            i, error = bloque_suite(tokens, i)
            if error != '':
                return i, error
    else:
        return i, "ERROR: SE ESPERABA 'simple_stmt' O 'suite' DESPUES DE LOS DOS PUNTOS"

    if i < len(tokens) and tokens[i] == 40: 
        i += 1
        if i < len(tokens) and tokens[i] == 30:
            i += 1
        else:
            return i, "ERROR: SE ESPERABA ':' DESPUES DEL 'else'"

        if i < len(tokens) and tokens[i] == 50:
            i += 1
        elif i < len(tokens) and tokens[i] == 500:
            i, error = bloque_else(tokens, i)
            if error != '':
                return i, error
        else:
            return i, "ERROR: SE ESPERABA 'Newline' O 'suite_else' DESPUES DE 'else'"

    return i, ''

def lista_objetivos(tokens, i):
    if i < len(tokens) and tokens[i] == 100:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'target_list'"

def lista_expresiones(tokens, i):
    if i < len(tokens) and tokens[i] == 200:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'expression_list'"

def sentencia_simple(tokens, i):
    if i < len(tokens) and tokens[i] == 300:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'simple_stmt'"
def bloque_suite(tokens, i):
    if i < len(tokens) and tokens[i] == 400:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'suite'"

def bloque_else(tokens, i):
    if i < len(tokens) and tokens[i] == 500:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'suite_else'"

print(inicio(vector_for))
