
# this is just an example: 2 + 3 * (4 + 1) (token)
numbers = ["2", "+", "3", "*", "(", "4", "+", "1", ")", "END"] 

position = 0

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
    while peek() == "*" or peek() =="/" or peek() =="%":
        middle = take() 
        right = parse_level3_unary()
    elif peek() == "(":
        middle = "*"
        right = parse_level3_unary()
    left = f"({middle}, {left}, {right})"
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
    with open (input_path, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for line in lines:
        if not line.strip():
            continue
        numbers = tokenise(line)
        #xxxx


           
        result = parse_level1_add_sub()
        if peek() != "END":
            raise Exception(f"error!")







if __name__ == "__main__":
    evaluate_file ("input.txt")