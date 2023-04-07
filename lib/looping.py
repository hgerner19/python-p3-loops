#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)
            
        i -= 1
    pass

def square_integers(int_list):
    square_list = list()
    for num in int_list:
        square_int = num * num
        square_list.append(square_int)
    return square_list
    pass

def fizzbuzz():
    i = 1
    while(i <= 100):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: 
            print(i)
        i += 1
    
    pass
