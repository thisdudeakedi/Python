# rpsls template
# Equating the strings to numbers

def name_to_number(choice):
    if choice == 'rock':
        return 0
    elif choice == 'spoke':
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
        return 'spoke'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'lizard'
    elif choice == 4:
        return 'scissors'
    else:
        return 'none'

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
        name_or_number()
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

name_or_number()

