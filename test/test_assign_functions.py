import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import pytest
from executor import evaluate, execute
from grammar import parser


def test_assign_statement():
    program = parser.parse(
        """
        ( BEGIN
            ( assign x 10 )
            ( show x )
        END )
    """
    )
    env = {}
    execute(program, env)
    assert env["x"] == 10


def test_function_declaration_and_call():
    program = parser.parse(
        """
        ( BEGIN
            ( function addTwo ( x )
                ( return ( + x 2 ) )
            )
            ( show ( call addTwo 5 ) )
        END )
    """
    )
    env = {}
    execute(program, env)
    assert env["output"] == 7
