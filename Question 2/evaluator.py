
# this is just an example: 2 + 3 * (4 + 1)
numbers = ["2", "+", "3", "*", "(", "4", "+", "1", ")"] 

position = 0


def parse_level1_add_sub(): # 3 position left - middle - right 
    pass
def parse_level2_mul_div(): # 3 position left - middle - right 
    pass
def parse_level3_power(): # 3 position left - middle - right 
    pass
def parse_level4_unary(): # 3 position: middle - right
    pass



def parse_level5_primary(): # takes in brackets and numbers/ start from parse_lv5 backwards to 1 and everything comes back to lv5
    left = parse_level4_unary()
    



















def evaluate_file (input_path: str):
    with open (input_path, "r") as f:
        content = f.read()
    for line in content:
        # something something
        result = parse_level5_primary()







if __name__ == "__main__":
    evaluate_file ("input.txt")