import re

def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    rules = [line.split('\n')[0].split('|') for line in lines if re.search('^\d+\|\d+$', line)]
    queue = [line.split('\n')[0].split(',') for line in lines if re.search('^(\d+)(,\d+)*$', line)]
    
    return (rules, queue)

def validate_rule(rule, job):
    
    if not rule[0] in job or not rule[1] in job:
        return True
    
    rule = [int(r) for r in rule]
    job = [int(j) for j in job]
    
    if job.index(rule[0]) > job.index(rule[1]):
        return False
    
    return True

def first_part(puzzle_input):
    
    rules, queue = puzzle_input
    
    result = 0
    
    for job in queue:
    
        correct = 0
    
        for rule in rules:
            
            if validate_rule(rule, job):
        
                correct += 1
        
        if correct == len(rules):
            
            result += int(job[ int((len(job)-1)/2) ])
        
    return str(result)

if __name__ == '__main__':
    
    puzzle_input = format_input(2024, 5)
    
    print('First part solution: ' + first_part(puzzle_input))
