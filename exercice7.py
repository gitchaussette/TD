# exercice en cours (j'étais parti sur les chapeaux de roues, j'ai plein d'idées sur une feuille mais ça bloque sur les boucles)
def ask_input_return_anagrams() :
    str_input = input("Entrez un mot : ")
    index = 0

    input_list = [str(i) for i in str_input]
    list_range = len(input_list)-1

    print(list_range)

    # peut-être utiliser un while ?
    for i in input_list :
        print(input_list.index(i))
        print(input_list)


    # for i in input_list :
    #     for i in input_list :
    #         anagram = "anagramme n°" + index + ???
    #         index += 1


    # version "normale" de la liste de compréhension "input_list" pour montrer que je ne l'ai pas juste volée sur stackoverflow
    # input_list = []
    # for i in str_input :
    #     input_list.append(str(i))

ask_input_return_anagrams()