
# this is just an example: 2 + 3 * (4 + 1) (token)
numbers = ["2", "+", "3", "*", "(", "4", "+", "1", ")", "END"] 

position = 0

#everytime a def parse takes a value, position is increased by 1.'

def peek():
    return numbers[position]

def take() 
    global position
    value = numbers[position]
    position += 1 #everytime a parse level accepts a character, position is moved.
    return value

def parse_level1_add_sub(): # 3 position left - middle - right/ start from lv 1 - 5, then return from 5 back to 1
    left = parse_level2_mul_div()
    if peek() == "+" or "-":
        middle = take()
        right = parse_level2_mul_div()
        left = f"{middle}, {left}, {right}"
    else:
        return left

def parse_level2_mul_div(): # 3 position left - middle - right 
    left = parse_level3_unary()
    if peek() == "*" or "/" or "%":
        middle = take()
        right = parse_level3_unary()
    else:
        return left


def parse_level3_unary(): # 3 position: middle - right
    if peek() = "-":
        middle =....
    else:
        return parse_level4_power()


def parse_level4_power(): # 3 position left - middle - right 
    left = parse_level5_primary()
    if peek() = "^":
        #xxx
    else:
        return left


def parse_level5_primary(): # takes in brackets and numbers
    if peek().isdigit():
        value = take()
        return value
    if peek() == "(":
        take() # left = "("
        middle = parse_level1_add_sub() # second layer start with lv1 inside first layer
    if peek() == ")":
        take ()
        return left


    


















def evaluate_file (input_path: str):
    with open (input_path, "r") as f:
        content = f.read()
    for line in content:
        # something something
        result = parse_level1_add_sub()
        if left != "END":
            raise Exception(f"error!")







if __name__ == "__main__":
    evaluate_file ("input.txt")