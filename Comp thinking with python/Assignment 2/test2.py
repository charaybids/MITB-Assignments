import re

class CrosswordSolver:
    def __init__(self):
        self.patterns = []

    def crossword_puzzle(self, s, l):
        ### DO NOT EDIT THIS PART ###
        self.m = len(s.split("\n"))
        self.n = len(s.split("\n")[0])

        # part 1: prepare the pattern variable
        self.patterns = []  # list of patterns to be used for part 2
        self.line_pattern = re.compile(r'a length (\d+) word with (.+)')

 # Generate patterns
        for item in l:
            if 'a length' in item:
                match = self.line_pattern.match(item)
                if match:
                    length = int(match.group(1))
                    positions = match.group(2).split(', ')
                    char_positions = {}
                    for pos in positions:
                        parts = pos.split(' ')
                        char = parts[0]
                        index = int(parts[-2])
                        char_positions[index] = char
                    pattern = self.create_pattern_from_positions(length, char_positions)
                    self.patterns.append(pattern)
            else:
                pattern = self.create_pattern_from_word(item)
                self.patterns.append(pattern)

        assert len(self.patterns) == len(l)
        
        # part 2: search for the pattern in the crossword
        for pattern in self.patterns:
            p = re.compile(pattern)
            m = p.findall(s)
            if len(m) == 1:
                return m[0]

    def create_pattern_from_word(self, word):
        # Create regex pattern to match the word in all possible directions
        return f"({word}|{word[::-1]})"

    def create_pattern_from_positions(self, length, char_positions):
        # Create regex pattern to match a word of given length with specified characters in positions
        horizontal_pattern = ['.'] * length
        vertical_pattern = ['.'] * length
        diagonal_pattern_lr = ['.'] * length
        diagonal_pattern_rl = ['.'] * length

        for pos, char in char_positions.items():
            horizontal_pattern[pos] = char
            vertical_pattern[pos] = char
            diagonal_pattern_lr[pos] = char
            diagonal_pattern_rl[length - pos - 1] = char

        horizontal_pattern = ''.join(horizontal_pattern)
        vertical_pattern = ''.join(vertical_pattern)
        diagonal_pattern_lr = ''.join(diagonal_pattern_lr)
        diagonal_pattern_rl = ''.join(diagonal_pattern_rl)

        return f"({horizontal_pattern}|{vertical_pattern}|{diagonal_pattern_lr}|{diagonal_pattern_rl})"

# Example usage:
solver = CrosswordSolver()
crossword = '''abc
gar
tvd'''
instructions = [
    'cat',
    'a length 3 word with g in the 0 position, a in the 1 position, t in the 2 position',
    'a length 3 word with a in the 1 position, t in the 2 position'
]
result = solver.crossword_puzzle(crossword, instructions)
print(result)