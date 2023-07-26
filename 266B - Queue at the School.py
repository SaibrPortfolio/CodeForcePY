# strings are numbered from 1 to n where n is the number of elements in the string

# if at time X a "B" is at s[i] and a "G" is at s[i+1]
# then at time make "G" s[i] amd "B" will be s[i+1]

# plain english:
# If the condition for t is met, switch the position of B's and G's
# else: keep the same order

#n, t = map(int, input().split())

s = "BGGBG"
new = list(s)

for i, char in enumerate(new):
    if char == "B":
        char = "G"


