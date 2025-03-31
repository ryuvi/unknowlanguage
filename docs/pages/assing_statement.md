### Language Syntax and Usage Guide

This document serves as an overview of the syntax and core features of the language, focusing on function creation and invocation, importing external modules, performing calculations, creating variables, and printing their values.

---

### General Syntax
The language uses a Lisp-like syntax, where operations, keywords, and function calls are enclosed in parentheses. Each expression starts with a keyword or operator followed by its arguments or parameters.

Example:
```
(KEYWORD arguments...)
```

---

### Functions: Creating and Calling

#### Creating Functions
Functions are defined using the `FUNCTION` keyword. A function can accept parameters and contain a block of statements to execute.

Syntax:
```
( FUNCTION function_name ( parameters... )
    statements...
)
```

Example:
```
( FUNCTION add ( a, b )
    ( RETURN ( + a b ) )
)
```

Explanation:
- The function `add` takes two parameters, `a` and `b`.
- It returns the result of adding `a` and `b`.

#### Calling Functions
Functions are called using the `CALL` keyword. The function name is followed by the required arguments.

Syntax:
```
( CALL function_name arguments... )
```

Example:
```
( CALL add 5 3 )
```

Explanation:
- Calls the `add` function with arguments `5` and `3`, returning `8`.

---

### Importing Modules

Modules can be imported using the `IMPORT` keyword. This allows you to reuse external code in your program.

Syntax:
```
( IMPORT "module_path" )
```

Example:
```
( IMPORT "math_module.lang" )
```

Explanation:
- Imports a module located at `"math_module.lang"`.
- The imported module is parsed and its contents become available in the current environment.

---

### Performing Mathematical Calculations

Mathematical operations are performed using binary operators like `+`, `-`, `*`, and `/`. These operations are enclosed in parentheses and follow the format:

Syntax:
```
( operator operand1 operand2 )
```

Example:
```
( + 10 5 )  ; Adds 10 and 5, returns 15
( / 20 4 )  ; Divides 20 by 4, returns 5
```

Supported Operators:
- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division

---

### Variables: Creating and Printing

#### Creating Variables
Variables are created using the `ASSIGN` keyword. The value assigned can be a result of an expression, a number, or a list.

Syntax:
```
( ASSIGN value variable_name )
```

Example:
```
( ASSIGN 42 x )
( ASSIGN ( + 5 7 ) result )
```

Explanation:
- Assigns `42` to `x`.
- Assigns the result of `( + 5 7 )`, which is `12`, to `result`.

#### Printing Variables
To print the value of a variable, use the `SHOW` keyword.

Syntax:
```
( SHOW variable_name )
```

Example:
```
( SHOW x )
```

Explanation:
- Displays the value of `x` in the output.

---

### Example Program
The following program demonstrates variable creation, a simple function, importing a module, performing calculations, and printing output:

```
( BEGIN
    ( IMPORT "math_utils.lang" )
    ( ASSIGN 10 x )
    ( ASSIGN 5 y )
    ( FUNCTION multiply ( a, b )
        ( RETURN ( * a b ) )
    )
    ( SHOW x )
    ( SHOW y )
    ( SHOW ( CALL multiply x y ) )
END )
```

Output:
```
10
5
50
```

Explanation:
1. Imports an external module.
2. Defines variables `x` and `y`.
3. Defines a `multiply` function.
4. Prints the values of `x` and `y`.
5. Calls the `multiply` function with `x` and `y`, printing the result.

---

This document provides a comprehensive overview of the syntax and essential constructs, enabling you to write and understand programs efficiently in the language.
