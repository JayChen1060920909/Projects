# Project Name: Project generator
# Creator: Jay Chen
# Create Date: 2017/8/15

import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd
min_length = int(input("請輸入最小數字:"))
has_number = input("請問你要有數字嗎(y/n):?").lower() == 'y'
has_special = input("請問你要新增特殊符號嗎(y/n):?").lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)

print(pwd)