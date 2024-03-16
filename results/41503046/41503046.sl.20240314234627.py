def first_word(input_list):
    output = []
    for sublist in input_list:
        phrase = sublist[0]
        if 'ssp' in phrase:
            output.append(' '.join(phrase.split()[:2]))
        else:
            output.append(phrase.split()[0])
    return output

input_list = [['Polygonum amphibium'], ['Hippuris vulgaris'], ['Lysimachia vulgaris'], ['Juncus bulbosus ssp. bulbosus'], ['Lycopus europaeus ssp. europaeus'], ['Nymphaea alba']]
output = first_word(input_list)
print(output)
