# exercice en cours (je pense je vais recommencer du début parce que là on comprend plus rien)
from random import randint

print()

def elections_problem() :
    NUMBER_OF_VOTERS = 20

    player_list = ["Ashe", "Morty", "Squall", "Neo", "Lara"]
    vote_list = ["Pas bien", "Assez bien", "Bien", "Très bien", "Excellent"]
    random_vote_list = []
    random_player_list = []

    # output_dictionary = {}

    # player_score = 0
    current_index = 0
    player_score_ashe = 0
    player_score_morty = 0
    player_score_squall = 0
    player_score_neo = 0
    player_score_lara = 0

    is_vote_over = False
    # is_vote_count_over = False


    # génération de votes aléatoires
    while not is_vote_over :
        random_player = randint(0, 4)
        random_vote = randint(0, 4)

        random_vote_list.append(vote_list[random_vote])
        random_player_list.append(player_list[random_player])

        # print(random_vote_list)
        # print(random_player_list)

        if len(random_vote_list) == NUMBER_OF_VOTERS :
            is_vote_over = True


    # décompte des voix positives
    for i in random_player_list :

        # GARBAGE CODE
        # list_of_lists_of_lists = []
        # current_vote = random_vote_list[current_index]
        # current_player = random_player_list[current_index]
        # print()
        # print("vote : " + str(current_vote))
        # print("player : " + str(current_player))
        # print()
        # if current_vote == "Bien" or "Très bien" or "Excellent" :
            # player_score += 1

        list_of_zipped_list = [[x, y] for x, y in zip(random_player_list, random_vote_list)]

        # GARBAGE CODE
        # zipped_player = list_of_zipped_list[current_index][0]
        # zipped_vote = list_of_zipped_list[current_index][1]
        # print("zipped plr : " + str(zipped_player))
        # print("zipped vote : " + str(zipped_vote))

    for zipped_vote in list_of_zipped_list :
        if zipped_vote[1] == "Bien" or zipped_vote[1] == "Très bien" or zipped_vote[1] == "Excellent"  :
            if zipped_vote[0] == "Ashe" :
                player_score_ashe += 1
            elif zipped_vote[0] == "Morty" :
                player_score_morty += 1
            elif zipped_vote[0] == "Squall" :
                player_score_squall += 1
            elif zipped_vote[0] == "Neo" :
                player_score_neo += 1
            else :
                player_score_lara += 1
            
            # GARBAGE CODE
            # list_of_lists_of_lists.append(zipped_player)
            # list_of_lists_of_lists.append(player_score)
            # print("zipped vote : " + str(zipped_vote))
            # print("plr score : " + str(player_score))
            # print(list_of_zipped_list)
            # output_dictionary[current_player] = player_score
            # print("index of current player : " + str(output_dictionary[current_player]))
        
        current_index += 1

    print("Ashe : " + str(player_score_ashe))
    print("Morty : " + str(player_score_morty))
    print("Squall : " + str(player_score_squall))
    print("Neo : " + str(player_score_neo))
    print("Lara : " + str(player_score_lara))


    # départage des voix (TODO)


    # GARBAGE CODE
    # for i in output_dictionary :
    # for i in player_list :
    #     print(i)
    #     chosen_player = player_list[random_player]
    #     chosen_vote = vote_list[random_vote]
    #     output_dictionary[chosen_player] = chosen_vote
    #     print(chosen_player)
    #     print(chosen_vote)
    #     print(output_dictionary)


elections_problem()
print()