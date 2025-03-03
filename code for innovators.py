
#1
def sum_of_multiples(n):
    if n < 0:
        return 0  
    
    total = 0
    for x in range(n):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    
    return total

print(sum_of_multiples(10))


#2
import re

def to_camel_case(text):
    words = re.split('[-_]', text)  
    return words[0] + ''.join(word.capitalize() for word in words[1:])

print(to_camel_case("the-stealth-warrior"))  
print(to_camel_case("The_Stealth_Warrior"))  
print(to_camel_case("The_Stealth-Warrior"))  


#3
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

print(remove_vowels("This website is for losers LOL!"))  


#4
def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda word: sorted(word)))

print(order("is2 Thi1s T4est 3a"))  
print(order("4of Fo1r pe6ople g3ood th5e the2"))  
print(order(""))  

#5
def sort_odd_numbers(arr):
    odds = sorted([num for num in arr if num % 2 != 0]) 
    odd_index = 0
    
    result = []
    for num in arr:
        if num % 2 != 0:
            result.append(odds[odd_index])  
            odd_index += 1
        else:
            result.append(num)  
    
    return result

print(sort_odd_numbers([7, 1]))  
print(sort_odd_numbers([5, 8, 6, 3, 4]))  
print(sort_odd_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  




