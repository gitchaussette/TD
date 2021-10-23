# exercice terminé
from random import randint

print()

def play_number_game() :
    random_number = randint(1,100)

    is_game_over = False

    number_of_tries = 1

    # print(random_number)

    while not is_game_over :

        try :
            user_guess = input('Entrez un nombre entier entre 1 et 100 ("stop" pour arrêter) : ')

            if user_guess == "stop" :
                is_game_over = True

            elif random_number > int(user_guess) and int(user_guess) >= 1 :
                number_of_tries += 1

                print("Le nombre est plus grand.")

            elif random_number < int(user_guess) and int(user_guess) <= 100 :
                number_of_tries += 1

                print("Le nombre est plus petit.")

            elif int(user_guess) < 1 or int(user_guess) > 100 :
                print("Au moins c'est un nombre entier, mais il faut qu'il soit compris entre 1 et 100...")

            else :
                is_game_over = True

                print("GG ! Vous avez trouvé le nombre en %d coups" %number_of_tries)

        except :
            print("Non, ce n'est pas un nombre entier !")

    return


play_number_game()
print()