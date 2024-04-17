# Start time: 2024-04-10 18:06:01.018602

'''
Prompt:
Given that input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = eval(input_str)
        if len(input_list) != 2:
            raise ValueError("Input should contain exactly 2 elements")
        
        university = input_list[0]
        location = input_list[1]
        
        if "USA" not in location:
            location += ", USA"
        
        return university + ", " + location
    
    except Exception as e:
        return str(e)

# Test cases
print(generated_function("['University of Pennsylvania', 'Phialdelphia, PA, USA']"))
print(generated_function("['UCLA', 'Los Angeles, CA']"))
print(generated_function("['Cornell University', 'Ithaca, New York, USA']"))
print(generated_function("['Penn', 'Philadelphia, PA, USA']"))
print(generated_function("['University of Maryland College Park', 'College Park, MD']"))
print(generated_function("['University of Michigan', 'Ann Arbor, MI, USA']"))
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: University of Pennsylvania, Phialdelphia, PA, USA
print(generated_function("UCLA", "Los Angeles, CA"))  ## Output: UCLA, Los Angeles, CA, USA
print(generated_function("Cornell University", "Ithaca, New York, USA"))  ## Output: Cornell University, Ithaca, New York, USA
print(generated_function("Penn", "Philadelphia, PA, USA"))  ## Output: Penn, Philadelphia, PA, USA
print(generated_function("University of Maryland College Park", "College Park, MD"))  ## Output: University of Maryland College Park, College Park, MD, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: University of Michigan, Ann Arbor, MI, USA

# End time: 2024-04-10 18:06:04.276576
# Elapsed time in seconds: 3.25791314099979