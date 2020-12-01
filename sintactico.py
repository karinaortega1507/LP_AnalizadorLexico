# se importa el módulo yacc
import ply.yacc as yacc

# se importa nuestra lista de tokens
from lexico import tokens


#Inicia Karina Ortega
# se define una línea de código
def p_sentencia(p):
    '''sentencia : expresion
               |   instanciacion
               |   declaracion'''
    p[0] = p[1]


def p_instanciacion(p):
    '''instanciacion : SYMBOL ASIGN NUMBER
                     | SYMBOL ASIGN TEXT
                     | SYMBOL ASIGN GETS
                     | asignacion_estructuras
                     | SYMBOL ASIGN expresion
                     | SYMBOL ASIGN PLUS'''
    p[0] = 'instanciacion'


def p_declaracion(p):
    '''declaracion : CLASS SYMBOL
                   | DEF SYMBOL'''
    p[0] = 'declaracion'


def p_expresion(p):
    '''expresion : comentario
                 | impresion_puts
                 | estructura_control
                 | metodo_cadena
                 | operaciones'''
    p[0] = p[1]


def p_metodo_cadena(p):
    '''metodo_cadena : TEXT DOT UPCASE
                     | SYMBOL DOT UPCASE
                     | TEXT DOT CAPITALIZE
                     | SYMBOL DOT CAPITALIZE'''
    p[0] = 'metodo_cadena'

def p_expresion_valor(p):
    '''valor : NUMBER
             | SYMBOL'''
    p[0] = 'valor'


def p_asignacion_estructuras(p):
    '''asignacion_estructuras : SYMBOL ASIGN estructura_array
                              | SYMBOL ASIGN estructura_hash'''
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
                      | PUTS SYMBOL
                      | PUTS SYMBOL estructura_array
                      | PUTS metodo_cadena'''
    p[0] = 'impresion_puts'



#Inicia Jocelyn
def p_estructura_control(p):
  ''' estructura_control : bloque_if
                         | bloque_for
                         | bloque_while'''
  p[0]= 'estructura_control'


def p_bloque_if(p):
    '''bloque_if : IF condicion
                 | IF NEG condicion
                 | ELSE
                 | ELSE IF condicion
                 | ELSE IF NEG condicion
                 | ELSE condicion
                 | ELSE NEG condicion
                 | ELSE condicion AND condicion
                 | ELSE condicion OR condicion
                 | RETURN boolean
                 | END'''
    p[0]='bloque_if'


def p_condicion(p):
    '''condicion : boolean
                 | comparacion
                 | LPAREN comparacion RPAREN
                 | LPAREN comparacion RPAREN AND LPAREN comparacion RPAREN
                 | comparacion OR comparacion
                 | LPAREN comparacion RPAREN OR LPAREN comparacion RPAREN'''


def p_boolean(p):
    ''' boolean : FALSE
                | TRUE
                '''
    p[0]= 'boolean'


def p_signo(p):
    '''signo : EQUAL
             | MAYORQUE
             | MENORQUE
             | DIFER
             | LEQT
             | GEQT'''
    p[0] = p[1]


def p_comparacion(p):
    '''comparacion : valor signo valor'''
    p[0]= 'comparacion'


def p_bloque_for(p):
    '''bloque_for : FOR SYMBOL IN rango'''

def p_rango(p):
    'rango : LPAREN NUMBER RANGE NUMBER RPAREN'
    p[0]= 'rango'

def p_bloque_while(p):
    '''bloque_while : WHILE condicion'''

def p_operaciones(p):
    '''operaciones : plus
                   | minus
                   | times
                   | div'''

def p_plus(p):
    '''plus : NUMBER PLUS NUMBER
            | SYMBOL PLUS NUMBER'''
    p[0] = 'plus'


def p_minus(p):
    ' minus : NUMBER MINUS NUMBER'
    p[0] = p[1] - p[3]

def p_times(p):
    'times : NUMBER TIMES NUMBER'
    p[0] = p[1] * p[3]


def p_div(p):
    'div : NUMBER DIVIDE NUMBER'
    p[0] = p[1] / p[3]


def p_estructura_hash(p):
    '''estructura_hash :  LKEY valor_hash RKEY'''
    p[0] = 'estructura_hash'

def p_valor_hash(p):
    '''valor_hash : NUMBER ASIGN MAYORQUE NUMBER
                  | TEXT ASIGN MAYORQUE NUMBER
                  | TEXT ASIGN MAYORQUE TEXT
                  | valor_hash COMMA valor_hash'''

#Finaliza karina Ortega

#fin Jocelyn

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

'''while True:
    try:
        s = input('Ingrese su código >>> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)'''


archivo = open("ejemplo.txt")

for linea in archivo:

    try:
        print("\nsentencia >>> " + linea)
    except EOFError:
        break
    if len(linea) == 0:
       break
    result = parser.parse(linea)
    print(result)