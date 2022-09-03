'''get user's birth date and print it in minutes in words'''
from datetime import date, datetime
import sys


num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
             90: 'Ninety', 0: 'Zero'}

num_word = []


def main():
    '''transfer minutes in numerals to words'''
    minutes = get_time_in_min()  # get minutes in type int and format it with ,
    turn_num_to_word(minutes)
    for word in num_word:
        print(word, end="")
    print("minutes")


def get_time_in_min():
    '''get input from user in the format of a date'''
    time = input("Date of Birth: ").strip()
    try:
        time = datetime.strptime(time, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date")
        print("usage:year-month-day")
        sys.exit()

    today = date.today()
    # get number of days that the user has lived
    time_in_days = (today-time).days
    return time_in_days * 24 * 60  # return that number in minutes


def turn_num_to_word(n):
    comma_count = 0
    working_num = f"{n:,}"
    for i in working_num:
        if "," == i:
            comma_count += 1

    match comma_count:
        case 2:
            million(working_num)

        case 1:
            thousand(working_num)
            working_num = working_num[working_num.index(",") + 1:]
        case 0:
            num_word.append(number(working_num).lower())


def number(n):
    if int(n) >= 100:
        hundred = num2words[int(n[0])] + " hundred "  # get the hundreds value
        word = hundred + number(n[1:]) if number(n[1:]) != "zero" else hundred
    else:
        num = int(n)
        try:
            word = num2words[num].lower()
        except KeyError:
            word = (num2words[num - num % 10] +
                    "-" + num2words[num % 10]).lower()
    return word


def million(n):
    num_word.append((number(n[:n.index(",")]) + " million, ").capitalize())
    n = n[n.index(",") + 1:]
    thousand(n)


def thousand(n):
    num_word.append((number(n[:n.index(",")]) + " thousand, ").capitalize())
    n = n[n.index(",") + 1:]
    num_word.append(number(n).lower())


if __name__ == "__main__":
    main()
