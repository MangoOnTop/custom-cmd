from tools.calculator import calculator
from tools.weather import weather
from tools.joke import joke

def dispatch(command : str) -> str:
    if command.startswith("calc "):
        expression = command[5:]
        return calculator(expression)
    elif command.startswith("weather "):
        city = command[8:]
        return weather(city)
    elif command.lower() == "joke":
        return joke()
    elif command.lower() == "help":
        return (
            "Available commands:\n"
            "  calc <expression>   e.g. calc 12 * 7\n"
            "  weather <city>      e.g. weather Dhaka\n"
            "  joke                fetches a random joke\n"
            "  exit / quit         exits Switchboard"
        )
    return "No matching command found. Type 'help' to see available commands."

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