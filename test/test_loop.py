import pytest
import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from executor import evaluate, execute
from grammar import parser

def test_while_statement():
    program = parser.parse(
        """
        ( BEGIN
            ( assign x 0 )
            ( while ( < x 5 )
                ( BEGIN
                    ( assign x ( + x 1 ) )
                    ( show x )
                END )
            )
        END )
    """
    )
    env = {"output": []}
    execute(program, env)
    assert env["output"] == [1, 2, 3, 4, 5]


def test_for_statement():
    program = parser.parse(
        """
        ( BEGIN
            ( for i in ( [1 2 3 4] )
                ( BEGIN
                    ( show i )
                END )
            )
        END )
    """
    )
    env = {"output": []}
    execute(program, env)
    assert env["output"] == [1, 2, 3, 4]
