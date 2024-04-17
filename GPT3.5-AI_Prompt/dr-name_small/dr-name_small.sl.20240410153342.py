# Start time: 2024-04-10 15:48:47.229226

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Data Summaries:
1. The input column data consists of names of individuals, with titles included (e.g., Nancy FreeHafer, Andrew Cencici, Jan Kotas, Mariya Sergienko).
   
Output Column Summary:
1. The output column consists of titles (Dr.) followed by the first names of the individuals (e.g., Dr. Nancy, Dr. Andrew, Dr. Jan, Dr. Mariya).

Relationship Summary:
The relationship between the input and output columns is that the titles from the input column are transformed into a standardized format in the output column, where "Dr." is added before the first name of each individual. This transformation suggests that the individuals in the input column hold a doctorate degree, as indicated by the title "Dr." in the output column. The output column provides a more formal and professional representation of the individuals' names by incorporating the title "Dr." before their first names., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into title and first name
    title, first_name = input_str.split()[1], input_str.split()[0]
    # Format the output with "Dr." before the first name
    output_str = f"Dr. {first_name}"
    return output_str

# Test cases
print(generated_function('Nancy FreeHafer'))  # Dr. Nancy
print(generated_function('Andrew Cencici'))  # Dr. Andrew
print(generated_function('Jan Kotas'))  # Dr. Jan
print(generated_function('Mariya Sergienko'))  # Dr. Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-10 15:48:50.046821
# Elapsed time in seconds: 2.817546294000749