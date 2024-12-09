import random
import os

programming_languages = [
    "Python", "Java", "C", "C++", "C#", "JavaScript", "Ruby", "Go", "Rust", "Swift",
    "Kotlin", "PHP", "Perl", "R", "Scala", "Haskell", "Lua", "Dart", "Elixir", 
    "F#", "Objective-C", "Shell", "Assembly", "Visual Basic", "Groovy", "TypeScript",
    "Crystal", "Nim", "Erlang", "COBOL", "Fortran", "Ada", "Smalltalk", "Scheme",
    "Prolog", "MATLAB", "Octave", "VBScript", "Scratch", "Pascal", "Delphi", "ActionScript",
    "PostScript", "AWK", "Tcl", "FoxPro", "ABAP", "D", "Bash", "PowerShell", "Q#", "Zig",
    "Julia", "VHDL", "Verilog", "PL/SQL", "Transact-SQL", "Common Lisp", "Racket", "Chapel",
    "Modula-2", "Simula", "J", "K", "Io", "Pony", "Logtalk", "Forth", "OCaml", "Mercury"
]

selected_file = "data/selected_languages.txt"

def select_language():
    selected_languages = set()
    if os.path.exists(selected_file):
        with open(selected_file, "r") as file:
            selected_languages = set(line.strip() for line in file)

    remaining_languages = list(set(programming_languages) - selected_languages)
    if not remaining_languages:
        print("All programming languages have been selected.")
        return None

    chosen_language = random.choice(remaining_languages)

    with open(selected_file, "a") as file:
        file.write(chosen_language + "\n")

    print(f"Selected language: {chosen_language}")
    return chosen_language

if __name__ == "__main__":
    select_language()