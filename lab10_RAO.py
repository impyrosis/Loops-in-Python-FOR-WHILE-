# 1. Print individual letters of a string using the FOR LOOP. Enter value using input () command.

a = input('Please input a string of your choice: ')
for l in a:
    print(l)

# 2. Make a program using FOR LOOP to iterate over a Python list and display it using the print command. The list should have at least 5 elements.

print('------------- print a list using FOR LOOP ----------------')
different_weathers = ['Winter', 'Summer', 'Spring', 'Autumn','Monsoon', 'Windy'] # create a list with []

for g in different_weathers:
    print(g)

print('------------- print a tuple using FOR LOOP ----------------')
weathers_tuple = ('Winter', 'Summer', 'Spring', 'Autumn','Monsoon', 'Windy') # create a tuple ()

for i in range(len(weathers_tuple)):
    print(f'{i} {weathers_tuple[i]}')


# 3. Make a program using FOR LOOP to find the sum of all integer numbers stored in a list.

a = [16, 14, 7, 35, 919, 425, 12, 11]

# create a variable to store the sum

b = 0

# iterate over the list of numbers and add them

for i in a:
    b = b + i

print('------------- print the sum of the list of numbers ----------------')
print(f'The sum is: {b}')

# 4. Make a program using WHILE LOOP to start at 1 and stop at 1000.


a = 1
while a <= 1000:
    print(a)
    a = 1 + a

# 5. Make an infinite loop using WHILE LOOP.

# EXAMPLE OF INFINITE LOOP

print('------------- WHILE LOOP----------------')
num = 10
var = 10
while num:  # while number is true
    var = var + 1
    print(var)