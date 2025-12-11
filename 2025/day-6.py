from functools import reduce
from numpy import rot90

def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    return lines

def first_part(puzzle_input):
    
    # get symbols
    symbols = puzzle_input[-1].split()
    
    # get numbers in columns
    nums = [[int(x) for x in line.split()] for line in puzzle_input[:-1]]
    nums = rot90(nums)[::-1]
    
    r = 0
    
    for i in range(len(nums)): 
        
        num = nums[i]
        s = symbols[i]
        
        # sum or product
        r += sum(num) if s == '+' else reduce(lambda x, y: x * y, num)        
        
    return r

def second_part(puzzle_input):
    
    # get symbols
    symbols = puzzle_input[-1].split()
    
    # get columns of numbers (or empty chars) as strings
    nums = [list(n.split('\n')[0]) for n in puzzle_input[:-1]]
    nums = rot90(nums)[::-1]
    
    ris = 0
    j = 0           # symbol index
    new_nums = []   # collected numbers for current symbol
    
    for i in range(len(nums)):
        
        # get number (or empty char)
        n = reduce(lambda x, y: x + y, nums[i])
        
        # if the line is empty, calculate the sum/product of the collected numbers
        if not n.strip():
            
            # sum or product
            ris += sum(new_nums) if symbols[j] == '+' else reduce(lambda x, y: x * y, new_nums)
            
            # reset collected numbers
            new_nums = []
            
            # move to next symbol
            j += 1
            
            continue
        
        # convert to int
        n = int(n)
        
        # collect number
        new_nums.append(n)
    
    # process last collected numbers
    ris += sum(new_nums) if symbols[j] == '+' else reduce(lambda x, y: x * y, new_nums)
    
    return ris

if __name__ == '__main__':
    
    puzzle_input = format_input(2025, 6)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')
