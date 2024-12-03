import re

def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        line = ''.join(f.readlines())
    
    return line

def first_part(puzzle_input):
    
    # initialize the sum of the multiplication functions
    result = 0
    
    # split the puzzle input in eventual values
    puzzle_input = puzzle_input.split('mul(')
    
    # cycle the eventual values
    for arg in puzzle_input:
        
        try:
            
            # try to close the brackets of the function
            value = arg.split(')')[0]

            # check if the format of the argument is valid
            validity = re.search('^\d{1,3},\d{1,3}$', value)
            
            if not validity:
                continue
            
            # split the value in the two numbers
            a,b = value.split(',')
        
            # multiply the two numbers and add them to the result
            result += int(a) * int(b)
            
        except:
            
            # if there isn't a closing bracket, continue to check other eventual values
            continue
    
    return str(result)

def second_part(puzzle_input):
    
    # initialize the sum of the multiplication functions
    result = 0
    
    # initialize the clear input (without inactive instructions)
    clear_puzzle_input = puzzle_input.split("don't()")[0]
    
    # remove disabled instructions
    for part in puzzle_input.split("don't()"):
        
        try:
            
            # save only active code
            clear_puzzle_input += part.split('do()', 1)[1]
        
        except:
            
            continue
    
    # split the puzzle input in eventual values
    clear_puzzle_input = clear_puzzle_input.split('mul(')
    
    # cycle the eventual values
    for arg in clear_puzzle_input:
        
        try:
            
            # try to close the brackets of the function
            value = arg.split(')')[0]

            # check if the format of the argument is valid
            validity = re.search('^\d{1,3},\d{1,3}$', value)
            
            if not validity:
                continue
            
            # split the value in the two numbers
            a,b = value.split(',')
        
            # multiply the two numbers and add them to the result
            result += int(a) * int(b)
            
        except:
            
            # if there isn't a closing bracket, continue to check other eventual values
            continue
    
    return str(result)

if __name__ == '__main__':
    
    puzzle_input = format_input(2024, 3)
    
    print('First part solution: ' + first_part(puzzle_input))
    print('Second part solution: ' + second_part(puzzle_input))
