import re

# Given array
array = [
    'bat',
    'a length 3 word with c in the 0 position, a in the 1 position, t in the 2 position',
    'a length 3 word with a in the 1 position, t in the 2 position'
]

s = '''abc
gar
tvd
cat''' 

pattern = []  # list of patterns to be used for part 2
### REPLACE THE BELOW LINES WITH YOUR CODE ###
line_pattern = r"(\w) in the (\d+) position"

for instructions in array:
    if "length" not in instructions:
        pattern.append(r"\b" + re.escape(instructions) + r"\b")
    else:
        matches = re.findall(line_pattern, instructions)
        length_match = re.search(r'length (\d+)', instructions)
        if length_match:
            length = int(length_match.group(1))
            regex = '^' + ''.join(
                [re.escape(m[0]) if pos < len(matches) and int(m[1]) == pos else '.' 
                 for pos in range(length)
                 for m in matches if int(m[1]) == pos]
            ) + '$'
            pattern.append(regex)

for pat in pattern:
    compiled_pat = re.compile(pat)
    for line in s.splitlines():
        match = compiled_pat.findall(line)
        if match:
            print(match)