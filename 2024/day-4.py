
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    # remove \n from lines
    lines = [line.split('\n')[0] for line in lines]
    
    return lines

def check_xmas_via_direction(puzzle, x, y, dx, dy, length):
    
    # prevent the 'pacman effect' of the word XMAS
    if not (0 <= y + 3 * dy < length and 0 <= x + 3 * dx < length):
        return False
    
    return (
        puzzle[y][x] == 'X' and
        puzzle[y+dy][x+dx] == 'M' and
        puzzle[y+2*dy][x+2*dx] == 'A' and
        puzzle[y+3*dy][x+3*dx] == 'S'
    )

def first_part(puzzle):
    
    # initialize the counter of XMAS
    result = 0
    
    # declare a list of directions
    directions = [
        (0, 1), (0, -1),    # vertical
        (1, 0), (-1, 0),    # horizontal
        (1, -1), (1, 1),    # top diagonal
        (-1, -1), (-1, 1)   # bottom diagonal
    ]
    
    # save in a costant height and width of the puzzle
    length = len(puzzle)
    
    # cycle for the Y of the puzzle
    for y in range(length):
        
        # cycle for the X of the puzzle
        for x in range(length):
            
            # cycle for the directions
            for dx, dy in directions:
                
                # check if in the desired direction, there is the word XMAS
                if check_xmas_via_direction(puzzle, x, y, dx, dy, length):
                    
                    # if there is the word XMAS, increment the counter
                    result += 1
                
    return str(result)

def second_part(puzzle):
    
    # initialize the counter of X-MAS
    result = 0
    
    # save in a costant height and width of the puzzle
    length = len(puzzle)
    
    # cycle for the Y of the puzzle
    for y in range(length):
        
        # cycle for the X of the puzzle
        for x in range(length):
            
            # save the character in a variable
            char = puzzle[y][x]
            
            # check if the character isn't in the edge
            if x == 0 or x == length-1 or y == 0 or y == length-1:
                continue
            
            # save the 4 corner character in variables
            tl = puzzle[y-1][x-1]
            tr = puzzle[y-1][x+1]
            bl = puzzle[y+1][x-1]
            br = puzzle[y+1][x+1]
            
            # check only in relation to the center of the X-MAS, the character A
            if char == 'A':
                
                if (tl=='M' and br=='S') and ( (tr=='M' and bl=='S') or (tr=='S' and bl=='M') ):
                    
                    result += 1
                
                elif (tl=='S' and br=='M') and ( (tr=='M' and bl=='S') or (tr=='S' and bl=='M') ):
                    
                    result += 1
            
    return str(result)

if __name__ == '__main__':
    
    puzzle_input = format_input(2024, 4)
    
    print('First part solution: ' + first_part(puzzle_input))
    print('Second part solution: ' + second_part(puzzle_input))
