def first_word(input_phrase):
    phrase = input_phrase.split()
    if 'ssp' in input_phrase:
        return ' '.join(phrase[:2])
    else:
        return phrase[0]

# Input: 'Polygonum amphibium', Output: 'Polygonum'
# Input: 'Hippuris vulgaris', Output: 'Hippuris'
# Input: 'Lysimachia vulgaris', Output: 'Lysimachia'
# Input: 'Juncus bulbosus ssp. bulbosus', Output: 'Juncus bulbosus'
# Input: 'Lycopus europaeus ssp. europaeus', Output: 'Lycopus europaeus'
# Input: 'Nymphaea alba', Output: 'Nymphaea'
