# exercice en cours
communications=[{"number":"0634567832", "duree":"45","prix":""}, {"number":"0134767842", "duree":"2460","prix":""}, {"number":"0467921526", "duree":"125","prix":""},
{"number":"0276859473", "duree":"1","prix":""}, {"number":"0579864893", "duree":"335","prix":""}, {"number":"0854098743", "duree":"8876","prix":""}, {"number":"0875660433", "duree":"2245","prix":""}
,{"number":"0387594758", "duree":"5","prix":""}, {"number":"0745938212", "duree":"185","prix":""}]

prefix=[["01", "0.2"],["02", "0.1"],["03", "0.5"],["04", "0.3"],["06", "0.6"],["07", "0.6"],["0134", "0.6"],["0275", "0.6"],["0854098743", "0.18"],["0875660433", "0.30"]]

def return_com_price() :
    
    # j'aime vraiment beaucoup les listes de compréhension
    com_list = [c.get("number") for c in communications]
    call_len_list = [c.get("duree") for c in communications]
    prefix_number_list = [p[0] for p in prefix]
    prefix_value_list = [p[1] for p in prefix]

    output_number = []

    for number in com_list :

        for prefix_number in prefix_number_list :

            if prefix_number in number and number not in output_number :
                print(prefix_number)
                print(number)
                output_number.append(number)

                print(output_number)

                # for value in prefix_value_list :
                #     print(value)

                # print(prefix_number)


    # ancienne fonction de la liste de compréhension com_list
    # def return_communications_number_list() :
        # com_list = []
        # for c in communications :
        #     com = c.get("number")
        #     com_list.append(com)
    # return com_list

    # ancienne fonction de la liste de compréhension call_len_list
    # def return_communications_call_len_list() :
    #     call_len_list = []
    #     for c in communications :
    #         call_len = c.get("duree")
    #         call_len_list.append(call_len)
    #     return call_len_list

    # print(com_list)
    # print(call_len_list)
    # print(prefix_number_list)
    # print(prefix_value_list)

return_com_price()