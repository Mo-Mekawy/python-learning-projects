import string
from random import shuffle


def main():
    # store all characters in lists (upper/lower case, digits, punctuations)
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    # get number of characters from user
    characters_num = get_valid_num()
    # shuffle all lists
    shuffle(s1)
    shuffle(s2)
    shuffle(s3)
    shuffle(s4)
    # calculate 30% and 20% of characters' number
    part1 = round(characters_num * 30 / 100)
    part2 = round(characters_num * 20 / 100)

    # create password 60% letters and 40% digits and punctuations
    password = []

    j = 0
    for i in range(part1):
        if i >= len(s1) or i >= len(s2):
            i = 0
        password.append(s1[i])
        password.append(s2[i])
        if j == part1:
            break
        j += 1

    j = 0
    for i in range(part2):
        if i >= len(s3) or i >= len(s4):
            i = 0
        password.append(s3[i])
        password.append(s4[i])
        if j == part2:
            break
        j += 1

    shuffle(password)
    print(*password, sep="")


def get_valid_num():
    while True:  # make sure input is an integer that is >= 6
        try:
            characters_number = int(
                input("how many characters for the password? "))
        except ValueError:
            print("expecting an interger more than or equal to 6")
        else:
            if characters_number < 6:
                print("expecting an interger more than or equal to 6")
                continue
            else:
                return characters_number


main()
