# Start time: 2024-03-30 02:43:51.377287
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if there is more than two words in the inputted phrase, return everything between the first and last word, and given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if there is more than two words in the inputted phrase, return everything between the first and last word
# Input: ['susan ann chang'] Output: ann
# Input: ['ayako tanaka'] Output: 
# Input: ['bobby t. smith'] Output: t.
# Input: ['anthory r. tom brown'] Output: r. tom

def extract_middle(input_phrase):
    try:
        # Extracting the input phrase from the list
        input_phrase = input_phrase[0]
        
        # Splitting the input phrase into words
        words = input_phrase.split()
        
        # Checking if there are more than two words in the input phrase
        if len(words) > 2:
            # Returning everything between the first and last word
            return ' '.join(words[1:-1])
        else:
            return ''
    except Exception as e:
        return str(e)

# Test cases
print(extract_middle(['susan ann chang']))  # Output: ann
print(extract_middle(['ayako tanaka']))     # Output: 
print(extract_middle(['bobby t. smith']))   # Output: t.
print(extract_middle(['anthory r. tom brown']))  # Output: r. tom

# End time: 2024-03-30 02:43:55.362950
# Elapsed time in seconds: 3.985566368999571