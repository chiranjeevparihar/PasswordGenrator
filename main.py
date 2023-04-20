import random
import string 

def gen_pwd(minlen,Num=True,Punc=True):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    char = letters

    if Num:
        char += numbers
    if Punc:
        char += special

    pwd = ""
    criteria = False
    has_num = False
    has_punc = False

    while not criteria or len(pwd) < minlen:
        new_char = random.choice(char)
        pwd += new_char

        if new_char in numbers:
            has_num = True
        elif new_char in special:
            has_punc = True
        
        criteria = True
        if Num:
            criteria = has_num
        elif Punc:
            criteria = criteria and has_punc

    return pwd

minlen = int(input("Enter the length of the pass: "))
has_num = input("Required numbers in pass? y/n: ").lower() == "y"
has_punc = input("Required special char in pass? y/n: ").lower() == "y"

new_pwd = gen_pwd(minlen,has_num,has_punc)
print(new_pwd)
