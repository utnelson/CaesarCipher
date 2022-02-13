import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Shifted alle buchstaben um einen bestimmten wert nach rechts oder nach links
def caesar(cipher_text, cipher_shift, cipher_direction):
    caesar_text = ""
    #Durchlaufe jeden Buchstaben im Text
    for letter in cipher_text:
        # Nur wenn es ein Buchstabe aus dem Alphabet ist
        if letter in alphabet:
            position = alphabet.index(letter)
            #Check Richtung der Verschlüsselung
            if cipher_direction == "encode":
                new_position = position + cipher_shift
            elif cipher_direction == "decode":
                new_position = position - cipher_shift
            # Der neue Buichstabe wird der geschobene Buchstabe
            new_letter = alphabet[new_position]
            caesar_text += new_letter
            # Wenn Symbol nicht im Alphabet dann Buchstabe einfach ohne shifting übernehmen
        else: 
            caesar_text += letter
    print(f"The {cipher_direction}d Code is: {caesar_text}")


print(caesar_art.logo)

end_of_programm = False
# While loop für endlosschleife, wird auf True gesetzt wenn Ende input mit no beantwortet wird
while  not end_of_programm:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Wenn SHift über 26 ist, dann Modulos anwenden
    new_shift = shift % 26

    caesar(cipher_text = text, cipher_shift = new_shift, cipher_direction = direction)

    restart = input("Would you like to restart the program??? Yes or No\n").lower()
    if restart == "no":
        end_of_programm = True
