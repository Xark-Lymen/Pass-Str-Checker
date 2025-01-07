# Password Generator and Checker
This is a basic Password Generator and Strength Checker made in python.

## PASS_GEN
```
import string
import random

if __name__ == "__main__":
    T1 = string.ascii_lowercase
    T2 = string.ascii_uppercase
    T3 = string.digits
    T4 = string.punctuation

    PassLen= int(input("Enter Password Length:- \n"))
    T = []
    T.extend(list(T1))
    T.extend(list(T2))
    T.extend(list(T3))
    T.extend(list(T4))

    print ("Your Password is:- ")
    print ("" .join(random.sample(T, PassLen)))
    
```
## Code STR_CHCKR
```
import string


password = input("Enter your password here:   ")
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters= [upper_case, lower_case, special, digits]

length =  len(password)

score = 0

with open('commonlist.txt', 'r')as f:
    comm= f.read().splitlines()

if password in comm:
    print("Password found in common list. Score= 0/7")
    exit()

if length > 8:
    score+=1
if length > 12:
    score+=1
if length > 16:
    score+=1
if length > 20:
    score+=1

print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score+= 1
if sum(characters) > 2:
    score+= 1
if sum(characters) > 3:
    score+= 1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) -1)} Points!!")  

if score < 4:
    print(f"Input password is weak. Score: {str(score)}/7")
elif score == 4:
    print(f"Input password is mid. Score: {str(score)}/7")
elif 4 < score < 6:
    print(f"Input password is Slightly strong. Score: {str(score)}/7")
elif score > 6:
    print(f"Input password is Strong. Score: {str(score)}/7")
```
