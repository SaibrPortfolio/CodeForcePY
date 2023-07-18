# n - number of games played 
# for loop to find how many games are played between A and D
# second input S - consists of the outcome of each game i.e "ADADD"
# example above, output -> D is the winner
# output "Anton or "Danik" to determine winner

n = int(input())

s = input().upper()

a_count = 0
d_count = 0

for letter in s:
    if letter == "A":
        a_count += 1
    else:
        d_count += 1

if a_count > d_count:
    print("Anton")
elif d_count > a_count:
    print("Danik")
else:
    print("Friendship")
