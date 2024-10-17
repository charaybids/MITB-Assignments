import re

class Q2:

    def crossword_puzzle(self, s, l):
        ### DO NOT EDIT THIS PART ###
        self.m = len(s.split("\n"))
        self.n = len(s.split("\n")[0])

        # part 1: prepare the pattern variable
        self.pattern = [] # list of patterns to be used for part 2
        ### REPLACE THE BELOW LINES WITH YOUR CODE ###
        self.line_pattern = r"" # replace this with the pattern you will use 

        # part 2: search for the pattern in the crossword
        # feel free to change this part if you feel that it is necessary
        ### REPLACE THE BELOW LINE WITH YOUR CODE ###
        for pattern in self.pattern:
            p = re.compile(pattern)
            m = p.findall(s)
            if len(m) == 1:
                return ____________________________

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
