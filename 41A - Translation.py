# input s - string of word
# input t - reversed string s
# if s == t reversed 
# print "YES"
# else print "NO"

s = input()
t = input()

if s == t[::-1]:
    print("YES")
else:
    print("NO")

