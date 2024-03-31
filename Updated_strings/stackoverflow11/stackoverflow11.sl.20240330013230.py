# Start time: 2024-03-30 01:51:16.366542
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything after the "_" in input, and given input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, given input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, given input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return everything after the "_" in input
# Input: '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
# Output: HEEN PAX 77820

def extract_text_after_underscore(input_str):
    try:
        # Split the input string by "_"
        parts = input_str.split('_')
        
        # Check if there is text after "_"
        if len(parts) > 1:
            return parts[1].strip()
        else:
            return "No text found after '_'"
    except Exception as e:
        return str(e)

# Test cases
print(extract_text_after_underscore('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))  # Output: HEEN PAX 77820
print(extract_text_after_underscore('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))  # Output: PAX
print(extract_text_after_underscore('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))  # Output: BOX 4403 PAX SSKA

# End time: 2024-03-30 01:51:19.343443
# Elapsed time in seconds: 2.976811672000622