# exercice terminé (mais si on rentre un plus grand chiffre que 26 et qu'il y a la lettre "Z" dans le mot en entrée, l'exécution se terminera en IndexError)
from string import ascii_uppercase

print()

# fonction pour séparer les caractères d'un mot
def split(word) :
        return list(word)

def encode_message() :
    splitted_alphabet = split(ascii_uppercase)

    alphabet_list = splitted_alphabet
    double_alphabet_list = splitted_alphabet + splitted_alphabet

    is_message_correctly_inputted = False
    is_going_to_crash = True

    encoded_letter = ""
    encoded_message = ""

    while not is_message_correctly_inputted :
        message_input = input("Entrez en MAJUSCULES le message que vous voulez coder (stop pour arrêter) : ")

        if message_input.isupper() :
            is_message_correctly_inputted = True

        if message_input == "stop" :
            return

    while is_going_to_crash :
        n_input = input("Entrez la clé de codage n (inférieur à 26) : ")

        if int(n_input) <= 26 :
            is_going_to_crash = False

        print()

    for letter_message in message_input :

        for letter_alphabet in alphabet_list :

            if letter_message == letter_alphabet :

                try :
                    encoded_letter = alphabet_list[alphabet_list.index(letter_alphabet) + int(n_input)]

                    encoded_message += encoded_letter

                except :
                    encoded_letter = double_alphabet_list[double_alphabet_list.index(letter_alphabet) + int(n_input)]
                    # print(encoded_letter)

                    encoded_message += encoded_letter

    return encoded_message


print("Message encodé : " + str(encode_message()))
print()