def name_and_age(name, age):
    return name, 'is', str(age), 'years old'

def show(name, age):
    print name_and_age(name, age)

show('Joe Warren', 52)
show('Scott Rixner', 40)
show('John Greiner', 46)
