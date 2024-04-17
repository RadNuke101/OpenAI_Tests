# Start time: 2024-04-16 21:03:43.310328

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first phrase in the inputted epxression that begins with "_", and input as: ['this is a _username in the middle'] output is: _username, input as: ['twitter names look like= _name'] output is: _name, input as: ['with two _name1 and _name2'] output is: _name1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(*args):
    def find_phrase_with_underscore(input_str):
        phrases = input_str.split()
        for phrase in phrases:
            if phrase.startswith('_'):
                return phrase
        return ""
    
    results = []
    for arg in args:
        result = find_phrase_with_underscore(arg)
        results.append(result)
    
    return results

# Test cases
generated_function('this is a _username in the middle', 'twitter names look like= _name', 'with two _name1 and _name2')



print(generated_function("this is a _username in the top"))  ### Output: "this is a _username in the top"
print(generated_function("with two _account1 and _account2"))  ### Output: "with two _account1 and _account2"
print(generated_function("this is a _user in the middle"))  ### Output: "this is a _user in the middle"
print(generated_function("x names look like= _name"))  ### Output: "x names look like= _name"
print(generated_function("there are _names in the middle"))  ### Output: "there are _names in the middle"
print(generated_function("there is a _username in the middle"))  ### Output: "there is a _username in the middle"


print(generated_function("this is a _username in the middle"))  ## Output: _username
print(generated_function("twitter names look like= _name"))  ## Output: _name
print(generated_function("with two _name1 and _name2"))  ## Output: _name1



# End time: 2024-04-16 21:03:45.135575
# Elapsed time in seconds: 1.825213170999973