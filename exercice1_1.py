# exercice terminé
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

    index_count = 0

    for i in list :

        # enumerate or import numpy : numpy.where()
        # au final j'ai utilisé un variable représentant l'index mais qui n'est pas réellement l'index
        index_list.append(index_count)
        values_list.append(i)

        print("index : " + str(index_count) + "  valeur : " + str(i))

        index_count += 1

    return index_list, values_list

return_index_and_values(inputted_list)
print()


# 1.3
def return_sum_of_list_elements(list) :
    sum = 0

    for i in list :
        sum += int(i)

    return sum

print("Somme de tous les éléments de la liste : " + str(return_sum_of_list_elements(inputted_list)))
print()


# 1.4
def return_multiple_of_three_list(list) :
    multiple_list = []

    for i in list :
        multiple = int(i) * 3

        multiple_list.append(multiple)

    return multiple_list

print("Liste des multiples de 3 des éléments de la liste : " + str(return_multiple_of_three_list(inputted_list)))
print()


# 1.5
def return_greatest_number(list) :
    greatest_number = int(list[0])

    for i in list :

        if int(i) > greatest_number :
            greatest_number = int(i)

    return greatest_number

print("Le plus grand nombre de la liste est : " + str(return_greatest_number(inputted_list)))
print()


# 1.6
def return_smallest_number(list) :
    smallest_number = int(list[0])

    for i in list :

        if int(i) < smallest_number :
            smallest_number = int(i)

    return smallest_number

print("Le plus petit nombre de la liste est : " + str(return_smallest_number(inputted_list)))
print()


# 1.7
def return_number_of_even_elements(list) :
    number_of_even_elements = 0

    for i in list :

        if int(i) % 2 == 0 :
            number_of_even_elements += 1

    return number_of_even_elements

print("Nombre d'éléments pairs de la liste : " + str(return_number_of_even_elements(inputted_list)))
print()


# 1.8
def return_sum_of_odd_elements(list) :
    sum = 0

    for i in list :

        if int(i) % 2 != 0 :
            sum += int(i)

    return sum

print("Somme des éléments impairs de la liste : " + str(return_sum_of_odd_elements(inputted_list)))
print()
