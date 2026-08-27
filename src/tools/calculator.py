def calculator(expression : str) -> str:
    if not expression.strip():
        return "No expression provided. Usage: calc <expression>"
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid math expression"