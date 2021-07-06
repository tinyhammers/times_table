import time

print('Which number table are you learning?')

# Take the number input and convert to integer
table = int(input())

# Print text with table var as a string 
print('OK, lets try the ' + str(table) + ' times table')

# Loop through i with the range 1-13 to give 12 values. Start at 1 as we don't
# want to multiply by 0
for i in range(1, 13):
    # Print the value of i (1-13) as a string, then value of table as a string
    # then the vaue of table and i as a string
    print(str(i) + ' x ' + str(table) + ' = ?')
    answer = input()
    while answer != str(table * i):
        print('That wasn\'t right. Try again')
        print(str(i) + ' x ' + str(table) + ' = ')
        answer = input()
    print('Correct!')

print('That\'s the ' + str(table) + ' times table!')
