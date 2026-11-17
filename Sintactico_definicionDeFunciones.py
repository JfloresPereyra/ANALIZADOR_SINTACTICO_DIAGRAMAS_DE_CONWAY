
#   def   = 10
#   (   = 20
#   ,   = 30
#   )   = 40
#   :     = 50
#   function_name = 100
#   parameter     = 200
#   simple_stmt   = 300
#  statement     = 400

vector_def = [10, 100, 20, 200, 30, 200, 40, 50, 400, 400]

def inicio(tokens):
    error = ''
    i = 0
    i, error = funcion(tokens, i)
    if error != '':
        return error
    if i < len(tokens):
        return f"ERROR SINTACTICO: NO SE ESPERABA ESE SIMBOLO '{tokens[i]}' EN LA POSICION {i}"
    return 'VALIDO'

def funcion(tokens, i):
    if i < len(tokens) and tokens[i] == 10:
        i += 1
    else:
        return i, "ERROR: SE ESPERABA LA PALABRA RESERVADA 'def'"

    i, error = nombre_funcion(tokens, i)
    if error != '':
        return i, error

    if i < len(tokens) and tokens[i] == 20:
        i += 1
        if i < len(tokens) and tokens[i] == 200:
            i, error = parametro(tokens, i)
            if error != '':
                return i, error
            while i < len(tokens) and tokens[i] == 30:
                i += 1
                i, error = parametro(tokens, i)
                if error != '':
                    return i, error

        if i < len(tokens) and tokens[i] == 40:
            i += 1
        else:
            return i, "ERROR: SE ESPERABA PARENTESIS DE CIERRE ')'"

    if i < len(tokens) and tokens[i] == 50:
        i += 1
    else:
        return i, "ERROR: SE ESPERABA ':' EN LA DEFINICION DE LA FUNCION"

    if i < len(tokens) and tokens[i] == 300:
        i, error = sentencia_simple(tokens, i)
        if error != '':
            return i, error
    elif i < len(tokens) and tokens[i] == 400:
        i, error = sentencia(tokens, i)
        if error != '':
            return i, error
        while i < len(tokens) and tokens[i] == 400:
            i, error = sentencia(tokens, i)
            if error != '':
                return i, error
    else:
        return i, "ERROR: SE ESPERABA 'simple_stmt' O 'statement' DESPUES DE LOS DOS PUNTOS"

    return i, ''

def nombre_funcion(tokens, i):
    if i < len(tokens) and tokens[i] == 100:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA EL NOMBRE DE LA FUNCION"

def parametro(tokens, i):
    if i < len(tokens) and tokens[i] == 200:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA UN PARAMETRO"



def sentencia(tokens, i):
    if i < len(tokens) and tokens[i] == 400:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'statement'"
  
def sentencia_simple(tokens, i):
    if i < len(tokens) and tokens[i] == 300:
        return i + 1, ''
    return i, "ERROR: SE ESPERABA 'simple_stmt'"
  


print(inicio(vector_def))
