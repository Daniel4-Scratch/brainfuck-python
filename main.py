import os

tape = [0] * 30000
pointer = 0

def execute(string):
    global pointer, tape
    loop_stack = []
    string = list(string)
    i = 0
    while i < len(string):
        command = string[i]
        if command == ".":
            print(chr(tape[pointer]), end="")
        elif command == "+":
            tape[pointer] += 1
        elif command == "-":
            tape[pointer] -= 1
        elif command == ">":
            pointer += 1
            if pointer >= 30001:
                pointer = 0
        elif command == "<":
            pointer -= 1
            if pointer < 0:
                pointer = 30000
        elif command == "[":
            if tape[pointer] == 0:
                loop_start = i
                loop_counter = 1
                while loop_counter > 0:
                    i += 1
                    if string[i] == "[":
                        loop_counter += 1
                    elif string[i] == "]":
                        loop_counter -= 1
            else:
                loop_stack.append(i)
        elif command == "]":
            if tape[pointer] != 0:
                i = loop_stack[-1] - 1
            else:
                loop_stack.pop()
        elif command == ",":
            tape[pointer] = ord(input("")[0])
        i += 1
    print("")

while True:
    code = input(">")
    if code == "exit":
        break
    elif code == "tape":
        cut = 30000
        for i in reversed(tape):
            if i == 0:
                cut -= 1
            else:
                break
        print(tape[:cut])
    elif code == "point":
        print(pointer)
    elif code.split(" ")[0] == "run":
        try:
            with open(code.split(" ")[1], "r") as file:
                for line in file.read().split("\n"):
                    execute(line)
        except Exception as e:
            print(e)
    elif code == "clear":
        tape = [0] * 30000
        pointer = 0
    else:
        execute(code)
