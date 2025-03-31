import ply.lex as lex
import ply.yacc as yacc
import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
# === LEXER ===
# Tokens List
tokens = [t.strip() for t in open('src/tokens_list.txt', 'r').readlines()]

# Simple tokens rules
t_BEGIN = r'begin'
t_END = r'end'
t_ASSIGN = r'assign'
t_SHOW = r'show'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_FOR = r'for'
t_UNTIL = r'until'
t_IN = r'in'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LE = r'\<\='
t_GE = r'\>\='
t_EQ = r'\=\='
t_NE = r'\!\='
t_AND = r'\&\&'
t_NOT = r'\!'
t_OR = r'\|\|'
t_LT = r'\<'
t_GT = r'\>'
t_COMMA = r'\,'
t_FUNCTION = r'function'
t_CALL = r'call'
t_RETURN = r'return'
t_IMPORT = r'import'
t_ignore = ' \t'

reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'assign': 'ASSIGN',
    'show': 'SHOW',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'function': 'FUNCTION',
    'call': 'CALL',
    'return': 'RETURN',
    'import': 'IMPORT',
    "for": "FOR",
    'in': 'IN',
    'until': 'UNTIL'
}

# Complex tokens rules
def t_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'(\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\')'
    t.value = t.value[1:-1]
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'Invalid Character: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()
