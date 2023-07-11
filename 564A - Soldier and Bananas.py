# w = bananas
# k = cost of banana
# n = money of the soldier

# output = borrowed money of solder

# Algorithm: 
# - Read input and split it in 3 integers
# w, k, n = map(int, input().split())

#     - k = cost of first banana
#     - n = money of the soldier
#     - w - number of bananas he wants

# - get the costs
#     - costs = 1*k + 2*k + ... w*k

# - borrowed = costs - n
# - if borrowed < 0 -> borrow = 0 

# - output "borrowed"

k, n, w = map(int, input(). split())

costs = 0

for i in range(1, w + 1):
    costs = costs + k * i

borrowed = costs - n

if borrowed < 0:
    borrowed = 0
print(borrowed)


