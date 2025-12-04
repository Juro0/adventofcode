
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    lines = [list(line.split('\n')[0].replace('@', '1').replace('.', '0')) for line in lines]
    
    lines = [[int(num) for num in line] for line in lines]
    
    return lines

def first_part(puzzle_input):
    
    r = 0
    
    for y in range(len(puzzle_input)):
        
        for x in range(len(puzzle_input[y])):
            
            # skip empty seats (dots)
            if puzzle_input[y][x] == 0:
                continue
            
            count = 0
            
            # check all adjacent seats
            to_check_list = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
            
            # filter out seats that are out of bounds
            to_check_list = [(y, x) for (y, x) in to_check_list if 0 <= y < len(puzzle_input) and 0 <= x < len(puzzle_input[0])]
            
            for (cy, cx) in to_check_list:
                if puzzle_input[cy][cx] == 1:
                    count += 1
            
            r += count < 4

    return r

def second_part(puzzle_input):
    
    r = 0
    
    for y in range(len(puzzle_input)):
        
        for x in range(len(puzzle_input[y])):
            
            # skip empty seats (dots)
            if puzzle_input[y][x] == 0:
                continue
            
            count = 0
            
            # check all adjacent seats
            to_check_list = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]

            # filter out seats that are out of bounds
            to_check_list = [(y, x) for (y, x) in to_check_list if 0 <= y < len(puzzle_input) and 0 <= x < len(puzzle_input[0])]
            
            for (cy, cx) in to_check_list:
                if puzzle_input[cy][cx] == 1:
                    count += 1
            
            if count < 4:
                
                r += 1
                # mark seat as empty for next iterations
                puzzle_input[y][x] = 0
                
                # recursively check again
                # ~ work with the complete input only if you set the recursion limit to a high value :(
                # > import sys
                # > sys.setrecursionlimit(10000)
                return r + second_part(puzzle_input)

    return r

if __name__ == '__main__':
    
    puzzle_input = format_input(2025, 4)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')
