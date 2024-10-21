import re

# Given array
array = [
    'bat',
    'a length 3 word with g in the 0 position, a in the 1 position, t in the 2 position',
    'a length 3 word with a in the 1 position, t in the 2 position'
]

s = '''abc
gar
tvd''' 

pattern = [] # list of patterns to be used for part 2
### REPLACE THE BELOW LINES WITH YOUR CODE ###
line_pattern = r"(\w) in the (\d) position"
generated_pattern = []

for instructions in array:
    if "length" not in instructions:
        pattern.append(r"\b" + instructions + r"\b")
    else:
        m = re.findall(line_pattern, instructions)
        
        concatenated_pattern = ""
        for match in m:
            concatenated_pattern += f"({match[0]}).\n"
        
        # Remove the last '.\n.' and add the final '..'
        concatenated_pattern = concatenated_pattern[:-2] + ''
        pattern.append(concatenated_pattern)
'''
for pat in pattern:
    p = re.compile(pat)
    m = p.findall(s)
    print(m)
    generated_pattern.append(m)
'''

'''
The words have to be found in a crossword
        format i.e. the words have to be found in a horizontal, vertical or diagonal manner. so given a 2D array
        the allowable sequences are [0,0] [0,1] [0,2], [1,0] [1,1] [1,2], [2,0] [2,1][2,2] for vertical,
        [0,0] [1,0] [2,0], [0,1] [1,1] [2,1], [0,2] [1,2] [2,2] for horizontal and [0,0] [1,1] [2,2] or [0,2] [1,1] [2,0] for diagonal
'''

print(pattern)

# Helper function to check if the pattern is found in the crossword
def check_pattern(grid, patterns):
 
    rows = len(grid)
    cols = len(grid[0])
    
    def check_sequence(sequence, patterns):
        for pat in patterns:
            p = re.compile(pat)
            m = p.findall(sequence)
            if m:
                return m[0]
        return None

    # Check horizontal sequences
    for r in range(rows):
        horizontal_sequence = ''.join(grid[r])
        result = check_sequence(horizontal_sequence, patterns)
        if result:
            return result

    # Check vertical sequences
    for c in range(cols):
        vertical_sequence = ''.join(grid[r][c] for r in range(rows))
        result = check_sequence(vertical_sequence, patterns)
        if result:
            return result

    # Check main diagonal sequence
    main_diagonal_sequence = ''.join(grid[i][i] for i in range(min(rows, cols)))
    result = check_sequence(main_diagonal_sequence, patterns)
    if result:
        return result

    # Check anti-diagonal sequence
    anti_diagonal_sequence = ''.join(grid[i][cols - 1 - i] for i in range(min(rows, cols)))
    result = check_sequence(anti_diagonal_sequence, patterns)
    if result:
        return result

    return "No match found"

print(check_pattern(s, pattern)) # cat