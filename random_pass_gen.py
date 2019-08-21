from random import choice
from string import ascii_letters, digits, punctuation


def password_generator(length=16):

    chars = tuple(ascii_letters) + tuple(digits) + tuple(punctuation)
    return ''.join(choice(chars) for x in range(length))



def alternative_password_generator(ctbi, i):

    pass  # Put your code here...


def random_number(ctbi, i):
    pass  # Put your code here...


def random_letters(ctbi, i):
    pass  # Put your code here...


def random_characters(ctbi, i):
    pass  # Put your code here...


def main():
    length = int(
        input('Please indicate the max length of your password: ').strip())
    print('Password generated:', password_generator(length))



if __name__ == '__main__':
    main()
