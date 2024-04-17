# Start time: 2024-04-16 21:31:04.375980

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the words "Inc", "Company", "Corporation", or "Enterprises", and input as: "General Electric" output is: General Electric, input as: "General Electric Inc" output is: General Electric, input as: "General Electric Company" output is: General Electric, input as: "Microsoft" output is: Microsoft, input as: "Microsoft Corporation" output is: Microsoft, input as: "Nintendo" output is: Nintendo, input as: "Nintendo Enterprises" output is: Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(*args):
    # Remove the words "Inc", "Company", "Corporation", or "Enterprises" from the input
    outputs = []
    for arg in args:
        output = arg.replace(" Inc", "").replace(" Company", "").replace(" Corporation", "").replace(" Enterprises", "")
        outputs.append(output)
    
    return outputs



print(generated_function("Nintendo Company"))  ### Output: "Nintendo Company"
print(generated_function("General Electric Corporation"))  ### Output: "General Electric Corporation"
print(generated_function("Microsoft Corporation"))  ### Output: "Microsoft Corporation"
print(generated_function("Microsoft Inc"))  ### Output: "Microsoft Inc"
print(generated_function("Microsoft Enterprises"))  ### Output: "Microsoft Enterprises"
print(generated_function("Microsoft"))  ### Output: "Microsoft"
print(generated_function("Walmart Inc"))  ### Output: "Walmart Inc"
print(generated_function("General Electric Enterprises"))  ### Output: "General Electric Enterprises"
print(generated_function("Microsoft Company"))  ### Output: "Microsoft Company"
print(generated_function("Walmart"))  ### Output: "Walmart"
print(generated_function("Walmart Corporation"))  ### Output: "Walmart Corporation"
print(generated_function("Walmart Enterprises"))  ### Output: "Walmart Enterprises"
print(generated_function("Nintendo Corporation"))  ### Output: "Nintendo Corporation"
print(generated_function("Walmart Company"))  ### Output: "Walmart Company"


print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo



# End time: 2024-04-16 21:31:05.729645
# Elapsed time in seconds: 1.3536368439999933