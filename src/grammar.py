import ply.lex as lex
import ply.yacc as yacc
import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from tokens import *

# PARSER
# Gramatical Rules
def p_program(p):
    """program : LPAREN BEGIN statements END RPAREN"""
    p[0] = ('program', p[3])


def p_statement_import(p):
    """statement : LPAREN IMPORT STRING RPAREN"""
    p[0] = ('import', p[3])

def p_statements_multiple(p):
    """statements : statements statement"""
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    """statements : statement"""
    p[0] = [p[1]]

def p_statement_assign(p):
    """statement : LPAREN ASSIGN expression IDENTIFIER RPAREN"""
    p[0] = ('assign', p[3], p[4])

def p_statement_show(p):
    """statement : LPAREN SHOW IDENTIFIER RPAREN"""
    p[0] = ('show', p[3])

def p_expression_binop(p):
    """expression : LPAREN expression PLUS expression RPAREN
                  | LPAREN expression MINUS expression RPAREN
                  | LPAREN expression TIMES expression RPAREN
                  | LPAREN expression DIV expression RPAREN"""
    p[0] = ('binop', p[3], p[2], p[4])

def p_condition(p):
    """condition : LPAREN expression LE expression RPAREN
                 | LPAREN expression GE expression RPAREN
                 | LPAREN expression EQ expression RPAREN
                 | LPAREN expression NE expression RPAREN
                 | LPAREN expression LT expression RPAREN
                 | LPAREN expression GT expression RPAREN
                 | LPAREN expression AND expression RPAREN
                 | LPAREN expression OR expression RPAREN
                 | LPAREN NOT expression RPAREN
                 """
    match p[2]:
        case 'and':
            p[0] = ('condition', p[3], '&&', p[4])
        case 'or':
            p[0] = ('condition', p[3], '||', p[4])
        case 'not':
            p[0] = ('condition', '!', p[3])
        case _:
            p[0] = ('condition', p[3], p[2], p[4])

def p_statement_if(p):
    """statement : LPAREN IF condition statements ELSE statements RPAREN"""
    p[0] = ('if', p[3], p[4], p[6])

def p_statement_while(p):
    """statement : LPAREN WHILE condition statements RPAREN"""
    p[0] = ('while', p[3], p[4])

def p_statement_while(p):
    """statement : LPAREN FOR IDENTIFIER IN expression statements RPAREN
                 | LPAREN FOR IDENTIFIER UNTIL expression statements RPAREN"""
    p[0] = ('for', p[3], p[4], p[5], p[6])

def p_statement_function(p):
    """statement : LPAREN FUNCTION IDENTIFIER LPAREN parameters RPAREN statements RPAREN
                 | LPAREN FUNCTION IDENTIFIER LPAREN RPAREN statements RPAREN"""
    p[0] = ('function', p[3], p[5], p[7])

def p_statement_call(p):
    """expression : LPAREN CALL IDENTIFIER arguments RPAREN
                  | LPAREN CALL IDENTIFIER LPAREN RPAREN"""
    p[0] = ('call', p[3], p[4])

def p_expression_identifier(p):
    """expression : IDENTIFIER"""
    p[0] = p[1]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_parameters_multiple(p):
    """parameters : IDENTIFIER COMMA parameters"""
    p[0] = [p[1]] + p[2]

def p_parameters_single(p):
    """parameters : IDENTIFIER"""
    p[0] = [p[1]]


def p_arguments_multiple(p):
    """arguments : expression COMMA arguments"""
    p[0] = [p[1]] + p[2]

def p_arguments_single(p):
    """arguments : expression"""
    p[0] = [p[1]]

def p_expression_list(p):
    """expression : LBRACKET elements RBRACKET
                  | LBRACKET RBRACKET"""
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_elements_multiple(p):
    """elements : expression COMMA elements"""
    p[0] = [p[1]] + p[3]

def p_elements_single(p):
    """elements : expression"""
    p[0] = [p[1]]

def p_expression_list_index(p):
    """expression : IDENTIFIER LBRACKET expression RBRACKET"""
    p[0] = ('index', p[1], p[3])

def p_statement_return(p):
    """statement : LPAREN RETURN expression RPAREN"""
    p[0] = ('return', p[3])

def p_error(p):
    if p:
        print(f'Syntax error at token {p.type}: {p.value}')
    else:
        print('Unexpected end of input!')

# parser construct
parser = yacc.yacc()
