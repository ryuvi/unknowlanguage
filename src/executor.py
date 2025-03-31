import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from grammar import parser

def evaluate_condition(node, env):
    if not isinstance(node, tuple):
        if len(node) == 3:
            operator,left = node[1],node[2]
            value = evaluate(left, env)
            if operator == 'not':
                return not value
            else:
                raise ValueError(f'Invalid condition node: {node}')
        elif len(node) == 4:
            operator,left,right = node[1], node[2], node[3]
            left_val = evaluate(left,env)
            right_val = evaluate(right, env)
            match operator:
                case '==':
                    return left_val == right_val
                case '!=':
                    return left_val != right_val
                case '<':
                    return left_val <  right_val
                case '<=':
                    return left_val <= right_val
                case '>':
                    return left_val > right_val
                case '>=':
                    return left_val >= right_val
                case '&&':
                    return left_val and right_val
                case '||':
                    return left_val or right_val
                case _:
                    raise ValueError(f'Unknown condition operator: {operator}')
        else:
            raise ValueError(f'Invalid condition node: {node}')
    else:
        raise ValueError(f'Invalid condition node: {node}')


def evaluate(node, env):
    if isinstance(node, float):
        return node
    elif isinstance(node, str):
        if node in env:
            return env[node]
        else:
            raise ValueError(f'Undefined variable: {node}')
    elif isinstance(node, list):
        return [evaluate(item,env) for item in node]
    elif isinstance(node, tuple):
        if node[0] == 'binop':
            if len(node) != 4:
                raise ValueError(f'Invalid binop node: {node}')
            _,operator,left,right = node
            left_val = evaluate(left,env)
            right_val = evaluate(right,env)
            match operator:
                case '+':
                    return left_val + right_val
                case '-':
                    return left_val - right_val
                case '*':
                    return left_val * right_val
                case '/':
                    if right_val == float(0):
                        raise ValueError('Division by zero.')
                    return left_val / right_val
                case '%':
                    if right_val == float(0):
                        raise ValueError('Division by zero.')
                    return left_val % right_val
                case _:
                    raise ValueError(f'Unknown operator: {operator}')
        elif node[0] == 'call':
            if len(node) != 3:
                raise ValueError(f'Invalid call node: {node}')
            _, name, args = node
            if name in env and env[name][0] == 'function':
                _,params,body = env[name]
                if len(params) != len(args):
                    raise ValueError(f'Function "{name}" expects {len(params)} arguments, got {len(args)}')
                local_env = env.copy()
                for param, arg in zip(params, args):
                    local_env[param] = evaluate(arg, env)
                for stmt in body:
                    result = execute(stmt, local_env)
                    if result is not None:
                        return result
                return None
            else:
                raise ValueError(f'Undefined function: {name}')
        else:
            raise ValueError(f'Unknown expression type: {node[0]}')
    else:
        raise ValueError(f'Unknown expression node: {node}')

def execute_import(module_path, env):
    try:
        if '/' in module_path:
            with open(module_path, 'r') as f:
                code = f.read()
            module_ast = parser.parse(code, debug=False)
            execute(module_ast, env)
        else:
            with open(f'lib/{module_path}', 'r') as f:
                code = f.read()
            module_ast = parser.parse(code, debug=False)
            execute(module_ast, env)
    except FileNotFoundError:
        raise ValueError(f'Module "{module_path}" not found.')
    except Exception as e:
        raise ValueError(f'Error loading module "{module_path}": {e}')


# === EXECUTOR ===
def execute(node, env):
    if node[0] == 'program':
        for stmt in node[1]:
            result = execute(stmt, env)
            if result is not None:
                return result
    elif node[0] == 'assign':
        _, expression, name = node
        value = evaluate(expression, env)
        env[name] = value
    elif node[0] == 'show':
        _, name = node
        if name in env:
            print(env[name])
        else:
            print(f"Error: variable '{name}' not defined..")
    elif node[0] == 'if':
        _, condition, true_branch, false_branch = node
        if evaluate_condition(condition, env):
            for stmt in true_branch:
                result = execute(stmt, env)
                if result is not None:
                    return result
        else:
            for stmt in false_branch:
                result = execute(stmt, env)
                if result is not None:
                    return result
    elif node[0] == 'while':
        _, condition, body = node
        while evaluate_condition(condition, env):
            for stmt in body:
                result = execute(stmt, env)
                if result is not None:
                    return result
    elif node[0] == 'for':
        _, loop_var, kw, expression, body = node
        if kw == 'in':
            iterable = evaluate(expression, env)
            if not isinstance(iterable, list):
                raise ValueError(f'Expression after "in" must be a list, got {type(iterable).__name__}')
            for item in iterable:
                env[loop_var] = item
                for stmt in body:
                    result = execute(stmt, env)
                    if result is not None:
                        return result
        elif kw == 'until':
            limit = evaluate(expression, env)
            if not isinstance(limit, int):
                raise ValueError(f'Expression after "until" must be an integer, got {type(limit).__name__}')
            for idx in range(1, limit):
                env[loop_var] = idx
                for stmt in body:
                    result = execute(stmt, env)
                    if result is not None:
                        return result
    elif node[0] == 'function':
        _, name, params, body = node
        env[name] = ('function', params, body)
    elif node[0] == 'call':
        _, name, args = node
        if name in env and env[name][0] == 'function':
            _, params, body = env[name]
            if len(params) != len(args):
                raise ValueError(f'Function "{name}" expected {len(params)} arguments, got {len(args)}.')
            local_env = env.copy()
            for param, arg in zip(params, args):
                local_env[param] = evaluate(arg, env)
            for stmt in body:
                result = execute(stmt, local_env)
                if result is not None:
                    return result
        else:
            raise ValueError(f'Undefined function: {name}')
    elif node[0] == 'return':
        _, expression = node
        return evaluate(expression, env)
    elif node[0] == 'import':
        _, module_path = node
        execute_import(module_path, env)
    else:
        raise ValueError(f'Unknown statement type: {node[0]}')
    return None
