import re

def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    # removed \n from lines, divided using regex
    rules = [line.split('\n')[0].split('|') for line in lines if re.search('^\d+\|\d+$', line)]
    queue = [line.split('\n')[0].split(',') for line in lines if re.search('^(\d+)(,\d+)*$', line)]
    
    return (rules, queue)

def validate_rule(rule, job):
    
    # if one of the rule element isn't in the list, validate it
    if not rule[0] in job or not rule[1] in job:
        return True
    
    # check if the rule is violated
    if job.index(rule[0]) > job.index(rule[1]):
        return False
    
    return True

def first_part(puzzle_input):
    
    # unpack the two inputs
    rules, queue = puzzle_input
    
    # initialize the sum of the middle-terms
    result = 0
    
    # cycle for job in the queue
    for job in queue:
        
        # initialize the validated-rules counter
        correct = 0
    
        # cycle for rules
        for rule in rules:
            
            # validate the rules and increase the counter
            if validate_rule(rule, job):
        
                correct += 1
        
        # check if the job respect all the rules
        if correct == len(rules):
            
            # add the middle-term value to the result
            result += int(job[ int((len(job)-1)/2) ])
        
    return str(result)

if __name__ == '__main__':
    
    puzzle_input = format_input(2024, 5)
    
    print('First part solution: ' + first_part(puzzle_input))
