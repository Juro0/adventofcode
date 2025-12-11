
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    lines = [line.split('\n')[0] for line in lines]
    
    # fresh ranges
    fresh = [line for line in lines if line.__contains__('-')]
    
    # items to check
    items = [int(line) for line in lines if not line.__contains__('-') and len(line) > 0]
    
    return (fresh, items)

def first_part(puzzle_input):
    
    fresh, items = puzzle_input
    
    r = 0
    
    for item in items:
        
        for f in fresh:
            
            min, max = int(f.split('-')[0]), int(f.split('-')[1])
            
            # check if item is in range
            if min <= item <= max:
                r +=1
                break
    
    return r

def second_part(puzzle_input):
    
    # mantain only the ranges of fresh items
    fresh, _ = puzzle_input
    
    fresh = [[int(f.split('-')[0]), int(f.split('-')[1])] for f in fresh]
    
    # sort ranges by their start value
    fresh.sort(key=lambda x: x[0])
    
    # current range checking
    c = fresh[0]
    
    r = 0
    
    # start from the second range
    for f in fresh[1:]:
        
        # if current range end is greater than or equal to the next range start
        if c[1] >= f[0]:
            
            # if the range is completely inside the current range skip it
            if c[1] >= f[1]:
                continue
            
            # extend the current range end to the next range end
            c[1] = f[1]
        
        else:
            
            # add the length of the current range to the result
            r += c[1] - c[0] + 1
            
            # move to the next range
            c = f

    # add the last range length to the result
    r += c[1] - c[0] + 1

    return r

if __name__ == '__main__':
    
    puzzle_input = format_input(2025, 5)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')
