# Check for both uppercase and lowercase letters in a string
# x = "House"
# [print(i) for i in x]
# add a counter for each to keep track of each upper/lowercase letter
# if lower>upper print the whole string in upper and vice versa
# if the amount are the same for both we print in lower (else)

x = input()

upper_counter = 0
lower_counter = 0
for i in x:
    if i.isupper():
        upper_counter += 1
    elif i.islower():
        lower_counter += 1
    else:
        pass

if upper_counter > lower_counter:
    print(x.upper())
elif lower_counter > upper_counter:
    print(x.lower())
else:
    print(x.lower())
