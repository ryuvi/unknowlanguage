import pytest
import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from executor import evaluate, execute
from grammar import parser

def test_and_operator():
    expression = parser.parse("( && ( == 3 3 ) ( == 5 5 ) )")
    result = evaluate(expression, {})
    assert result is True


def test_or_operator():
    expression = parser.parse("( || ( == 3 3 ) ( == 1 2 ) )")
    result = evaluate(expression, {})
    assert result is True


def test_not_operator():
    expression = parser.parse("( not ( == 3 4 ) )")
    result = evaluate(expression, {})
    assert result is True
