# Start time: 2024-03-30 01:00:02.384114
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase, and given input as ['Polygonum amphibium'] output is Polygonum, given input as ['Hippuris vulgaris'] output is Hippuris, given input as ['Lysimachia vulgaris'] output is Lysimachia, given input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, given input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, given input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def first_word(input_phrase):
    try:
        phrase = input_phrase[0] if isinstance(input_phrase, list) else input_phrase
        words = phrase.split()
        
        if 'ssp' in phrase:
            return ' '.join(words[:2])
        else:
            return words[0]
    except (IndexError, AttributeError):
        return "Invalid input"

# Input: ['Polygonum amphibium']
# Output: Polygonum
# Prompt: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase
print(first_word(['Polygonum amphibium']))

# Input: ['Hippuris vulgaris']
# Output: Hippuris
print(first_word(['Hippuris vulgaris']))

# Input: ['Lysimachia vulgaris']
# Output: Lysimachia
print(first_word(['Lysimachia vulgaris']))

# Input: ['Juncus bulbosus ssp. bulbosus']
# Output: Juncus bulbosus
print(first_word(['Juncus bulbosus ssp. bulbosus']))

# Input: ['Lycopus europaeus ssp. europaeus']
# Output: Lycopus europaeus
print(first_word(['Lycopus europaeus ssp. europaeus']))

# Input: ['Nymphaea alba']
# Output: Nymphaea
print(first_word(['Nymphaea alba']))

# End time: 2024-03-30 01:00:11.604156
# Elapsed time in seconds: 9.21979123500023