# Start time: 2024-03-30 04:45:57.733449
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if there is more than two words in the inputted phrase, return everything between the first and last word, and given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if there is more than two words in the inputted phrase, return everything between the first and last word
# Input: ['susan ann chang'], Output: 'ann'
# Input: ['ayako tanaka'], Output: ''
# Input: ['bobby t. smith'], Output: 't.'
# Input: ['anthory r. tom brown'], Output: 'r. tom'

def extract_middle_word(input_phrase):
    try:
        # Extracting the first and last words from the input phrase
        words = input_phrase.split()
        first_word = words[0]
        last_word = words[-1]

        # Checking if there are more than two words in the input phrase
        if len(words) > 2:
            # Returning everything between the first and last word
            return input_phrase[input_phrase.index(first_word) + len(first_word):input_phrase.rindex(last_word)].strip()
        else:
            return ''
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test cases
print(extract_middle_word('susan ann chang'))  # Output: 'ann'
print(extract_middle_word('ayako tanaka'))     # Output: ''
print(extract_middle_word('bobby t. smith'))    # Output: 't.'
print(extract_middle_word('anthory r. tom brown'))  # Output: 'r. tom'

# End time: 2024-03-30 04:46:02.220053
# Elapsed time in seconds: 4.486604634999821