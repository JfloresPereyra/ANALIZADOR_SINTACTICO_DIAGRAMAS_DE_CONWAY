#  or       = 10
#   and       = 20
#   not      = 30
#   (         = 40
#   )          = 50
#   True             = 60
#   False            = 70
#   expresion_logica = 100
#   termino          = 200
#   factor           = 300

vector_logico = [100, 40, 10, 200, 20, 30]

def inicio(tokens):
    error = ''
    i = 0
    i, error = analizar_logica(tokens, i)
    if error != '':
        return error
    if i < len(tokens):
        return f"ERROR SINTACTICO: NO SE ESPERABA ESE SIMBOLO '{tokens[i]}' EN LA POSICION {i}"
    return 'VALIDO'

def analizar_logica(tokens, i):
    i, error = expresion_logica(tokens, i)
    if error != '':
        return i, error

    if i < len(tokens) and tokens[i] == 40:
        i += 1
    else:
        return i, "ERROR: SE ESPERABA '(' DESPUES DE EXPRESION LOGICA"

    if i < len(tokens) and tokens[i] == 10:
        i += 1
    elif i < len(tokens) and tokens[i] == 20:
        i += 1
    elif i < len(tokens) and tokens[i] == 200:
        i, error = termino(tokens, i)
        if error != '':
            return i, error
    else:
        return i, "ERROR: SE ESPERABA 'or', 'and' O 'termino'"

