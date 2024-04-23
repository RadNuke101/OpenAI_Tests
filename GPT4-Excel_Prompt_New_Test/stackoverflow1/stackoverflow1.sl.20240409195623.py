# Start time: 2024-04-09 20:12:51.331221

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary for Input Column Data:

The input data consists of company names that are primarily associated with the trucking industry. These names are presented in a formal structure, often including legal identifiers such as "Inc." or "LLC" at the end of the name. The names vary in length and complexity, ranging from simple, straightforward names to more complex ones that may include abbreviations or additional descriptive terms. The common theme across all entries is their association with trucking, indicating a focus on companies within the transportation sector. The presence of legal identifiers suggests these are established entities recognized as corporations or limited liability companies.

### Summary for Output Column Data:

The output data retains the core identity of each company by preserving the main name or descriptive part that indicates the business's focus or brand identity. It systematically removes legal identifiers such as "Inc.", "LLC", and any commas that precede these terms. This process simplifies the company names, making them more straightforward and focused on the essential elements that convey the company's primary business or brand name. The output names are cleaner and more concise, emphasizing the brand or business name without the formal legal structure identifiers.

### Relationship Summary Between Input and Output:

The transformation from input to output demonstrates a process of simplification and clarification of company names within the trucking industry. By removing legal identifiers and any additional punctuation that accompanies these identifiers, the output provides a streamlined version of each company name. This process highlights the essence of each company's identity, focusing on the brand or business name that is most relevant for casual reference or branding purposes. The relationship between the input and output data underscores an effort to make company names more accessible and easier to recognize without the formalities that are necessary for legal or official contexts but might be superfluous in everyday communication or branding. This transformation supports clearer communication and potentially enhances brand recognition by focusing on the most distinctive and memorable elements of the company names., and input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # Remove legal identifiers and any preceding commas
    for identifier in [" Inc.", " LLC", " Inc", " LLC,", ", Inc.", ", LLC"]:
        if identifier in company_name:
            company_name = company_name.replace(identifier, "")
    return company_name

# Test cases based on the provided examples
print(generated_function('Trucking Inc.'))  # Expected output: Trucking
print(generated_function('New Truck Inc'))  # Expected output: New Truck
print(generated_function('ABV Trucking Inc, LLC'))  # Expected output: ABV Trucking
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking

# End time: 2024-04-09 20:12:57.521085
# Elapsed time in seconds: 6.1897273780014075


# APPEND TEST SCRIPTS...
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking


print(generated_function("New House Inc"))  ### Output: New House
print(generated_function("Brand New House Inc"))  ### Output: Brand New House
print(generated_function("Housing Inc."))  ### Output: Housing
print(generated_function("ABV Housing Inc, LLC"))  ### Output: ABV Housing

# TEST SCRIPTS APPENDED!

