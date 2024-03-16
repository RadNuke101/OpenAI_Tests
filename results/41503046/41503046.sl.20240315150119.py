def extract_first_word(input_list):
    result = []
    for sublist in input_list:
        phrase = sublist[0]
        if 'ssp' in phrase:
            result.append(' '.join(phrase.split()[:2]))
        else:
            result.append(phrase.split()[0])
    return result

input_list = [['Polygonum amphibium'], ['Hippuris vulgaris'], ['Lysimachia vulgaris'], ['Juncus bulbosus ssp. bulbosus'], ['Lycopus europaeus ssp. europaeus'], ['Nymphaea alba']]
output = extract_first_word(input_list)
print(output)
