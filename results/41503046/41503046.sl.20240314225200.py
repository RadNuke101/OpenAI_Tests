def first_word(input_list):
    output_list = []
    for sublist in input_list:
        phrase = sublist[0]
        if 'ssp' in phrase:
            output_list.append(' '.join(phrase.split()[:2]))
        else:
            output_list.append(phrase.split()[0])
    return output_list

input_list = [['Polygonum amphibium'], ['Hippuris vulgaris'], ['Lysimachia vulgaris'], ['Juncus bulbosus ssp. bulbosus'], ['Lycopus europaeus ssp. europaeus'], ['Nymphaea alba']]
output = first_word(input_list)
print(output)
