# `FOR` Control Structure

The language supports `FOR` loops with two modes: iterating over the elements of a list (`IN`) and iterating through indices up to a limit (`UNTIL`). Below is a detailed description of how this structure works.

---

## `FOR` Syntax

```plaintext
(FOR <variable> IN <list> <body>)
(FOR <variable> UNTIL <limit> <body>)
```

- `<variable>`: An identifier that will hold the current value in each iteration.
- `<list>`: An expression that evaluates to a list (used with `IN`).
- `<limit>`: An integer specifying the number of iterations (used with `UNTIL`).
- `<body>`: One or more instructions to be executed in each iteration.

---

## Behavior

### Iterating over lists (`IN`)
When `IN` is used, the loop variable is assigned to each element of the list, in the order they appear. For each element, the block of code in the loop body is executed.

### Iterating through indices (`UNTIL`)
When `UNTIL` is used, the loop variable is set to the current index, starting at `0` and continuing up to (`<limit> - 1`). The loop body is executed for each index value.

---

## Example 1: Iterating over a list

This example demonstrates how to use `FOR` to iterate over the elements of a list:

### Code
```lisp
(begin
  (assign [10, 20, 30] mylist)
  (for x in mylist
    (show x))
)
```

### Output
```
10
20
30
```

### Explanation
1. The list `[10, 20, 30]` is assigned to the variable `mylist`.
2. The `FOR` loop iterates over each element of the list, assigning the current value to the variable `x`.
3. The instruction `(show x)` displays the current value of `x`.

---

## Example 2: Iterating through indices

This example demonstrates how to use `FOR` with a specific limit:

### Code
```lisp
(begin
  (for i until 5
    (show i))
)
```

### Output
```
0
1
2
3
4
```

### Explanation
1. The loop starts at index `0` and continues up to `4` (i.e., `limit - 1`).
2. The variable `i` holds the current index value in each iteration.
3. The instruction `(show i)` displays the current value of `i`.

---

## Error Handling

1. **Invalid type after `IN`:** If the expression following `IN` is not a list, an error is raised:
   ```
   Error: Expression after "in" must be a list, got <type>.
   ```
2. **Invalid type after `UNTIL`:** If the expression following `UNTIL` is not an integer, an error is raised:
   ```
   Error: Expression after "until" must be an integer, got <type>.
   ```
3. **Undefined variables:** If a variable used in the loop body is not defined, an error is raised:
   ```
   Error: Undefined variable: <variable>.
   ```

---

With these features, the `FOR` structure provides flexibility for working with lists and index-based iterations, making it a powerful tool for data manipulation and flow control.
