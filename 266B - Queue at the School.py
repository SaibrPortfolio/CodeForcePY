# strings are numbered from 1 to n where n is the number of elements in the string

# if at time X a "B" is at s[i] and a "G" is at s[i+1]
# then at time make "G" s[i] amd "B" will be s[i+1]

# plain english:
# If the condition for t is met, switch the position of B's and G's
# else: keep the same order

#n, t = map(int, input().split())

n, t = map(int, input().split())

s = input()
new = list(s)

for _ in range(t):
    i = 0
    while i < len(new) - 1:
        if new[i] == "B" and new[i + 1] == "G":
            new[i], new[i + 1] = new[i + 1], new[i]  # Swapping
            i += 2  # Skip next character since we know it's 'B' after swap
        else:
            i += 1  # If no swap, just proceed to next character

s = "".join(new)
print(s)

