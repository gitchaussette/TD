# exercice en cours
from string import ascii_uppercase

print()

# fonction pour séparer les caractères d'un mot
def split(word) :
        return list(word)

def encode_message() :
    splitted_alphabet = split(ascii_uppercase)

    alphabet_list = splitted_alphabet
    double_alphabet_list = splitted_alphabet + splitted_alphabet

    n_list = []
    double_n_list = []

    is_message_correctly_inputted = False
    is_going_to_crash = True

    current_index = 0

    encoded_letter = ""
    encoded_message = ""

    while not is_message_correctly_inputted :
        message_input = input("Entrez en MAJUSCULES le message que vous voulez coder (stop pour arrêter) : ")

        if message_input.isupper() :
            is_message_correctly_inputted = True

        if message_input == "stop" :
            return

    while is_going_to_crash :
        n_input = input("Entrez la clé de codage n (en MAJUSCULES) : ")

        if type(n_input) == type("") :
            is_going_to_crash = False

        print()

    for letter_n_input in n_input :

        for letter_alphabet in alphabet_list :

            if letter_n_input == letter_alphabet :

                    n_list.append(alphabet_list.index(letter_alphabet))
                    print(n_list)

    for letter_message in message_input :

        for letter_alphabet in alphabet_list :

            if letter_message == letter_alphabet :

                # try :
                #     encoded_letter = alphabet_list[n_list[current_index]]
                #     print(encoded_letter)
                #     encoded_message += encoded_letter
                #     current_index += 1
                #     print(current_index)
                # except :
                #     pass

                # try :
                #     encoded_letter = alphabet_list[alphabet_list.index(letter_alphabet) + int(n_list[current_index])]
                #     encoded_message += encoded_letter
                # print("alphabet_list[alphabet_list.index(letter_alphabet)]) : " + str(alphabet_list[alphabet_list.index(letter_alphabet)]))
                # print("n_list[current_index]) : " + str(n_list[current_index]))
                # print("encoded_letter : " + str(encoded_letter))
                #     current_index += 1
                # except :
                #     encoded_letter = double_alphabet_list[alphabet_list.index(n_list[current_index])]
                #     encoded_message += encoded_letter
                #     current_index += 1

    # return encoded_message





    # for letter_message in message_input :

    #     for letter_alphabet in alphabet_list :

    #         if letter_message == letter_alphabet :




print("Message encodé : " + str(encode_message()))
print()