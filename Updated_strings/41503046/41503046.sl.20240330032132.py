# Start time: 2024-03-30 03:24:46.950232
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase, and given input as ['Polygonum amphibium'] output is Polygonum, given input as ['Hippuris vulgaris'] output is Hippuris, given input as ['Lysimachia vulgaris'] output is Lysimachia, given input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, given input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, given input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase

def first_word(input_phrase):
    try:
        phrase = input_phrase.split()[0]
        if "ssp" in input_phrase:
            phrase = ' '.join(input_phrase.split()[:2])
        return phrase
    except:
        return "Invalid input"

# Test cases
print(first_word('Polygonum amphibium'))  # Output: Polygonum
print(first_word('Hippuris vulgaris'))  # Output: Hippuris
print(first_word('Lysimachia vulgaris'))  # Output: Lysimachia
print(first_word('Juncus bulbosus ssp. bulbosus'))  # Output: Juncus bulbosus
print(first_word('Lycopus europaeus ssp. europaeus'))  # Output: Lycopus europaeus
print(first_word('Nymphaea alba'))  # Output: Nymphaea

# End time: 2024-03-30 03:24:49.637805
# Elapsed time in seconds: 2.68835751000006