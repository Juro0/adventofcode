
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    # code
    
    return lines

def first_part(puzzle_input):
    
    return 0

def second_part(puzzle_input):
    
    return 0

if __name__ == '__main__':
    
    puzzle_input = format_input(0, 0)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')
