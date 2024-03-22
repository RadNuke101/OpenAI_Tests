def first_word(input_phrase):
    words = input_phrase.split()
    if 'ssp' in input_phrase:
        return ' '.join(words[:2])
    else:
        return words[0]

# Prompt: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase
# Input: ['Polygonum amphibium'] Output: Polygonum
# Input: ['Hippuris vulgaris'] Output: Hippuris
# Input: ['Lysimachia vulgaris'] Output: Lysimachia
# Input: ['Juncus bulbosus ssp. bulbosus'] Output: Juncus bulbosus
# Input: ['Lycopus europaeus ssp. europaeus'] Output: Lycopus europaeus
# Input: ['Nymphaea alba'] Output: Nymphaea

# Test cases
print(first_word('Polygonum amphibium'))  # Output: Polygonum
print(first_word('Hippuris vulgaris'))  # Output: Hippuris
print(first_word('Lysimachia vulgaris'))  # Output: Lysimachia
print(first_word('Juncus bulbosus ssp. bulbosus'))  # Output: Juncus bulbosus
print(first_word('Lycopus europaeus ssp. europaeus'))  # Output: Lycopus europaeus
print(first_word('Nymphaea alba'))  # Output: Nymphaea
