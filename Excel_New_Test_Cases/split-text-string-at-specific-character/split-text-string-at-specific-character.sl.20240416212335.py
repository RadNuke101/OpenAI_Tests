# Start time: 2024-04-16 21:29:39.136639

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and input as: "011016_assignment.xlsx", "1" output is: 011016, input as: "011016_assignment.xlsx", "2" output is: assignment.xlsx, input as: "030116_cost.xlsx", "1" output is: 030116, input as: "030116_cost.xlsx", "2" output is: cost.xlsx, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(input_str, n):
    # Find the nth occurrence of the period
    period_indices = [i for i, char in enumerate(input_str) if char == '.']
    nth_period_index = period_indices[n-1]
    
    # Find the prior occurrence of the period
    prior_period_index = period_indices[n-2]
    
    # Extract the substring between the nth and prior occurrences of the period
    output = input_str[prior_period_index+1:nth_period_index]
    
    return output



print(generated_function("011028_todosheet.xlsx", "1"))  ### Output: "011028_todosheet.xlsx", "1"
print(generated_function("030128_a.xlsx", "2"))  ### Output: "030128_a.xlsx", "2"
print(generated_function("030128_a.xlsx", "1"))  ### Output: "030128_a.xlsx", "1"
print(generated_function("011028_todosheet.xlsx", "2"))  ### Output: "011028_todosheet.xlsx", "2"


print(generated_function("011016_assignment.xlsx", "1"))  ## Output: 011016
print(generated_function("011016_assignment.xlsx", "2"))  ## Output: assignment.xlsx
print(generated_function("030116_cost.xlsx", "1"))  ## Output: 030116
print(generated_function("030116_cost.xlsx", "2"))  ## Output: cost.xlsx



# End time: 2024-04-16 21:29:40.770136
# Elapsed time in seconds: 1.63346296200001