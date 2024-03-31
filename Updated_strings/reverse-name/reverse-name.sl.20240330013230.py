# Start time: 2024-03-30 01:51:12.802365
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return second input, followed by a space, and then the first input, and given input as ['Launa', 'Withers'] output is Withers Launa, given input as ['Lakenya', 'Edison'] output is Edison Lakenya, given input as ['Brendan', 'Hage'] output is Hage Brendan, given input as ['Bradford', 'Lango'] output is Lango Bradford, given input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, given input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers'] Output: Withers Launa
# Input: ['Lakenya', 'Edison'] Output: Edison Lakenya
# Input: ['Brendan', 'Hage'] Output: Hage Brendan
# Input: ['Bradford', 'Lango'] Output: Lango Bradford
# Input: ['Rudolf', 'Akiyama'] Output: Akiyama Rudolf
# Input: ['Lara', 'Constable'] Output: Constable Lara

def reverse_names(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly two elements")
        
        return input_list[1] + ' ' + input_list[0]
    
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)

# Test cases
print(reverse_names(['Launa', 'Withers']))  # Output: Withers Launa
print(reverse_names(['Lakenya', 'Edison']))  # Output: Edison Lakenya
print(reverse_names(['Brendan', 'Hage']))  # Output: Hage Brendan
print(reverse_names(['Bradford', 'Lango']))  # Output: Lango Bradford
print(reverse_names(['Rudolf', 'Akiyama']))  # Output: Akiyama Rudolf
print(reverse_names(['Lara', 'Constable']))  # Output: Constable Lara
print(reverse_names(['John']))  # Output: Input list must contain exactly two elements
print(reverse_names(['Alice', 'Bob', 'Charlie']))  # Output: Input list must contain exactly two elements

# End time: 2024-03-30 01:51:16.268352
# Elapsed time in seconds: 3.4659318110007007