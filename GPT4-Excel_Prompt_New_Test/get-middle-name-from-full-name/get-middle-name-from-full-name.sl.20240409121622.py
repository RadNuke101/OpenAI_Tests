# Start time: 2024-04-09 14:13:45.661284

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of full names of individuals, which are strings containing first names, middle names or initials, and last names. These names are presented in a variety of formats, including:

1. Single middle names or initials (e.g., 'susan ann chang', 'bobby t. smith').
2. No middle name or initial (e.g., 'ayako tanaka').
3. Multiple middle names or initials (e.g., 'anthory r. tom brown').

The names are diverse, indicating no specific cultural, geographical, or linguistic focus. They include both single and compound middle names or initials, showcasing a range of naming conventions.

### Output Column Summary:

The output column extracts and presents the middle names or initials from the input names, according to the following observed patterns:

1. When a single middle name or initial is present, it is extracted as the output (e.g., 'ann' from 'susan ann chang', 't.' from 'bobby t. smith').
2. When no middle name or initial is present, the output is empty (e.g., '' from 'ayako tanaka').
3. When multiple middle names or initials are present, all are extracted as part of the output (e.g., 'r. tom' from 'anthory r. tom brown').

### Relationship Between Input and Output:

The relationship between the input and output columns is defined by the extraction of middle names or initials from the full names provided in the input. The output specifically focuses on the segment(s) of the input string that represent(s) the middle name(s) or initial(s), if any. This extraction process disregards the first and last names, focusing solely on the middle portion of the name string. The process is consistent across the dataset, with the output varying based on the presence, absence, or quantity of middle names or initials in the input names. This relationship highlights a systematic approach to identifying and extracting middle names or initials from a given set of full names., and input as ['susan ann chang'] output is ann, input as ['ayako tanaka'] output is , input as ['bobby t. smith'] output is t., input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    # Split the full name into parts
    name_parts = full_name.strip().split()
    
    # Check if the name has more than two parts (indicating the presence of a middle name or initial)
    if len(name_parts) > 2:
        # Extract and return the middle name(s) or initial(s), excluding the first and last parts
        return ' '.join(name_parts[1:-1])
    else:
        # Return an empty string if no middle name or initial is present
        return ''

# Test cases
print(generated_function('susan ann chang'))  # Expected output: ann
print(generated_function('ayako tanaka'))     # Expected output: 
print(generated_function('bobby t. smith'))   # Expected output: t.
print(generated_function('anthory r. tom brown'))  # Expected output: r. tom
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom

# End time: 2024-04-09 14:13:53.649364
# Elapsed time in seconds: 7.987841839999419


# APPEND TEST SCRIPTS...
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom


print(generated_function("olivia parker"))  ### Output: 
print(generated_function("emma von reynolds"))  ### Output: von
print(generated_function("caleb mitchell"))  ### Output: 
print(generated_function("grace f. harrison"))  ### Output: f.
print(generated_function("mason ann thompson"))  ### Output: ann
print(generated_function("wyatt thomas davis"))  ### Output: thomas
print(generated_function("jackson ann turner"))  ### Output: ann
print(generated_function("benjamin t. hayes"))  ### Output: t.
print(generated_function("lily anderson"))  ### Output: 

# TEST SCRIPTS APPENDED!

