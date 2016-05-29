#receives and returns input of name and age

def name_and_age(name,age):
    print 'Enter your name'
    name=raw_input()
    name=str(name)
    print 'Enter your Age'
    age=raw_input()
    age=int(age)
    return name, age

#calls input of name and age and prints it

def show_name_and_age(name,age):
    print name_and_age(name,age)
    print name, 'is', age, 'years old'
    
show_name_and_age(0,0)


