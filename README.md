# my_first_project-
Learning GitHub

## my_second_project

A simple Python script (`my_second_project/main.py`) demonstrating basic programming concepts:

- **`greet(name)`** – returns a greeting string; raises `ValueError` for invalid input.
- **`add(a, b)`** – returns the sum of two numbers.
- **`divide(a, b)`** – returns the quotient; raises `ZeroDivisionError` when `b` is zero.

### Fix suggestions applied

| Issue | Fix |
|---|---|
| Missing module-level docstring | Added `"""..."""` at the top of the file |
| No input validation in `greet()` | Added `isinstance` / truthy check; raises `ValueError` on bad input |
| Division by zero not handled | `divide()` raises `ZeroDivisionError` before dividing; caller wraps in `try/except` |
| No `if __name__ == "__main__":` guard | Added guard so the module is importable without side-effects |
| Bare `print` statements at module level | Moved all output into `main()` |
| f-strings used without fallback | Code targets Python 3.6 + which is appropriate for f-strings |

Run the script:

```bash
python3 my_second_project/main.py
```
