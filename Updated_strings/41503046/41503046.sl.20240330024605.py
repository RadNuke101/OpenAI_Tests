# Start time: 2024-03-30 02:48:33.893941
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase, and given input as ['Polygonum amphibium'] output is Polygonum, given input as ['Hippuris vulgaris'] output is Hippuris, given input as ['Lysimachia vulgaris'] output is Lysimachia, given input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, given input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, given input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase
# Input: 'Polygonum amphibium', Output: 'Polygonum'
# Input: 'Hippuris vulgaris', Output: 'Hippuris'
# Input: 'Lysimachia vulgaris', Output: 'Lysimachia'
# Input: 'Juncus bulbosus ssp. bulbosus', Output: 'Juncus bulbosus'
# Input: 'Lycopus europaeus ssp. europaeus', Output: 'Lycopus europaeus'
# Input: 'Nymphaea alba', Output: 'Nymphaea'

def get_first_words(phrase):
    try:
        if 'ssp' in phrase:
            return ' '.join(phrase.split()[:2])
        else:
            return phrase.split()[0]
    except:
        return "Invalid input"

# Test cases
print(get_first_words('Polygonum amphibium'))  # Output: Polygonum
print(get_first_words('Hippuris vulgaris'))  # Output: Hippuris
print(get_first_words('Lysimachia vulgaris'))  # Output: Lysimachia
print(get_first_words('Juncus bulbosus ssp. bulbosus'))  # Output: Juncus bulbosus
print(get_first_words('Lycopus europaeus ssp. europaeus'))  # Output: Lycopus europaeus
print(get_first_words('Nymphaea alba'))  # Output: Nymphaea

# End time: 2024-03-30 02:48:39.834440
# Elapsed time in seconds: 5.9403703509997285