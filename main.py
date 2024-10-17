# 2024 - 10 - 17 / PW Generator / NC

import random

# arrays for valid letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# variable to store generated password
generated_password = []

def main():

    print('Welcome to the PW Generator!')

    # getting input for password length
    print('How many characters should the password have? (Minimum 6 - Maximum 128)')
    number_of_characters = int(input('>>> '))
    while number_of_characters < 6 or number_of_characters > 128:
        print('Invalid value. Please try again.')
        number_of_characters = int(input('>>> '))

    # getting input for number of letters in password
    print('How many letters should the password have?')
    print(f'{number_of_characters} letters possible.')
    number_of_letters = int(input('>>> '))
    while number_of_letters < 1 or number_of_letters > number_of_characters:
        print('Invalid value. Please try again.')
        number_of_letters = int(input('>>> '))

    # getting input for number of numbers in password
    print('How many numbers should the password have?')
    print(f'{number_of_characters - number_of_letters} numbers possible.')
    number_of_numbers = int(input('>>> '))
    while number_of_numbers < 1 or number_of_numbers > (number_of_characters - number_of_letters):
        print('Invalid value. Please try again.')
        number_of_numbers = int(input('>>> '))

    # getting input for number of symbols in password
    print('How many symbols should the password have?')
    print(f'{number_of_characters - (number_of_letters + number_of_numbers)} symbols possible.')
    number_of_symbols = int(input('>>> '))
    while number_of_symbols < 1 or number_of_symbols > (number_of_characters - (number_of_letters + number_of_numbers)):
        print('Invalid value. Please try again.')
        number_of_symbols = int(input('>>> '))

    # generating random letters 
    for i in range(number_of_letters):
        random_letter = random.choice(letters)
        generated_password.append(random_letter)

    # generating random numbers 
    for i in range(number_of_numbers):
        random_number = random.choice(numbers)
        generated_password.append(random_number)

    # generating random symbols 
    for i in range(number_of_symbols):
        random_symbols = random.choice(symbols)
        generated_password.append(random_symbols)

    # checking condition if letters, numbers and symbols don't match password length - filling the password with letters
    if number_of_characters > (number_of_letters + number_of_numbers + number_of_symbols):
        fill_of_characters = (number_of_characters - (number_of_letters + number_of_numbers + number_of_symbols))
        print(f'Filling the missing {fill_of_characters} characters with random letters.')
        for _ in range(fill_of_characters):
            random_letter = random.choice(letters)
            generated_password.append(random_letter)

    # scramble the list, joining the values and printing final result
    random.shuffle(generated_password)
    final_password = ''.join(generated_password)
    print('')
    print(final_password)
    print('')

    # storing the password inside a txt file
    with open('passwords.txt', 'w') as store_password:
        store_password.write(final_password)
        store_password.close

if __name__ == '__main__':
    main()