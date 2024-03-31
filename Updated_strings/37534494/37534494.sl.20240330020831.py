# Start time: 2024-03-30 02:13:47.324380
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column), and given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column)
# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas
# Input: ['I love apples', 'I hate bananas', 'apple']
# Output: I love apples

def find_matching_phrase(phrase1, phrase2, word):
    try:
        if word in phrase1:
            return phrase1
        elif word in phrase2:
            return phrase2
        else:
            return "No matching phrase found"
    except Exception as e:
        return str(e)

# Test cases
input1 = ['I love apples', 'I hate bananas', 'banana']
output1 = find_matching_phrase(input1[0], input1[1], input1[2])
print(output1)

input2 = ['I love apples', 'I hate bananas', 'apple']
output2 = find_matching_phrase(input2[0], input2[1], input2[2])
print(output2)

# End time: 2024-03-30 02:13:51.797671
# Elapsed time in seconds: 4.473191922999831