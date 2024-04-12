# Start time: 2024-04-09 17:33:00.283879

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a primary text string followed by three keywords. The primary text string describes a scene or an object, often incorporating colors and elements from the natural or artificial world. The three keywords that follow are 'yellow', 'green', and 'dog'. These keywords seem to serve as criteria for evaluating the primary text string. The primary text strings vary in their content, ranging from descriptions of animals in their environment, clothing items, celestial bodies within landscapes, to urban signage. The variety suggests a broad scope of application for the criteria represented by the keywords.

### Output Column Summary:

The output data is binary, represented by true or false values. These values indicate whether the primary text string meets a certain condition or set of conditions based on the three keywords that follow it. The true value suggests that the primary text string contains or is related to the criteria set by the keywords, while the false value indicates the absence or irrelevance of the criteria within the primary text.

### Relationship Summary:

The relationship between the input and output columns appears to be governed by the presence and relevance of the keywords within the primary text string. When the primary text string contains elements or themes directly related to all the keywords ('yellow', 'green', and 'dog'), the output is true. This indicates that the criteria for a true output require the primary text to encompass aspects or mentions of all three keywords in some form. In cases where the primary text does not explicitly or implicitly relate to all the keywords, the output is false. This suggests that the evaluation process is stringent, requiring all keywords to be represented or implied in the primary text for a positive affirmation. The relationship underscores a logical connection where the output serves as an indicator of the primary text string's compliance with the set criteria defined by the keywords., and input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(primary_text, keyword1, keyword2, keyword3):
    """
    Evaluates if the primary text string contains or is related to the criteria set by the three keywords.
    
    Parameters:
    - primary_text (str): The primary text string describing a scene or an object.
    - keyword1 (str): The first keyword to evaluate against the primary text.
    - keyword2 (str): The second keyword to evaluate against the primary text.
    - keyword3 (str): The third keyword to evaluate against the primary text.
    
    Returns:
    - bool: True if the primary text contains or is related to all three keywords, False otherwise.
    """
    # Convert the primary text to lowercase to ensure case-insensitive matching
    primary_text_lower = primary_text.lower()
    
    # Check if all keywords are present or related to the primary text
    if all(keyword.lower() in primary_text_lower for keyword in [keyword1, keyword2, keyword3]):
        return True
    else:
        return False

# Test cases
print(generated_function('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Expected output: True
print(generated_function('warm gray sweater', 'yellow', 'green', 'dog'))  # Expected output: False
print(generated_function('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Expected output: True
print(generated_function('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Expected output: True
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "dog"))  ## Output: false
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: true
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: true

# End time: 2024-04-09 17:33:11.849367
# Elapsed time in seconds: 11.565146706001542