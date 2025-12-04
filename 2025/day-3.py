
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    lines = [list(line.split('\n')[0]) for line in lines]
    
    lines = [[int(char) for char in line] for line in lines]
    
    return lines

def first_part(puzzle_input):
    
    r = 0
    
    for battery in puzzle_input:
        
        # keep the largest digit that is NOT in the last position
        max_digit = max(battery[:-1])
        max_digit_i = battery.index(max_digit)

        # keep the largest digit that is after the first largest digit
        max2_digit = max(battery[(max_digit_i+1):])
        
        r += (max_digit * 10) + max2_digit
    
    return r

def second_part(puzzle_input):
    
    r = 0
    
    for battery in puzzle_input:
        
        # save the amount of digits to remove
        k = len(battery) - 12

        i = 0
        while k > 0:
            
            # if we are at the end of the list, just remove the last digit
            if i >= len(battery) - 1:
                battery.pop()
                k -= 1
                i += 1
                continue
            
            # if the current digit is less than the next one, remove it 
            if battery[i] < battery[i+1]:
                battery.pop(i)
                k -= 1
                # move back one index to re-evaluate the previous digit
                i = i -1 if i > 0 else 0
            
            else:
                # move to the next digit only if we did not remove the current one
                i += 1
        
        r += int(''.join([str(digit) for digit in battery]))
    
    return r

if __name__ == '__main__':
    
    puzzle_input = format_input(2025, 3)
    
    print(f'First part solution: {first_part(puzzle_input)}')
    print(f'Second part solution: {second_part(puzzle_input)}')
