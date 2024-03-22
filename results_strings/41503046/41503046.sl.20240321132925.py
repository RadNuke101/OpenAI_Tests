def first_word(input_phrase):
    phrase = input_phrase.split()
    if 'ssp' in input_phrase:
        return ' '.join(phrase[:2])
    else:
        return phrase[0]

# Prompt: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase
# Input: ['Polygonum amphibium']
# Output: Polygonum
print(first_word('Polygonum amphibium'))

# Input: ['Hippuris vulgaris']
# Output: Hippuris
print(first_word('Hippuris vulgaris'))

# Input: ['Lysimachia vulgaris']
# Output: Lysimachia
print(first_word('Lysimachia vulgaris'))

# Input: ['Juncus bulbosus ssp. bulbosus']
# Output: Juncus bulbosus
print(first_word('Juncus bulbosus ssp. bulbosus'))

# Input: ['Lycopus europaeus ssp. europaeus']
# Output: Lycopus europaeus
print(first_word('Lycopus europaeus ssp. europaeus'))

# Input: ['Nymphaea alba']
# Output: Nymphaea
print(first_word('Nymphaea alba'))
