# creating functions needed for the task
def add_ascii_upp(i):
    added_num= (ord(i) + 15 - 65) % 26 + 65
    return chr(added_num)

def add_ascii_low(i1):
    added_num= (ord(i1) + 15 - 97) % 26 + 97
    return chr(added_num)

def is_it_a_upp(input_chr):
    x = ord(input_chr)
    if x >= 65 and x <= 90:
        return True
    else:
        return False
    
def is_it_a_low(second_input_chr):
    lower_case = ord(second_input_chr)
    if lower_case >= 97 and lower_case <= 122:
        return True
    else:
        return False

def is_it_a_sp_chr(third_input_chr):
    special_chr = ord(third_input_chr)
    if special_chr >= 32 and special_chr <= 64:
        return True
    else:
        return False

def is_it_a_sp_chr2(fourth_input_chr):
    special_chr2 = ord(fourth_input_chr)
    if special_chr2 >= 91 and special_chr2 <= 96:
        return True
    else:
        return False
encrypted_string = ""
# asking to input the sentence to encrypt
plain_text = input("Please enter the sentence to encrypt: ")

# iterate over the inputed sentence
for i in range(len(plain_text)):
    character1= (plain_text[i])

    # check if character is uppercase 
    is_it_a_upp(character1)
    result_upp = is_it_a_upp(character1)
    if result_upp == True:
        encrypted_character = add_ascii_upp(character1)
        encrypted_string = encrypted_string + encrypted_character
    
    # check if character is lowercase   
    is_it_a_low(character1)
    result_low = is_it_a_low(character1)
    if result_low == True:
        encrypted_character1 = add_ascii_low(character1)
        encrypted_string = encrypted_string + encrypted_character1
        
    # check if character is special character
    is_it_a_sp_chr(character1)
    result_sp_ch = is_it_a_sp_chr(character1)
    if result_sp_ch == True:
        encrypted_character2 = character1
        encrypted_string = encrypted_string + encrypted_character2
    is_it_a_sp_chr2(character1)
    result_sp_ch2 = is_it_a_sp_chr2(character1)
    if result_sp_ch2 == True:
        encrypted_character3 = character1
        encrypted_string = encrypted_string + encrypted_character3
        
print("The encrypted sentence is:            " + encrypted_string)






   






