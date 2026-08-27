from tools.calculator import calculator

def dispatch(command : str) -> str:
    if command.startswith("calc "):
        expression = command[5:]
        return calculator(expression)
    return "no matching command found"

def main():
    while True:
        command = input("Switchboard>>> ")
        if command.lower() in ["exit", "quit"]:
            break
        else:
            result = dispatch(command)
            print(result)
            
if __name__ == "__main__":
    main()            