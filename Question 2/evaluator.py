import os

def peek():
    return numbers[position]

def take(): 
    global position
    value = numbers[position]
    position += 1 
    return value

def parse_level1_add_sub(): 
    left = parse_level2_mul_div() 
    while peek() == "+" or peek() =="-":
        middle = take() 
        right = parse_level2_mul_div()
        left = f"({middle}, {left}, {right})"

    return left

def parse_level2_mul_div(): 
    left = parse_level3_unary() 
    while True: 
        if peek() == "*" or peek() =="/" or peek() =="%":
            middle = take() 
            right = parse_level3_unary()
        elif peek() == "(":
            middle = "*"
            right = parse_level3_unary()
            left = f"({middle}, {left}, {right})"
        else:
            break
    return left


def parse_level3_unary(): 
    if peek() == "-":
        middle = take()
        right = parse_level4_power()
        return f"(neg {right})"
    
    return parse_level4_power()


def parse_level4_power(): 
    left = parse_level5_primary()
    if peek() == "^":
        middle = take()
        right = parse_level5_primary()
        left = f"({middle}, {left}, {right})"
    return left


def parse_level5_primary():
    if peek().isdigit():
        value = take()
        return value
    if peek() == "(":
        take() 
        middle = parse_level1_add_sub() 
        if peek() == ")":
            take ()
            return middle
    
    raise Exception (f"Error!")

def tokenise(line):
    tokens = []
    pos = 0
    
    while pos < len(line):
        c = line[pos]
        if c.isspace():
            pos += 1
            continue
        if c.isdigit():
            token = c
            pos += 1
            while pos < len(line) and line[pos].isdigit():
                    token += line[pos]
                    pos += 1
            tokens.append(token)
            continue
        if c in "+-*/%^()":
            token = c
            pos += 1
            tokens.append(token)
            continue
        else:
            raise Exception (f"Error!")
    tokens.append("END")
    return tokens
    



def evaluate_file (input_path: str):
    global numbers, position
    return_block = []
    with open (input_path, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for line in lines:
        if not line.strip():
            continue
        
        original = line
        
        tokens_formartted = []
        try:
            numbers = tokenise(line)
            for i in numbers:
                if i.isdigit():
                    tokens_formartted.append(f"[NUM:{i}]")
                elif i in "+-*/%^":
                    tokens_formartted.append(f"[OP:{i}]")
                elif i == "(":
                    tokens_formartted.append(f"[LPAREN:{i}]")
                elif i == ")":
                    tokens_formartted.append(f"[RPAREN:{i}]")
                elif i == "END":
                    tokens_formartted.append("[END]")
            
            token_str = " ".join(tokens_formartted)    
            position = 0
            tree = parse_level1_add_sub()

            if peek() != "END":
                raise Exception(f"error!")
            
            d = {
                "input": original,
                "tree": tree,
                "tokens": token_str,
                "result": 0.0
            }
        except Exception:
            d = {
                "input": original,
                "tree": "ERROR",
                "tokens": "ERROR",
                "result": "ERROR"
            }
        return_block.append(d)
    return return_block


if __name__ == "__main__":
    evaluate_file ("input.txt")