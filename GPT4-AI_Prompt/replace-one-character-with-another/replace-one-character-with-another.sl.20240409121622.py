# Start time: 2024-04-09 13:18:32.351393

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of strings representing phone numbers in a specific format. Each string is a sequence of digits grouped into three segments: the first segment contains three digits, the second segment also contains three digits, and the third segment contains four digits. These segments are separated by spaces. The format of the input data can be summarized as follows:

- Format: `XXX YYY ZZZZ`
- Example: `801 456 8756`

The input data represents phone numbers in a non-standard format, where the standard format typically involves the use of hyphens (-) or parentheses around the area code instead of spaces.

### Output Column Summary:

The output data transforms the input phone numbers into a more conventional format. The transformation involves replacing the spaces between the segments with hyphens (-). This results in a standardized phone number format that is commonly used and recognized. The format of the output data can be summarized as follows:

- Format: `XXX-YYY-ZZZZ`
- Example: `801-456-8756`

The output data represents the phone numbers in a format that is easier to read and is widely accepted in various contexts, such as forms, documents, and digital interfaces.

### Relationship Summary:

The transformation from the input to the output involves a simple yet crucial formatting change. The relationship between the input and output data can be summarized by the following points:

1. **Consistency in Segmentation**: Both the input and output maintain the segmentation of the phone numbers into three parts. The first part (area code) contains three digits, the second part (local exchange) also contains three digits, and the third part (subscriber number) contains four digits.

2. **Change in Delimiters**: The primary transformation involves changing the delimiters between the segments. In the input, the segments are separated by spaces, while in the output, the segments are separated by hyphens (-).

3. **Preservation of Digits**: The digits themselves remain unchanged during the transformation. The order and value of the digits in each segment are preserved, ensuring that the integrity of the phone number is maintained.

4. **Standardization**: The transformation process standardizes the phone number format, making it more aligned with common usage and expectations. This standardization facilitates easier recognition, memorization, and usage of the phone numbers.

In summary, the relationship between the input and output data is characterized by a simple formatting change that significantly enhances the usability and readability of the phone numbers, transitioning them from a less conventional format to a widely accepted standard format., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms a phone number from the format 'XXX YYY ZZZZ' to 'XXX-YYY-ZZZZ'.
    
    Parameters:
    phone_number (str): The phone number in the format 'XXX YYY ZZZZ'.
    
    Returns:
    str: The phone number in the format 'XXX-YYY-ZZZZ'.
    """
    # Replace spaces with hyphens to transform the format
    return phone_number.replace(" ", "-")

# Test cases
# Transforming '801 456 8756' to '801-456-8756'
print(generated_function('801 456 8756'))

# Transforming '978 456 8756' to '978-456-8756'
print(generated_function('978 456 8756'))
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-09 13:18:41.845851
# Elapsed time in seconds: 9.491474626000127