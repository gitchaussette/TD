# exercice terminé
from random import randint

print()

def play_number_game() :
    random_number = randint(1,100)
    is_game_over = False
    number_of_tries = 1

    # décommenter pour savoir le nombre aléatoire (tricheur !)
    # print(random_number)

    while not is_game_over :
        try :
            user_guess = input('Entrez un nombre entier entre 1 et 100 ("stop" pour arrêter) : ')

            if user_guess == "stop" :
                is_game_over = True
            elif random_number > int(user_guess) and int(user_guess) >= 1 :
                print("Le nombre est plus grand.")
                number_of_tries += 1
            elif random_number < int(user_guess) and int(user_guess) <= 100 :
                print("Le nombre est plus petit.")
                number_of_tries += 1
            elif int(user_guess) < 1 or int(user_guess) > 100 :
                print("Au moins c'est un nombre entier, mais il faut qu'il soit compris entre 1 et 100...")
            else :
                print("GG ! Vous avez trouvé le nombre en %d coups" %number_of_tries)
                is_game_over = True
        except :
            print("Non, ce n'est pas un nombre entier !")
        
    return

play_number_game()
print()