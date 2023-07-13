
n, k = map(int, input().split())

# n, k = 512 4
# if the the last digit is non-zero, do -1 until it is
# should be 510 and k = 2
# if the last digit is zero, divide by ten 
# should be 51 and k = 2
# repeating the first step should be n = 50 and k = 0
# Output should be n = 50

while (k >= 1):
    if n % 10 != 0:
        n = n - 1
        k -= 1
    elif n % 10 == 0:
        n = n // 10
        k -= 1
    else:
        pass

print(n)
