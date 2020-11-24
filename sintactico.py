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
                 | expresion_valor
                 | estructura_control'''
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

def p_estructura_control(p):
  ''' estructura_control : bloque_if'''
  p[0]= 'estructura_control'

def p_bloque_if(p):
    '''bloque_if : IF comparacion expresion END'''
    p[0]='bloque_if'

def p_comparacion(p):
    '''comparacion : NUMBER EQUAL NUMBER
                   | NUMBER MAYORQUE NUMBER
                   | NUMBER MENORQUE NUMBER'''
    p[0]= 'comparacion'

#Inicia Edwin
def p_expresion_booleana(p):
    '''
    expresion   :   expresion AND expresion
                |   expresion OR expresion
                |   expresion NOT expresion
                |  LPAREN expresion AND expresion RPAREN
                |  LPAREN expresion OR expresion RPAREN
                |  LPAREN expresion NOT expresion RPAREN
    '''
    if p[2] == "&&":
        p[0] = p[1] and p[3]
    elif p[2] == "||":
        p[0] = p[1] or p[3]
    elif p[2] == "not":
        p[0] =  p[1] is not p[3]
    elif p[3] == "&&":
        p[0] = p[2] and p[4]
    elif p[3] == "||":
        p[0] = p[2] or p[4]
    elif p[3] == "not":
        p[0] =  p[2] is not p[4]

def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion
                |  expresion MAYORQUE expresion
                |  expresion LEQT expresion
                |   expresion GEQT expresion
                |   expresion EQUAL expresion
                |   expresion DIFER expresion
                |  LPAREN expresion RPAREN MENORQUE LPAREN expresion RPAREN
                |  LPAREN expresion RPAREN MAYORQUE LPAREN expresion RPAREN
                |  LPAREN expresion RPAREN LEQT LPAREN expresion RPAREN
                |  LPAREN  expresion RPAREN GEQT LPAREN expresion RPAREN
                |  LPAREN  expresion RPAREN ASIGN LPAREN expresion RPAREN
                |  LPAREN  expresion RPAREN DIFER LPAREN expresion RPAREN
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "==": t[0] = t[1] is t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

#fin Edwin

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