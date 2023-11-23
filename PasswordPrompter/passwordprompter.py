import argparse

def date_to_numeric_representation(birth_date, length, alternate_flag):
    day, month, year = map(int, birth_date.split('/'))
    numeric_representation = int(f'{year:04}{month:02}{day:02}')

    if alternate_flag:
        # Swap the second and third characters
        numeric_representation = int(f'{year:04}{day:02}{month:02}')

    return str(numeric_representation)[-length:]


def generate_possible_passwords(original_password):
    possible_passwords = []

    # Move the first two characters to the end
    possible_passwords.append(original_password[2:] + original_password[:2])

    # Reverse the order of characters
    possible_passwords.append(original_password[::-1])

    # Swap the first and last characters
    possible_passwords.append(original_password[-1] + original_password[1:-1] + original_password[0])

    # Insert a character at the middle position
    middle_pos = len(original_password) // 2
    possible_passwords.append(original_password[:middle_pos] + 'X' + original_password[middle_pos:])

    # Swap adjacent characters
    for i in range(len(original_password) - 1):
        swapped_password = list(original_password)
        swapped_password[i], swapped_password[i + 1] = swapped_password[i + 1], swapped_password[i]
        possible_passwords.append(''.join(swapped_password))

    # Add a special character at the beginning, middle, and end
    possible_passwords.append('@' + original_password)
    possible_passwords.append(original_password[:middle_pos] + '#' + original_password[middle_pos:])
    possible_passwords.append(original_password + '!')

    # Mix uppercase and lowercase characters
    possible_passwords.append(original_password.lower())
    possible_passwords.append(original_password.upper())

    # Add more variations as needed

    return possible_passwords



def main():
    parser = argparse.ArgumentParser(
        description='Convert a birth date to a numeric representation and generate possible passwords.')
    parser.add_argument('input', help='Birth date in the format "MM/DD/YYYY"')
    parser.add_argument('-l', '--length', type=int, choices=[4, 6, 8], required=True,
                        help='Desired length of numeric representation (4, 6, or 8)')
    parser.add_argument('-a', '--alternate', action='store_true',
                        help='Generate alternate password variant with swapped characters')

    args = parser.parse_args()

    original_password = date_to_numeric_representation(args.input, args.length, args.alternate)

    print(f'Original password: {original_password}')

    possible_passwords = generate_possible_passwords(original_password)

    print('Possible passwords:')
    for password in possible_passwords:
        if len(password) == args.length:
            print(password)


if __name__ == "__main__":
    main()
