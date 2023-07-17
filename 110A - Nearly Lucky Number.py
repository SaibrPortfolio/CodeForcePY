# read input
# init counter
# go through string and count the 4s and 7s

# go through the counter and check if every digit is a 4 or 7
# if every digit is a 4 or 7 -> "YES" otherwise "NO"

n = input()

count = 0

for num in n:
    if num == "4" or num == "7":
        count += 1

counter = 0

for num in str(count):
    if num == "4" or num == "7":
        counter += 1

if counter == len(str(count)):
    print("YES")
else:
    print("NO")