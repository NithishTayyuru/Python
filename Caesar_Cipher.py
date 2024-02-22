alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabets.index(letter)
        new_position=position+shift_amount
        if new_position>25:
            new_position-=26
        new_letter=alphabets[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
def decrypt(cipher_text,shift_amount):
    decoded_text=""
    for letter in cipher_text:
        position=alphabets.index(letter)
        new_position=position-shift_amount
        new_letter=alphabets[new_position]
        decoded_text+=new_letter
    print(f"The decoded text is {decoded_text}")
if direction=="decode":
    decrypt(text,shift)
else:
    encrypt(text,shift)
    