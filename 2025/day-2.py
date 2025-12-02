
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        line = f.readlines()[0].split(',')
    
    line = [line.split('-') for line in line]
    
    line = [[int(a), int(b)] for a, b in line]
    
    return line
    
def first_part(puzzle_input):
    
    s = 0
    
    for a, b in puzzle_input:
        
        for i in range(a, b + 1):
            
            x, y = str(i)[:len(str(i))//2], str(i)[len(str(i))//2:]
            
            if x == y:
                s += i
    
    return s
    
def second_part(puzzle_input):

    import re
    
    s = 0
    
    patter = re.compile(r'^(\d+)\1+$')
    
    for a, b in puzzle_input:
        
        for i in range(a, b + 1):
            
            if patter.match(str(i)):
                s += i
    
    return s

if __name__ == '__main__':
    
    puzzle_input = format_input(2025, 2)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')