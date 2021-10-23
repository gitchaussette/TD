# exercice terminé
from random import randint

print()

def d4_game(bet=2) :
    first_d4 = randint(1, 4)
    second_d4 = randint(1, 4)

    money_earned = 0

    print("Vous misez %d €." %bet)

    if first_d4 == second_d4 :
        money_earned = bet + first_d4 + second_d4

        print("Premier dé : " + str(first_d4))
        print("Second dé : " + str(second_d4))
        print("Vous avez gagné %d € !" %money_earned)

    else :

        print("Vous perdez votre mise. :/")

    return money_earned


d4_game()
print()