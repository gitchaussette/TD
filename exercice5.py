# exercice terminé
from random import randint

print()

def play_bomb_game() :
    random_bomb_coordinates = randint(0, 100)
    is_game_over = False
    nb_lives = 5

    while not is_game_over :
        user_guess = input("Entrez un point entre 0 et 100 : ")
        guess_result = int(user_guess) - random_bomb_coordinates

        if guess_result >= -10 and guess_result <= 0 or guess_result <= 10 and guess_result >= 0 and nb_lives > 0 :
            print(guess_result)
            print("Bravo ! Le point était situé à %d" %random_bomb_coordinates)
            is_game_over = True
        elif nb_lives <= 1 :
            print("Game Over !")
            is_game_over = True
        elif nb_lives == 2 :
            nb_lives -= 1
            print("Non, c'est raté :/, il vous reste %d vie" %nb_lives)
        else :
            nb_lives -= 1
            print("Non, c'est raté :/, il vous reste %d vies" %nb_lives)
    
    return

play_bomb_game()
print()