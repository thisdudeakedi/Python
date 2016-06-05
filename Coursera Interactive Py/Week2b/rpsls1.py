from random import randrange
# rpsls template
# Equating the strings to numbers

def name_to_number(choice):
    if choice == 'rock':
        return 0
    elif choice == 'spock':
        return 1
    elif choice == 'paper':
        return 2
    elif choice == 'lizard':
        return 3
    elif choice == 'scissors':
        return 4
    else:
        return 5

def number_to_name(choice):
    if choice == 0:
        return 'rock'
    elif choice == 1:
        return 'spock'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'lizard'
    elif choice == 4:
        return 'scissors'
    else:
        return 'null'

def enter_choice():
    print'Enter RPSLS '
    name = raw_input()
    print name_to_number(name)
    play_again()

def enter_number():
    print'Enter Number 1-5 to discover choice '
    number = raw_input()
    number = int(number)
    print number_to_name(number)
    play_again()

def play_again():
    print 'Play again?'
    again = raw_input()
    if again == 'y':
        rpsls()
    else:
        stop()

def stop():
    print 'thank you for playing'


def name_or_number():
    print 'Name or Number ?'
    choice = raw_input()
    if choice == 'name':
        print enter_choice()
    elif choice == 'number':
        print enter_number()
    else:
        print 'not an option, options are number or name'

def rpsls():
    print 'Enter rock, paper, scissors, lizard or spock'
    choice = raw_input()
    print 'Player chooses', choice
    irand = randrange(0,4+1)
    comp = number_to_name(irand)
    print 'Computer chooses', comp
    number = name_to_number(choice)
    if number == 5:
        print 'bad choice'
        print play_again()
    else:
        difference = (number - irand) % 5
        if difference == 0:
            print 'for debugging difference is', difference
            print 'Default Player wins'
            print play_again()
        elif difference == 1 or difference == 2:
            print 'for debugging difference is', difference
            print 'Player wins'
            print play_again()
        else:
            print 'for debugging difference is ', difference
            print 'Computer wins'
            print play_again()

#name_or_number()
rpsls()
