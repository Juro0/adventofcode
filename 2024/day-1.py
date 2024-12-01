
def format_input(year, day):

    with open(f'{year}/inputs/day-{day}.txt') as f:
        lines = f.readlines()
    
    # remove \n from lines and split each line in two parts
    lines = [line.split('\n')[0].split('   ') for line in lines]
    
    # separate the two parts of every line each in one list
    list_a = [int(line[0]) for line in lines]
    list_b = [int(line[1]) for line in lines]
    
    return [list_a, list_b]
    
def first_part(puzzle_input):
    
    # unpack the two list
    list_a, list_b = puzzle_input
    
    # sort each list
    list_a.sort()
    list_b.sort()
    
    # initialize the sum of the distances
    result = 0
    
    # cycle the indexes of the two lists
    for i in range(0, len(list_a)):
        
        # calculate the distance between the two numbers
        result += abs(list_a[i] - list_b[i])
    
    return str(result)

def second_part(puzzle_input):
    
    # unpack the two list
    list_a, list_b = puzzle_input
    
    # initialize the similarity score
    result = 0
    
    # cycle the number in the first list
    for number in list_a:
        
        # check how many times the number is inside the second list
        times = list_b.count(number)
        
        # increase the similarity score
        result += number * times
    
    return str(result)

if __name__ == '__main__':
    
    puzzle_input = format_input(2024, 1)
    
    print('First part solution: ' + first_part(puzzle_input))
    print('Second part solution: ' + second_part(puzzle_input))
