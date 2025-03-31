from sys import argv
from src.tokens import *
from src.grammar import *
from src.executor import *


# === TEST ===
code = """
(begin
    (import "utils.lisp")
    (assign (call square 5) result)
    (show result)
end)
"""


debug=False
if len(argv) < 2:
    print(f'Error: Usage is alicia <file>')
    exit(-1)

with open(argv[1]) as file:
    code = file.read()

def run(code):
    ast = parser.parse(code, debug=debug)
    environment = {}
    execute(ast, environment)

run(code)
