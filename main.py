def dispatch(command : str) -> str:
    
    return "no matching command found"

def main():
    while True:
        command = input("Switchboard>>> ")
        if command.lower()in ["exit", "quit"]:
            break
        else:
            result = dispatch(command)
            print(result)
            
if __name__ == "__main__":
    main()            