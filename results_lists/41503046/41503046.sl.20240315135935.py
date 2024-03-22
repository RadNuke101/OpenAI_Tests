def extract_first_word(data):
    result = []
    for item in data:
        phrase = item[0]
        if 'ssp' in phrase:
            result.append(' '.join(phrase.split()[:2]))
        else:
            result.append(phrase.split()[0])
    return result

input_data = [['Polygonum amphibium'], ['Hippuris vulgaris'], ['Lysimachia vulgaris'], ['Juncus bulbosus ssp. bulbosus'], ['Lycopus europaeus ssp. europaeus'], ['Nymphaea alba']]
output_data = ['Polygonum', 'Hippuris', 'Lysimachia', 'Juncus bulbosus', 'Lycopus europaeus', 'Nymphaea']

print(extract_first_word(input_data))
