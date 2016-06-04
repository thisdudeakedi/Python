#rpsls template
#Equating the strings to numbers

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'spoke':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizzard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 5

    return name

name = input('Enter RPSLS ')
name=str(name)
name_to_number(name)
