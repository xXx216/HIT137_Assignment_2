
# this is just an example: 2 + 3 * (4 + 1)
numbers = ["2", "+", "3", "*", "(", "4", "+", "1", ")"] 

position = 0

#everytime a def parse takes a value, position is increased by 1.'



def parse_level1_add_sub(): # 3 position left - middle - right/ start from lv 1 - 5, then return from 5 back to 1
    left = parse_level2_mul_div()
def parse_level2_mul_div(): # 3 position left - middle - right 
    left = parse_level3_power()
def parse_level3_power(): # 3 position left - middle - right 
    left = parse_level4_unary()
    if numbers[position] == "^":
        ###
def parse_level4_unary(): # 3 position: middle - right
    if numbers[position] == "-":
        ####
    else:
        return parse_level5_primary()



def parse_level5_primary(): # takes in brackets and numbers
    value = numbers[position]
    if value.isdigit():
        position += 1 
        return value
    
    if value == "()"
        # something 


















def evaluate_file (input_path: str):
    with open (input_path, "r") as f:
        content = f.read()
    for line in content:
        # something something
        result = parse_level1_add_sub()







if __name__ == "__main__":
    evaluate_file ("input.txt")