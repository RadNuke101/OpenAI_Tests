# Start time: 2024-03-30 00:55:46.311008
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if there is more than two words in the inputted phrase, return everything between the first and last word, and given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if there is more than two words in the inputted phrase, return everything between the first and last word
# Input: ['susan ann chang'] Output: ann
# Input: ['ayako tanaka'] Output: 
# Input: ['bobby t. smith'] Output: t.
# Input: ['anthory r. tom brown'] Output: r. tom

def extract_middle_word(input_phrase):
    try:
        # Check if input is a list with one element
        if len(input_phrase) != 1 or not isinstance(input_phrase[0], str):
            raise ValueError("Input should be a list with a single string element")
        
        words = input_phrase[0].split()
        
        # Check if there are more than two words in the input phrase
        if len(words) > 2:
            return ' '.join(words[1:-1])
        else:
            return ''
    except (ValueError, IndexError) as e:
        return f"Error: {e}"

# Test cases
print(extract_middle_word(['susan ann chang']))  # Output: ann
print(extract_middle_word(['ayako tanaka']))    # Output: 
print(extract_middle_word(['bobby t. smith']))   # Output: t.
print(extract_middle_word(['anthory r. tom brown']))  # Output: r. tom

# End time: 2024-03-30 00:55:52.592180
# Elapsed time in seconds: 6.281027238999741