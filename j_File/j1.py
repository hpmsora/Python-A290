print('hello')

#program 1 swapping
subject = raw_input('Enter a quote: ')
print('The program will swap a word in the quote.\n')
word = raw_input('Enter a word for swap: ')
word_replace = raw_input('Enter the replacement: ')

print(subject.replace(word, word_replace))


#program 2 Ice Cream
print('I will ask you for 3 values, and then I will do some math.')
num_frid = input('Number of friends: ')
num_carr = input('Number of carrots: ')
num_doll = input('Number of dollars: ')

print('Number of ice cream: ' + str(2 * num_frid))

print('Number of carrot leftover by 5 people: ' + str(num_carr % 5))

print('Split bill: ' + str(float(num_doll) / num_frid))

#program 3 Next Year Age
name_3 = raw_input('Enter your name: ')
age_3 = input('Enter your age: ')

print(name_3 + ', you will be ' + str(age_3 + 1) + ' next year!')


#program 4 if statement
age_4 = input("Enter your age: ")
if age_4 > 62:
    print('You can get Social Security benefits')

report = raw_input("Enter the statement: ")
if 'large bonuses' in report:
    print('Vacation time!')

hits = input("Enter the hits: ")
shield = input("Enter the shield: ")

if hits > 10 and shield == 0:
    print('You lose... ')


#program 5 Age Eligibility
name = raw_input('Enter the user name: ')
age = input('Enter the age: ')

if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')


#program 6 Numbersize
num = input('Enter a number: ')
if num < 0:
    print('Negative!')

elif num >= 0 and num < 10:
    print('Small!')

elif num >= 10 and num < 100:
    print('Medium!')

else:
    print('Large!')
