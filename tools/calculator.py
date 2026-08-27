def calculator(expression : str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid math expression"

math = input("calc: ")
print(f"{calculator(math)}")