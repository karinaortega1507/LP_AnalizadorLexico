# se importa el módulo yacc
import ply.yacc as yacc

# se importa nuestra lista de tokens
from lexico import tokens
f = open('res_sin', 'w')
f.close

def p_body(p):
    """
    body : expresion
        | metodo_cadena

        | asignacion_estructuras
        | impresion_puts
        | estructura_control
        | funcion_def
        | signo
        | metodo_range
        | operaciones
        | estructura_hash
        | metodo_hash
        | comentario
    """
    print("CORRECTO!")
    f = open('res_sin', 'w')
    f.write("Correcto\n")
    f.close()

#Inicia Karina Ortega
# se define una línea de código
def p_sentencia(p):
    '''sentencia : expresion
               |   instanciacion'''
    p[0] = p[1]


def p_instanciacion(p):
    '''instanciacion : SYMBOL ASIGN NUMBER
                     | SYMBOL ASIGN TEXT
                     | SYMBOL ASIGN GETS
                     | asignacion_estructuras
                     | SYMBOL ASIGN expresion
                     | SYMBOL ASIGN PLUS
                     | SYMBOL ASIGN DECIMAL
                     | SYMBOL ASIGN rango'''
    p[0] = 'instanciacion'


def p_expresion(p):
    '''expresion : comentario
                 | impresion_puts
                 | estructura_control
                 | metodo_cadena
                 | operaciones
                 | metodo_range
                 | metodo_hash
                 | funcion_def'''
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
                      | PUTS metodo_cadena
                      | PUTS metodo_hash
                      | PUTS metodo_range'''
    p[0] = 'impresion_puts'



#Inicia Jocelyn
def p_estructura_control(p):
  ''' estructura_control : bloque_if
                         | bloque_for
                         | bloque_while'''
  p[0]= 'estructura_control'


def p_bloque_if(p):
    '''bloque_if : IF condicion expresion ELSE expresion END
                 | IF NEG condicion expresion END
                 | IF condicion expresion END
                 | IF condicion RETURN boolean END
                 | IF condicion expresion ELSE bloque_if END'''
    p[0]='bloque_if'



def p_bloque_for(p):
    '''bloque_for : FOR SYMBOL IN rango expresion END
                  | FOR SYMBOL IN rango bloque_if expresion END
                  | FOR SYMBOL IN rango expresion bloque_if END'''


def p_bloque_while(p):
    '''bloque_while : WHILE condicion expresion instanciacion END
                    | WHILE condicion bloque_if expresion instanciacion END '''


def p_funcion_def(p):
    '''funcion_def :  DEF SYMBOL expresion END
                    | DEF SYMBOL LPAREN SYMBOL RPAREN RETURN expresion END
                    | DEF SYMBOL LPAREN SYMBOL RPAREN expresion END
                   | DEF SYMBOL LPAREN RPAREN RETURN expresion END'''
    p[0] = 'funcion_def'


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
             | DIFER'''
    p[0] = p[1]


def p_comparacion(p):
    '''comparacion : valor signo valor'''
    p[0]= 'comparacion'


def p_rango(p):
    'rango : LPAREN NUMBER RANGE NUMBER RPAREN'
    p[0]= 'rango'

def p_metodo_range(p):
    '''metodo_range : TEXT DOT STEP LPAREN NUMBER RPAREN
                     | SYMBOL DOT STEP LPAREN NUMBER RPAREN
                     | rango DOT STEP LPAREN NUMBER RPAREN
                     | TEXT DOT MIN
                     | SYMBOL DOT MIN
                     | rango DOT MIN'''
    p[0] = 'metodo_range'

def p_operaciones(p):
    '''operaciones : plus
                   | minus
                   | times
                   | div
                   | pot'''

def p_plus(p):
    '''plus : valor PLUS valor'''
    p[0] = 'plus'


def p_minus(p):
    ' minus : valor MINUS valor'
    p[0] = p[1] - p[3]

def p_times(p):
    'times : valor TIMES valor'
    #p[0] = p[1] * p[3]


def p_div(p):
    'div : valor DIVIDE valor'
    #p[0] = p[1] / p[3]

def p_pot(p):
    'pot : valor POT valor'
    #p[0] = p[1] ** p[3]

def p_estructura_hash(p):
    '''estructura_hash :  LKEY valor_hash RKEY'''
    p[0] = 'estructura_hash'

def p_valor_hash(p):
    '''valor_hash : NUMBER ASIGN MAYORQUE NUMBER
                  | TEXT ASIGN MAYORQUE NUMBER
                  | TEXT ASIGN MAYORQUE TEXT
                  | valor_hash COMMA valor_hash'''

def p_metodo_hash(p):
    '''metodo_hash : TEXT DOT LENGHT
                     | SYMBOL DOT LENGHT
                     | TEXT DOT KEYS
                     | SYMBOL DOT KEYS'''
    p[0] = 'metodo_hash'

#Finaliza karina Ortega

#fin Jocelyn

def p_comentario(p):
    '''comentario : COMMENT'''
    p[0] = 'comentario'


# Error rule for syntax errors
def p_error(p):
    #print("Syntax error in input!")
    f = open('res_sin', 'w')
    if p:
        print(p)
        print("Error sintactico")
        f.write("Error sintactico")
    else:
        print("Error lexico")
        f.write("Error lexico")
    f.close()

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

def validate(expr):
    print(expr)
    return parser.parse(expr)

'''archivo = open("ejemplo.txt")

for linea in archivo:
    linea = linea.strip("\n")
    if len(linea) !=0 :
        # Se coloca en una sola linea el bloque IF
        if (linea[:2] == "if"):
            estructura = linea
            for linea in archivo:
                estructura = estructura + linea
                if(linea[:3] == "end"):
                    break
            linea =estructura
        elif (linea[:3] == "for"):
            estructura = linea
            for linea in archivo:
                estructura = estructura + linea
                if(linea[:3] == "end"):
                    break
            linea =estructura
        elif (linea[:5] == "while"):
            estructura = linea
            for linea in archivo:
                estructura = estructura + linea
                if(linea[:3] == "end"):
                    break
            linea =estructura
        elif (linea[:3] == "def"):
            estructura = linea
            for linea in archivo:
                estructura = estructura + linea
                if (linea[:3] == "end"):
                    break
            linea = estructura
        try:
            print("\nsentencia >>> " + linea)
        except EOFError:
            break
        result = parser.parse(linea)
        print(result)'''
