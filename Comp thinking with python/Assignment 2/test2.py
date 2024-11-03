import re

class Q2:

    def crossword_puzzle(self, s, l):
        ### DO NOT EDIT THIS PART ###
        self.m = len(s.split("\n"))
        self.n = len(s.split("\n")[0]) if self.m > 0 else 0

        # part 1: prepare the pattern variable
        self.pattern = []  # list of patterns to be used for part 2
        self.line_pattern = r"(\w) in the (\d+) position"  # regex to extract character and position

        for instructions in l:
            if "length" not in instructions:
                # Direct word pattern with word boundaries
                pattern = r"\b" + re.escape(instructions) + r"\b"
                self.pattern.append(pattern)
            else:
                # Extract character-position pairs
                matches = re.findall(self.line_pattern, instructions)
                length_match = re.search(r'length (\d+)', instructions)
                if length_match:
                    length = int(length_match.group(1))
                    # Initialize pattern with wildcards
                    pattern_chars = ['.'] * length
                    for char, pos in matches:
                        pos = int(pos)
                        if 0 <= pos < length and pos < self.n:
                            pattern_chars[pos] = re.escape(char)
                        else:
                            print(f"Warning: Position {pos} out of bounds for length {length} and grid columns {self.n}")
                    # Create regex pattern for the word
                    regex = '^' + ''.join(pattern_chars) + '$'
                    self.pattern.append(regex)

        # part 2: extract all possible sequences (rows, columns, diagonals)
        grid = [list(line) for line in s.split("\n")]

        # Extract rows
        rows = [''.join(row) for row in grid]

        # Extract columns
        columns = [''.join([grid[r][c] for r in range(self.m)]) for c in range(self.n)]

        # Extract main diagonals (top-left to bottom-right)
        main_diagonals = []
        for k in range(-self.m + 1, self.n):
            diagonal = ''.join([grid[r][c] for r in range(self.m) for c in range(self.n) if c - r == k])
            if len(diagonal) >= 1:
                main_diagonals.append(diagonal)

        # Extract anti-diagonals (top-right to bottom-left)
        anti_diagonals = []
        for k in range(self.m + self.n -1):
            diagonal = ''.join([grid[r][c] for r in range(self.m) for c in range(self.n) if r + c == k])
            if len(diagonal) >= 1:
                anti_diagonals.append(diagonal)

        # Combine all sequences
        all_sequences = rows + columns + main_diagonals + anti_diagonals

        # Compile all patterns
        compiled_patterns = [re.compile(pat) for pat in self.pattern]

        matched_words = set()

        # Check each sequence against all patterns
        for pat in compiled_patterns:
            for sequence in all_sequences:
                matches = pat.findall(sequence)
                for match in matches:
                    # If the pattern uses word boundaries or exact matching, match will be the word
                    if isinstance(match, str):
                        matched_words.add(match)
                    elif isinstance(match, tuple):
                        # In case of multiple groups, join them
                        matched_word = ''.join(match)
                        matched_words.add(matched_word)

        if matched_words:
            return list(matched_words)
        else:
            return ["No match found"]

# Example Usage:

if __name__ == "__main__":
    q2 = Q2()
    s = '''abc
gar
tvd'''
    l = [
        'bat',
        'a length 3 word with c in the 0 position, a in the 1 position, t in the 2 position',
        'a length 3 word with a in the 1 position, t in the 2 position'
    ]
    result = q2.crossword_puzzle(s, l)
    print(result)  # Expected Output: ["cat"]