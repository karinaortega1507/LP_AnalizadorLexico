import ply.lex as lex
# List of token names.   This is always required
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'MAYORQUE',
    'MENORQUE',
    'ASIGN',
    'EQUAL',
    'DIFFERENT',
    'AND',
    'ID',
    'TEXT',
    'COMMENT',
    'COMMA',
    'OR',
    'RANGE',
    'DECIMAL',#
    'ARROW',
    'GEQT',
    'LEQT',
    'DOSPUNTOS',
    'ATRIBUTE',
    'SYMBOL',
    'TEXTO',
    'DOT',
    

)

reserved_words = {
    'end': "END",
    'if': 'IF',
    'else': 'ELSE',
    'puts': 'PUTS',
    'for':'FOR',
    'in':'IN',
    'true':'TRUE',
    'false':'FALSE',
    'class':'CLASS',
    'struct':'STRUCT',
    'new':'NEW',
    'def':'DEF',
    'puts':'PUTS'
        
}

tokens = tokens + tuple(reserved_words.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_EQUAL = r'={2}'
t_DIFFERENT=r'!='
t_ASIGN = r'={1}'
t_AND = r'\&\&'
t_OR=r'\|\|'
t_RANGE=r'\.\.'
t_ARROW=r'=>'
t_GEQT=r'>='
t_LEQT=r'<='
t_DOSPUNTOS=r'\:'
t_ATRIBUTE=r'\:[a-z]+'
t_SYMBOL=r'^[$]{0,1}[a-z|A-Z][a-zA-Z0-9]*'
t_TEXTO=r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_DOT=r'\.'



# A regular expression rule with some action code

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'([a-z\-0-9]+)'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    else:
        t.type = 'SYMBOL'
    return t


def t_TEXT(t):
    r"(\'[\w\s\.\,\:]*\'|\"[\w\s\.\,\:]*\")"
    t.type = reserved_words.get(t.value, 'TEXT')
    return t


def t_COMMENT(t):
    r'(\#[\w\s\.\,\:\*\-]*)'
    t.type = reserved_words.get(t.value, 'COMMENT')
    return t


def t_error(t):
    #print("IlLegal caracter '%s'" % t.value[0])
    estado="** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    print(estado)
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


# Build the lexer
lexer = lex.lex()


# Give the lexer some input
def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


archivo = open("ejemplo.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break

