

import re

class Q2:

    def crossword_puzzle(self, s, l):
        ### DO NOT EDIT THIS PART ###
        # part 1: prepare the pattern variable
        self.patterns = []  # list of patterns to be used for part 2
        self.line_pattern = re.compile(r'a length (\d+) word with (.+)')

        # Generate patterns
        for item in l:
            if 'a length' in item:
                match = self.line_pattern.match(item)
                if match:
                    length = match.group(1)
                    positions = match.group(2).split(', ')
                    formatted_positions = ', '.join([f"{pos.split(' ')[0]}{pos.split(' ')[-2]}" for pos in positions])
                    self.patterns.append(f"{length} word {formatted_positions}")
            else:
                self.patterns.append(item)

        assert len(self.patterns) == len(l)
        print(self.patterns)
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
        pattern = ['.'] * length
        for pos, char in char_positions.items():
            pattern[pos] = char
        return ''.join(pattern)
    


q2 = Q2()

score = 0

### open test case # 1 ###
s = '''abc
gar
tvd''' # the indentation here is NOT an ERROR
l = [
        'bat',
        'a length 3 word with g in the 0 position, a in the 1 position, t in the 2 position',
        'a length 3 word with a in the 1 position, t in the 2 position'
    ]
if q2.crossword_puzzle(s, l) == "cat":
    score += 1
    print('[1/1] first sample case is matched\n')
else:
    print('[0/1] first sample case is not matched\n')

    ### open test case # 2 ###
    s = '''heluo
yello
bello
mello''' # the indentation here is NOT an ERROR
l = [
    'hellu',
    'a length 2 word with a in the 0 position',
    'a length 4 word with h in the 0 position, y in the 1 position, n in the 3 position',
    'a length 4 word with h in the 0 position, l in the 2 position, l in the 3 position'
]
if q2.crossword_puzzle(s, l) == "hell":
    score += 1
    print('[1/1] second sample case is matched\n')
else:
    print('[0/1] second sample case is not matched\n')

if q2.patterns and type(q2.patterns) == list:
    try:
        ### test that the pattern contains regular expression patterns ###
        count = 0
        for pattern in q2.patterns: # this checks that self.pattern contains valid regular expressions that works with the given code for part 2
            p = re.compile(pattern)
            m = p.findall(s)
            if len(m) == 1:
                count += 1
        if count == 1:
            score += 2
            print('[2/2] 1(a) pattern contains regular expressions that gives exactly one match\n')
        elif count > 0:
            score += 1
            print('[1/2] 1(a) pattern contains regular expressions that gives more than one match\n')
        else:
            print('[0/2] 1(a) pattern contains regular expressions that gives no match\n')

        ### test that part 2 works with the given solution ###
        if count > 0:
            score += 2
            print('[2/2] 2(b) part 2 works with the provided code\n')
        else:
            print('[0/2] 2(b) part 2 does not work with the provided code\n')
    except:
        print('[0/2] 1(a) pattern contains invalid regular expressions\n')

    ### tests that solution creates ONE regular expression for each string in l, i.e., length of pattern == length of l
    if len(q2.patterns) == len(l):
        score += 2
        print('[2/2] 1(c) length of pattern == length of l\n')
    else:
        print('[0/2] 1(c) length of pattern != length of l\n')