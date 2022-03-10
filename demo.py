from functools import total_ordering


first_name = 'Caleb'
last_name = "Ricks"
print(first_name)
print(last_name)

# by no means is this list comprehensive
favorite_games = '''
Skyrim, 
Diablo II, 
Warcraft III, 
Northgard, and 
Ark: Survival Evolved
'''
print(favorite_games)

age = 25
hourly_rate = 420.69
likes_dogs = True

print(type(age))
print(type(likes_dogs))
print(type(hourly_rate))

if likes_dogs == True:
    print('You have a soul.')

open_file = open("FinalGrades.csv")

total_a = 0
total_b =0
total_c = 0

for line in open_file:
    line = line.rstrip('\n').split(',')
    for value in line:
        if value == 'A':
            total_a +=1
        elif value == "B":
            total_b +=1
        elif value == "C":
            total_c +=1
print("A's:", total_a)
print("B's:",total_b)
print("C's:",total_c)
print(line[len(line) - 1])
open_file.close()

open_file2 = open("orders.csv")

big_orders = 0
small_orders = 0

for line in open_file2:
    line = line.rstrip('\n').split(',')
    for value in line:
        if int(line[1]) > 30:
            big_orders +=1
        else:
            small_orders +=1
open_file2.close()

print(big_orders)
print(small_orders)
