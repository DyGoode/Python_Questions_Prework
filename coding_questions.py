#1 Write a function to print "hello_USERNAME!"
def hello_name(user_name):
    print("Hello_" + user_name.upper() + "!")
hello_name("girl")



#2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
        numbers = list(range(0,100))
        for number in numbers: 
            if number % 2 !=0:
                print(number)



#3Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
        a_list.sort()
        print(a_list[-1])
        

max_num_in_list([2, 4, 6, 8])



#4 Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 400 == 0 and a_year % 100 == 0:
            return True
        else:
            return False
    else:
        return False



#5 Write a function to check to see if all numbers in list are consecutive numbers. 
def is_consecutive(a_list):
    min_number = min(a_list)
    max_number = max(a_list)
    a_list.sort()
    for number in a_list:
        if number == min_number:
            min_number += 1
        else:
            return False
        last_number = number
    if last_number == max_number:
        return True
    else:
        return False
print(is_consecutive)
is_consecutive([7, 6, 9, 5, 8])
