
print()

# fonction qui transforme le string entré par l'utilisateur en liste
def ask_input_return_list() :
    int_string = input("Entrez des chiffres (séparés par des virgules et sans espaces) : ")

    int_list = int_string.split(",")

    return int_list

inputted_list = ask_input_return_list()
print()


# 1.1
print(inputted_list)
print()


# 1.2
def return_index_and_values(list) :
    index_list = []
    values_list = []

    for i in list :

        # IDEE : utiliser une fonction pour tej la valeur de la liste d'origine après chaque occurence (pour régler le problème des mauvais index)
        index_list.append(list.index(i))
        values_list.append(i)
        print("index : " + str(list.index(i)) + "  valeur : " + str(i))

    return index_list, values_list

return_index_and_values(inputted_list)
print()


# 1.3
