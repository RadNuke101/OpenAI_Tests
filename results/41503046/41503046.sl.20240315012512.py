def first_word(input_list):
    output_list = []
    for sublist in input_list:
        if 'ssp' in sublist[0]:
            output_list.append(' '.join(sublist[0].split()[:2]))
        else:
            output_list.append(sublist[0].split()[0])
    return output_list

input_list = [['Polygonum amphibium'], ['Hippuris vulgaris'], ['Lysimachia vulgaris'], ['Juncus bulbosus ssp. bulbosus'], ['Lycopus europaeus ssp. europaeus'], ['Nymphaea alba']]
output = first_word(input_list)
print(output)
