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
    
