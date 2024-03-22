def first_word(input_list):
    output_list = []
    for sublist in input_list:
        phrase = sublist[0]
        if 'ssp' in phrase:
            words = phrase.split(' ')
            output_list.append(' '.join(words[:2]))
        else:
            output_list.append(phrase.split(' ')[0])
    return output_list

input_list = [['Polygonum amphibium'], ['Hippuris vulgaris'], ['Lysimachia vulgaris'], ['Juncus bulbosus ssp. bulbosus'], ['Lycopus europaeus ssp. europaeus'], ['Nymphaea alba']]
print(first_word(input_list))
