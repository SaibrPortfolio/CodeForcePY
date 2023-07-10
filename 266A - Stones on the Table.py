n = int(input())
s = input()

if n != len(s):
    exit

count = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
        
print(count)
