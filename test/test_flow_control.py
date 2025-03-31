import pytest
import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from executor import evaluate, execute
from grammar import parser

def test_if_statement():
    program = parser.parse(
        """
        ( BEGIN
            ( if ( == 1 1 )
                ( ( show  'True' ) )
                ( ( show 'False' ) )
            )
        END )
    """
    )
    env = {}
    execute(program, env)
    assert env["output"] == "True"
