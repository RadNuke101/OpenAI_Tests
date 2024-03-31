# Start time: 2024-03-30 01:42:51.470717
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return phrase containing three capitalized letters in the beginning, and given input as ['Tire Pressure ABC123873 Monitor'] output is ABC123873, given input as [' Oil Life ABC849999999021 gauge'] output is ABC849999999021, given input as [' Air conditioner GHF211 maintenance'] output is GHF211, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return phrase containing three capitalized letters in the beginning
# Input: 'Tire Pressure ABC123873 Monitor'
# Output: 'ABC123873'

# Input: ' Oil Life ABC849999999021 gauge'
# Output: 'ABC849999999021'

# Input: ' Air conditioner GHF211 maintenance'
# Output: 'GHF211'

def extract_capitalized(input_str):
    try:
        words = input_str.split()
        for word in words:
            if word.isupper() and len(word) >= 3:
                return word
    except Exception as e:
        print("Error: ", e)
    
    return None

# Test cases
print(extract_capitalized('Tire Pressure ABC123873 Monitor'))  # Output: ABC123873
print(extract_capitalized(' Oil Life ABC849999999021 gauge'))  # Output: ABC849999999021
print(extract_capitalized(' Air conditioner GHF211 maintenance'))  # Output: GHF211

# End time: 2024-03-30 01:42:54.270837
# Elapsed time in seconds: 2.8000631659997453