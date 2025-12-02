
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    # substitute L and R for - and +
    lines = [line.replace('L', '-') for line in lines]
    lines = [line.replace('R', '+') for line in lines]
    
    return lines
    
def first_part(puzzle_input):
    
    r = 0
    n = 50
    
    for step in puzzle_input:
        
        n += int(step)
        
        # use modulo to wrap around the 0-99 range
        if n % 100 == 0: r += 1
    
    return r
    
def second_part(puzzle_input):

    r = 0
    n = 50
    
    for step in puzzle_input:
        
        step = int(step)
        
        new = n + step
        
        # add the number of times it crosses a multiple of 100 (passing zero)
        # +1 if it crosses zero
        # +1 if it lands exactly on zero
        r += (abs(new) // 100)+ (1 if (n*new < 0) else 0) + (1 if new == 0 else 0)
        
        # use modulo to wrap around the 0-99 range
        n = new % 100
        
    return r

if __name__ == '__main__':
    
    puzzle_input = format_input(2025, 1)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')