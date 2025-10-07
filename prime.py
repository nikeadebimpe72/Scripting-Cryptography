#!/usr/bin/env python3

def prime_num(num):   
        if num <= 1:
         return False
         
        for i in range(2, int(num ** 0.5) + 1):
             if num% i == 0:
                return False
        return True    
for number in range(1, 101):
    if prime_num(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    
        