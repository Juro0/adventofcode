
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    # remove \n from lines and split the line in a list of numbers
    lines = [line.split('\n')[0].split(' ') for line in lines]
    
    return lines

def check_report_safety(report):
    
    # initialize the variation of the report (-1 decreasing / 1 increasing)
    variation = 0

    # initialize the safe level (must be the length of report - 1)
    safe_level = 0

    # cycle the indexes of report
    for i in range(0, len(report)):
        
        # stop if is checking the last char
        if i == len(report)-1:
            break
        
        # initialize char and the next char, converting both of them to int
        char = int(report[i])
        next_char = int(report[i+1])
        
        # if the variation of the report is unknown, set it comparing the first two char
        if variation == 0:
            
            # the report is increasing
            if char < next_char: variation = 1
            
            # the report is decreasing
            elif char > next_char: variation = -1
            
            # the first and second char are equal, second rule violated
            else: break
        
        # if the variation is known, check if it's still the same 
        else:

            if variation == 1 and char > next_char: break
            
            if variation == -1 and char < next_char: break
        
        # check the distance between the two char (valid both if the function is increasing or decreasing)
        distance = abs(char - next_char)
        
        # check if the distance of the number is in [1; 3]
        if distance > 0 and distance < 4:
            
            safe_level += 1
    
    # the report is safe if all the levels (except for the last) are safe
    return safe_level == len(report) - 1

def first_part(puzzle_input):
    
    # initialize the safe counter
    result = 0
    
    # cycle the reports
    for report in puzzle_input:
        
        # if report is safe, increment the safe counter
        result += int( check_report_safety(report) )
    
    return str(result)

def second_part(puzzle_input):
    
    # initialize the safe counter
    result = 0
    
    # cycle the reports
    for report in puzzle_input:
        
        # if report is safe, increment the safe counter
        if check_report_safety(report):
            
            result += 1
            
            continue
        
        # if the report isn't safe, cycle the indexes removing one level at time (Problem Dampener)
        for i in range(0, len(report)):
            
            # create a copy for the report
            report_copy = report.copy()
            
            # remove a level from the report
            report_copy.pop(i)
            
            # check if the report is safe
            if check_report_safety(report_copy):
                
                result += 1
                
                # if the report is safe, don't continue to remove levels from it
                break
    
    return str(result)
    
if __name__ == '__main__':
    
    puzzle_input = format_input(2024, 2)
    
    print('First part solution: ' + first_part(puzzle_input))
    print('Second part solution: ' + second_part(puzzle_input))
