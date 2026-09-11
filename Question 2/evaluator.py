import os

def peek():
    # Look at current token without moving.
    return numbers[position]

def take(): 
    # Take current token and move forward.
    global position
    value = numbers[position]
    position += 1 
    return value

# --- Recursive Descent Parser ---
# We parse by precedence, lowest to highest:
# Level 1: + - (addition/subtraction) - lowest
# Level 2: * / % and implicit multiplication e.g. 2(3+4)
# Level 3: unary minus e.g. -5
# Level 4: ^ power (right-associative)
# Level 5: numbers and (... ) - highest
def parse_level1_add_sub(): 
    left_value, left_tree = parse_level2_mul_div() 
    
    # While next token is + or -, keep combining
    while peek() == "+" or peek() =="-":
        op = take() 
        right_value, right_tree = parse_level2_mul_div()
        left_value = left_value + right_value if op == "+" else left_value - right_value
        # Build prefix tree: (+ left right) or (- left right).
        left_tree = f"({op} {left_tree} {right_tree})"

    return left_value, left_tree

def parse_level2_mul_div(): 
    left_value, left_tree = parse_level3_unary() 
    while True: 
        if peek() == "*" or peek() =="/" or peek() =="%":
            op = take() 
            right_value, right_tree = parse_level3_unary()
            if op == "*": left_value *= right_value
            elif op == "/": left_value /= right_value
            elif op == "%": left_value %= right_value
            left_tree = f"({op} {left_tree} {right_tree})"
        # Implicit multiplication: e.g. 2(3) or (2)(3) -> treat '(' as *
        elif peek() == "(":
            op = "*"
            right_value, right_tree = parse_level3_unary()
            left_value *= right_value
            left_tree = f"({op} {left_tree} {right_tree})"
        else:
            break
    return left_value, left_tree


def parse_level3_unary(): 
    if peek() == "-":
        op = take()
        right_value, right_tree = parse_level4_power()
        right_value = -right_value # flip sign
        return right_value, f"(neg {right_tree})"   
    return parse_level4_power()


def parse_level4_power(): 
    left_value, left_tree = parse_level5_primary()
    if peek() == "^":
        op = take()
        # Right side is unary again to allow - in exponent and right associativity
        right_value, right_tree = parse_level3_unary()
        left_value = (left_value) ** right_value
        left_tree = f"({op} {left_tree} {right_tree})"
    return left_value, left_tree


def parse_level5_primary():
    # If token is a number, e.g. '12' or '3.14'
    if peek()[0].isdigit():
        v_str = take() # keep original string for tree
        v_float = float(v_str) # convert to number for calculation
        return v_float, v_str
    
    # If token is '(' then parse inside and expect ')'
    if peek() == "(":
        take() # consume '('
        op = parse_level1_add_sub() # parse full expression inside
        if peek() == ")":
            take () # consume ')'
            return op

    # Anything else is invalid syntax
    raise Exception 

def tokenise(line):
    tokens = []
    pos = 0  
    while pos < len(line):
        c = line[pos]
        if c.isspace():
            pos += 1
            continue
        # Number: can be integer or float like 123 or 12.34
        if c.isdigit():
            token = c
            pos += 1
            # Collect remaining digits
            while pos < len(line) and line[pos].isdigit():
                token += line[pos]
                pos += 1
            # Check for decimal part
            if pos < len(line) and line[pos] == ".":
                token += line[pos]
                pos += 1
                # Must have at least one digit after '.'
                if pos < len(line) and line[pos].isdigit():
                    while pos < len(line) and line[pos].isdigit():
                        token += line[pos]
                        pos += 1
                else:
                    raise Exception  
            tokens.append(token)
            continue

        if c in "+-*/%^()":
            token = c
            pos += 1
            tokens.append(token)
            continue
        else:
            raise Exception 

    tokens.append("END") # Marks end of line
    return tokens
    
def evaluate_file (input_path: str):
    # Read input.txt line by line, parse each expression, write output.txt
    global numbers, position
    return_block = []
    output_text_block = []
    with open (input_path, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue

        original = line     
        tokens_formartted = []
        try:
            # Tokenise line
            numbers = tokenise(line)
            # Format tokens for output like [NUM:2] [OP:+] etc
            for i in numbers:
                if i.replace(".", "").isdigit():
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
            position = 0 # Reset parser to start of tokens
  
            result , tree = parse_level1_add_sub()

            # After parsing, we must be at END, otherwise extra junk like "2+3 abc"
            if peek() != "END":
                raise Exception(f"error!")
            # Build success output
            d = {
                "input": original,
                "tree": tree,
                "tokens": token_str,
                "result": float(result)
            }
            output_text = f"Input: {original}\nTree: {tree}\nTokens: {token_str}\nResult: {float(result)}"
        except Exception:
            # Any error -> ERROR
            d = {
                "input": original,
                "tree": "ERROR",
                "tokens": "ERROR",
                "result": "ERROR"
            }
            output_text = f"Input: {original}\nTree: ERROR\nTokens: ERROR\nResult: ERROR"
        return_block.append(d)
        output_text_block.append(output_text)

    # Write output.txt next to input.txt
    out_path = os.path.join(os.path.dirname(os.path.abspath(input_path)), "output.txt")
    with open(out_path, "w") as out:
        out.write("\n\n".join(output_text_block))
    return return_block


if __name__ == "__main__":
    # Make paths absolute so it works no matter where terminal is
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "input.txt")
    
    func_return = evaluate_file (input_file)
    print (func_return)