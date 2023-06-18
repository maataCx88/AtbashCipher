from operator import length_hint


Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m']
Alphabet2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
sentence=input("Welcome to my Atbash Cipher Encryptor, Please enter a sentence to be encrypted :")
builder=""
for character in sentence:
    if not(character.isupper()):          
         if character in Alphabet:
             i=Alphabet.index(character)
             builder += Alphabet2[len(Alphabet2)-i-1]
         else:
             if character in Alphabet2:
                     i=Alphabet2.index(character)
                     builder += Alphabet[len(Alphabet)-i-1]
             else:
                     builder+=character
    else:
        character=character.lower()
        if character in Alphabet:
             i=Alphabet.index(character)
             builder += Alphabet2[len(Alphabet2)-i-1].upper()
        else:
             if character in Alphabet2:
                     i=Alphabet2.index(character)
                     builder += Alphabet[len(Alphabet)-i-1].upper()
print(builder)


