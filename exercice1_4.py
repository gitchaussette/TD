# exercice en cours (je ne suis pas sûr d'être parti dans la bonne direction, je crois que c'est un début d'usine à gaz en plus)
print()

fifty = 50
twenty = 20
zero = 0

def calculate_darts_probability(max_points=300) :
    fifty_list = []
    twenty_list = []
    zero_list = []

    list_of_lists = [fifty_list, twenty_list, zero_list]

    for i in range(1, 11) :
        times_fifty = fifty * i

        fifty_list.append(times_fifty)

    for i in range(1, 11) :
        times_twenty = twenty * i

        twenty_list.append(times_twenty)

    for i in range(1, 11) :
        times_zero = zero * i

        zero_list.append(times_zero)

    for i in list_of_lists :
        print(i)

    # for i in range(1, 11) :
    #     if max_points == fifty_list[i-1] + twenty_list[i-1] + zero_list[i-1] :
    #         print("egg")

    # for i in list_of_lists :
    #     for i in list_of_lists[0] :
    #         print(i)
        
    #     for i in list_of_lists[1] :
    #         print(i)

    #     for i in list_of_lists[2] :
    #         print(i)
    
    # print(list_of_lists)


calculate_darts_probability()