# Start time: 2024-03-30 00:43:41.704479
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase, and given input as ['Polygonum amphibium'] output is Polygonum, given input as ['Hippuris vulgaris'] output is Hippuris, given input as ['Lysimachia vulgaris'] output is Lysimachia, given input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, given input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, given input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase

def extract_words(input_phrase):
    try:
        words = input_phrase.split()
        if 'ssp' in input_phrase:
            return ' '.join(words[:2])
        else:
            return words[0]
    except:
        return "Invalid input"

# Test cases
print(extract_words('Polygonum amphibium'))  # Output: Polygonum
print(extract_words('Hippuris vulgaris'))  # Output: Hippuris
print(extract_words('Lysimachia vulgaris'))  # Output: Lysimachia
print(extract_words('Juncus bulbosus ssp. bulbosus'))  # Output: Juncus bulbosus
print(extract_words('Lycopus europaeus ssp. europaeus'))  # Output: Lycopus europaeus
print(extract_words('Nymphaea alba'))  # Output: Nymphaea

# End time: 2024-03-30 00:43:44.805130
# Elapsed time in seconds: 3.1005855170005816