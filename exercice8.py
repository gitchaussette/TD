# exercice en cours
from random import randint

print()

def elections_problem() :
    player_list = ["Ashe", "Morty", "Squall", "Neo", "Lara"]
    vote_list = ["Pas bien", "Assez bien", "Bien", "Très bien", "Excellent"]
    output_dictionary = {}

    random_player = randint(0, 4)
    random_vote = randint(0, 4)

    for i in player_list :
        print(i)
        chosen_player = player_list[random_player]
        chosen_vote = vote_list[random_vote]

        output_dictionary[chosen_player] = chosen_vote

        print(chosen_player)
        print(chosen_vote)
        print(output_dictionary)


elections_problem()