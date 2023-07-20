# n stops, range from 1 to n

# at every stop, passengers a exits, passengers b enters
# Tram starts empty - 0
# Tram ends empty 
# calculate the Tram's min capacity, so passengers never exceeds it
# exit happens before entering
# noone enters at last stop

# n - number of stops
# i - amount of passengers each stop
# a*i = exit b*i = enter

# algorithm:
# read the first line and save as n
# create an empty list
# do n times:
#   read a(i) and b(i) and save it in empty list
# init max_number = 0
# init person = 0
# loop through list:
#   person - a(i) + b(i)
#   when max_number < person:
#       max_number = person
# print(max_number)


n = int(input())

max_number = 0
person_counter = 0
array = []


for stops in range(1, n + 1):
    passengers = list(map(int, input().split()))
    array.append(passengers)

for a in array:
    person_counter = person_counter - a[0] + a[1]
    if max_number < person_counter:
        max_number = person_counter

print(max_number)
