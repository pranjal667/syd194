total = 0
for i in range(5):
    for j in range(3):
        if i+j == 5:
            total +=i+j
        else:
            total -= i-j    
            
counter=0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2              

print("Counter:", counter)
print("Total:", total)

# Step 2: Simplified encryption function

original_code=""""""
def encrypt(text, key):
    encrypted_text=""
    for char in text:
        if char.isalpha():
            shifted= ord(char)+key
            if char.islower():
                if shifted>ord('z'):
                    shifted -=26
                elif shifted< ord('a'):
                    shifted+=26
            elif char.isupper():
                if shifted>ord('Z'):
                    shifted -=26
                elif shifted< ord('A'):
                    shifted+=26
            encrypted_text += chr(shifted)
        else:
            encrypted_text +=char
    return encrypted_text
key=total ##?????????????
encrypted_code=encrypt(original_code, key)
print("encrypted_code")
print(encrypted_code)

encrypted_code="""""
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1' , 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5] 

    juvyr ybpny_inevnoyr › 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir (ybpny_inevnoyr)
        ybpny_inevnoyr -= 1
    erghea ahzoref

zl_frg={1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag（v）
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag (tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)"""""

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key=total
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)
print(' ')
print('End of CODE')
print(' ')

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    local_variable = 5

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.discard(local_variable)
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(my_set.copy())

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict()

def update_global():
    global global_variable
    global_variable += 10


print("Global Variable:", global_variable)
print("Dictionary:", my_dict)
print("Set:", my_set)
for i in range(5):
    print(i)

if my_set is not None and my_dict.get('key4') == 10:  # Check using get() for key existence
    print("Condition met!")

if 5 not in my_set:
    print("5 not found in the set!")
