import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import pytest
from executor import evaluate, execute
from grammar import parser


def test_addition():
    expression = parser.parse("( 3 + 5 )")
    result = evaluate(expression, {})
    assert result == 8


def test_subtraction():
    expression = parser.parse("( 10 - 4 )")
    result = evaluate(expression, {})
    assert result == 6


def test_multiplication():
    expression = parser.parse("( 4 * 3 )")
    result = evaluate(expression, {})
    assert result == 12


def test_division():
    expression = parser.parse("( 10 / 2 )")
    result = evaluate(expression, {})
    assert result == 5


def test_modulo():
    expression = parser.parse("( 10 % 3 )")
    result = evaluate(expression, {})
    assert result == 1
