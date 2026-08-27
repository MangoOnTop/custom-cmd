# custom-cmd

A command-line tool-calling assistant. You type a plain text command, custom-cmd decides which tool it matches, runs that tool, and prints the result — then waits for your next command.

No LLM involved. This project is about practicing the decide → call → return loop that agent frameworks are built on, using simple keyword-based routing instead of a model making the decision.

## What it does

custom-cmd runs a loop in your terminal. Each command you type is routed to one of three tools:

Command
Example
What it does

`calc <expression>`
`calc 12 * 7`
Evaluates a math expression

`weather <city>`
`weather Dhaka`
Fetches current weather for a city (via wttr.in)

`joke`
`joke`
Fetches a random joke (via official-joke-api)

`help`
`help`
Lists available commands

`exit` / `quit`
`exit`
Exits the program

Example session:

```
$ python main.py
custom-cmd>>> calc 12 * 7
84
custom-cmd>>> weather Dhaka
Dhaka: ☀️ +32°C
custom-cmd>>> joke
Why do programmers prefer dark mode? ... Because light attracts bugs.
custom-cmd>>> fly me to the moon
No matching command found. Type 'help' to see available commands.
custom-cmd>>> exit
```

## How to run it

1. Clone the repo and `cd` into it.
2. Install the one dependency:

```
pip install requests
```
3. Run it:

```
python main.py
```
4. Type commands at the `custom-cmd>>>` prompt. Type `exit` or `quit` to stop.

## Project structure

```
switchboard/
├── main.py              # dispatcher loop — reads input, routes, prints result
├── tools/
│   ├── calculator.py    # calc: evaluates expressions with eval()
│   ├── weather.py       # weather: hits wttr.in, returns plain text
│   └── joke.py          # joke: hits official-joke-api, returns JSON
```

## How it works

`main.py` runs an infinite loop reading input. Each command string is passed to a `dispatch()` function, which checks the command against a series of conditions (`startswith("calc ")`, `startswith("weather ")`, `== "joke"`, etc.) and calls the matching tool function. Each tool is a plain function that takes the relevant argument (or none), does its work, and returns a string. `dispatch()` returns that string back up to `main()`, which prints it.

There's no shared state between commands — each one is handled independently, start to finish, with nothing remembered afterward.

## Limitations

- `calc` uses `eval()` — this evaluates the expression as real Python code, not just arithmetic. It's fine for personal, local use, but `eval()` should never be used on untrusted input in real-world software, since it can execute arbitrary code. A safer version would use Python's `ast` module to restrict evaluation to actual math expressions only.
- No memory or state — commands don't remember anything from previous commands or previous runs. This is intentional (see project goals), but means things like "check weather for the last city I asked about" aren't supported.
- Routing is keyword-based, not intelligent — a command has to start with an exact keyword (`calc `, `weather `) or match exactly (`joke`, `help`) to be recognized. Typos, rephrasing, or natural language input (e.g. "what's the weather like") won't be understood.
- No offline handling beyond basic try/except — if `weather` or `joke` can't reach the internet, the tool returns a generic failure message rather than distinguishing between "no internet," "API down," or "invalid city."
- Single command at a time — no chaining or combining commands in one line (e.g. can't do `calc 5+5 and then weather Dhaka` in one input).

## Why this project exists

This was built as a stepping-stone project toward agentic AI — practicing the "decide which tool to call, call it, return the result" pattern with plain keyword matching before introducing an LLM to make that decision. The dispatcher shape here is the same shape used when an LLM later chooses which tool/function to call based on a user's natural language request.
