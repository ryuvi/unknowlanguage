import ply.lex as lex
import ply.yacc as yacc

# === LEXER ===
# Tokens List
tokens = [t.strip() for t in open('tokens_list.txt', 'r').readlines()]

# Simple tokens rules
t_BEGIN = r'begin'
t_END = r'end'
t_ASSIGN = r'assign'
t_SHOW = r'show'
t_PLUS = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'

reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'assign': 'ASSIGN',
    'show': 'SHOW'
}

# Complex tokens rules
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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

# PARSER
# Gramatical Rules
def p_program(p):
    """program : LPAREN BEGIN statements END RPAREN"""
    p[0] = ('program', p[3])

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

def p_expression_plus(p):
    """expression : NUMBER PLUS NUMBER"""
    p[0] = p[1] + p[3]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_error(p):
    print(f"syntax error: {p.value}" if p else "Unexpected syntax error!")

# parser construct
parser = yacc.yacc()

def evaluate(node, env):
    if isinstance(node, int):
        return node
    elif node[0] == 'plus':
        _,left,right=node
        return evaluate(left,env) + evaluate(right,env)
    else:
        raise ValueError(f'Unknown expression node: {node}')

# === EXECUTOR ===
def execute(node, env):
    if node[0] == 'program':
        for stmt in node[1]:
            execute(stmt, env)
    elif node[0] == 'assign':
        _, expression, name = node
        value = evaluate(expression, env)
        env[name] = value
        print(env)
    elif node[0] == 'show':
        _, name = node
        print(env)
        if name in env:
            print(env[name])
        else:
            print(f"Error: variable '{name}' not defined..")

# === TEST ===
code = """
(begin
  (assign 1+1 sum)
  (show sum)
end)
"""

print("Testing lexer...")
lexer.input(code)
for token in lexer:
    print(token)

print("\nTesting parser...")
ast = parser.parse(code)
print(ast)
environment = {}

print('\nTesting execution')
execute(ast, environment)
