# Printing "Goodbye" with a local message variable

def print_goodbye():
    message = 'Goodbye'
    print message


###################################################
# Tests

message = "Hello"
print message
print_goodbye()
print message

message = "Ciao"
print message
print_goodbye()
print message


# Printing "Goodbye" with a global message variable

def set_goodbye():
    global message
    message = 'Goodbye'
    print message

###################################################
# Tests

message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message

####################################################
count = 1

def reset():
    global count
    count = 0
    #print count
    
def increment():
    global count
    count = count +1
    #print count
    
def print_count():
    global count
    print count
    
def decrement():
    global count
    count = count -1
    #print count

    #1
    #2
    #-2
