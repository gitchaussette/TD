print()

# 2.1
def ask_int_input_return_list() :
    int_list = []
    count_list = []
    is_input_over = False
    output = 0

    while not is_input_over :
        int_input = input('Entrez un nombre ("stop" pour arrêter): ')

        if int_input == "stop" :
            is_input_over = True
        else :
            try :
                int_list.append(int(int_input))
                print(int_list)
            except :
                pass

    # 2.2, 2.3
    for i in int_list :
        count = int_list.count(i)

        if count > 1 and not i in count_list :
            count_list.append(i)

            output += count
        
    print("Le nombre d'éléments dupliqués dans la liste est de : " + str(output))
    print("La nouvelle liste, sans les éléments dupliqués : " + str(count_list))

    return output


# ça marche pas mais je laisse pour qu'on puisse se moquer
# def ask_int_input_return_list() :
#     int_list = [0]

#     for i in int_list :
#         if list[0] == 0 :
#             print(list[0])
#             del int_list[0]
#         try :
#             current_int = int(input("Entrez un nombre : "))
#         except ValueError :
#             print("Entrez un N-O-M-B-R-E ! >:(")
#         int_list.append(current_int)
#         print(int_list)

ask_int_input_return_list()
print()