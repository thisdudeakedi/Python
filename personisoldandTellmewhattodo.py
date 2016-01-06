#two functions to determin your age and what to do

def person_is_old(age):     #determines your age and passes either true or false
    if age >=50:
        return True
    else:
        return False

def tell_me_what_to_do(age):  
    if person_is_old(age):  #takes either true or false from 1st function
        print ('You deserve to have a long vacation Sir!')
    else:
        print ('Go to work son!')
