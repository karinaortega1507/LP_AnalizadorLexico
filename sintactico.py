# se importa el módulo yacc
import ply.yacc as yacc

# se importa nuestra lista de tokens
from lexico import tokens


# se define una línea de código
def p_sentencia(p):
    '''sentencia : expresion
               |   instanciacion
               |   declaracion'''
    p[0] = p[1]


def p_instanciacion(p):
    '''instanciacion : SYMBOL ASIGN NUMBER
                     | SYMBOL ASIGN TEXT
                     | asignacion_estructuras'''
    p[0] = 'instanciacion'


def p_declaracion(p):
    '''declaracion : CLASS SYMBOL
                   | DEF SYMBOL'''
    p[0] = 'declaracion'


def p_expresion(p):
    '''expresion : comentario
                 | impresion_puts
                 | expresion_valor'''
    p[0] = p[1]


def p_expresion_valor(p):
    '''expresion_valor : NUMBER
                       | TEXT'''
    p[0] = p[1]


def p_asignacion_estructuras(p):
    '''asignacion_estructuras : SYMBOL ASIGN estructura_array'''
    p[0] = 'asignacion_estructuras'


def p_estructura_array(p):
    '''estructura_array :  LBRACK valor_array RBRACK'''
    p[0] = 'estructura_array'


def p_valor_array(p):
    '''valor_array : NUMBER
                   | TEXT
                   | TEXT COMMA valor_array
                   | NUMBER COMMA valor_array'''



def p_impresion_puts(p):
    '''impresion_puts : PUTS TEXT
                      | PUTS NUMBER
                      | PUTS SYMBOL'''
    p[0] = 'impresion_puts'


def p_comentario(p):
    '''comentario : COMMENT'''
    p[0] = 'comentario'


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Ingrese su código >>> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)