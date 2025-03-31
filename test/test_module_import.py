import pytest
import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from executor import evaluate, execute
from grammar import parser


def test_import_statement():
    # Supondo que você tenha um módulo chamado "module1"
    program = parser.parse(
        """
        ( BEGIN
            ( import 'math.ali' )
        END )
    """
    )
    env = {}
    execute(program, env)
    assert "module1" in env  # O módulo deve ser carregado no ambiente
