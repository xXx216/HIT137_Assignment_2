import os

def peek():
    return numbers[position]

def take(): 
    global position
    value = numbers[position]
    position += 1 
    return value

def parse_level1_add_sub(): 
    left_value, left_tree = parse_level2_mul_div() 
    while peek() == "+" or peek() =="-":
        op = take() 
        right_value, right_tree = parse_level2_mul_div()
        left_value = left_value + right_value if op == "+" else left_value - right_value
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
        right_value = -right_value
        return right_value, f"(neg {right_tree})"   
    return parse_level4_power()


def parse_level4_power(): 
    left_value, left_tree = parse_level5_primary()
    if peek() == "^":
        op = take()
        right_value, right_tree = parse_level3_unary()
        left_value = (left_value) ** right_value
        left_tree = f"({op} {left_tree} {right_tree})"
    return left_value, left_tree


def parse_level5_primary():
    if peek()[0].isdigit():
        v_str = take()
        v_float = float(v_str)
        return v_float, v_str
    if peek() == "(":
        take() 
        op = parse_level1_add_sub() 
        if peek() == ")":
            take ()
            return op
    raise Exception 

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
            if pos < len(line) and line[pos] == ".":
                token += line[pos]
                pos += 1
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
    tokens.append("END")
    return tokens
    
def evaluate_file (input_path: str):
    global numbers, position
    return_block = []
    output_text_block = []
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
            position = 0
  
            result , tree = parse_level1_add_sub()

            if peek() != "END":
                raise Exception(f"error!")
            
            d = {
                "input": original,
                "tree": tree,
                "tokens": token_str,
                "result": float(result)
            }
            output_text = f"Input: {original}\nTree: {tree}\nTokens: {token_str}\nResult: {float(result)}"
        except Exception:
            d = {
                "input": original,
                "tree": "ERROR",
                "tokens": "ERROR",
                "result": "ERROR"
            }
            output_text = f"Input: {original}\nTree: ERROR\nTokens: ERROR\nResult: ERROR"
        return_block.append(d)
        output_text_block.append(output_text)

    out_path = os.path.join(os.path.dirname(os.path.abspath(input_path)), "output.txt")
    with open(out_path, "w") as out:
        out.write("\n\n".join(output_text_block))
    return return_block


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "input.txt")
    func_return = evaluate_file (input_file)
    print (func_return)