alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext = ""
plaintext = input("Enter your sentence here: ")

while True:
    try:
        shift = int(input("Enter the shift number: ")) % 26
        break
    except ValueError:
        print("Please input a valid number.")

for letter in plaintext:
    if letter.lower() in alphabet:
        x = alphabet.index(letter.lower())
        final_index = x + shift

        if final_index > 25:
            final_index = final_index - 26
        else:
            pass

        if letter.isupper():
            ciphertext += alphabet[final_index].upper()
        else:
            ciphertext += alphabet[final_index]
    else:
        ciphertext += letter

print(ciphertext)
