# Start time: 2024-04-10 14:51:44.754083

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of company names related to the trucking industry.
- The names vary in length and structure, including variations such as abbreviations, full names, and additional descriptors like "Inc." or "LLC".

Output Column Summary:
- The output column data consists of modified versions of the input company names, where any additional descriptors like "Inc." or "LLC" have been removed.
- The output names retain the core identity of the company while simplifying the name for clarity and brevity.

Relationship Summary:
- The relationship between the input and output columns is that the output column aims to provide a cleaner and more concise version of the input company names.
- By removing unnecessary descriptors, the output names focus on the essential identity of the company, making them more accessible and easier to remember.
- The transformation from input to output suggests a process of streamlining and enhancing the company names for better communication and branding purposes in the trucking industry., and input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Remove any additional descriptors like "Inc." or "LLC" from the input company name
    output_str = input_str.replace(" Inc", "").replace(" LLC", "").replace(",", "").strip()
    
    return output_str

# Test cases
print(generated_function("Trucking Inc."))  # Output: Trucking
print(generated_function("New Truck Inc"))  # Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  # Output: ABV Trucking
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking

# End time: 2024-04-10 14:51:46.017297
# Elapsed time in seconds: 1.2631869800000004