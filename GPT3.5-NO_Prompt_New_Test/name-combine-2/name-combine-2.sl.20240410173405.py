# Start time: 2024-04-10 17:43:33.795848

'''
Prompt:
Given that input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        first_name = input_list[0].strip()
        last_name = input_list[1].strip()
        return f"{first_name} {last_name[0]}."
    except IndexError:
        return "Invalid input format. Please provide first name and last name separated by a comma."
    except Exception as e:
        return f"An error occurred: {e}"

# Test cases
print(generated_function('Nancy, FreeHafer'))
print(generated_function('Andrew, Cencici'))
print(generated_function('Jan, Kotas'))
print(generated_function('Mariya, Sergienko'))
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.

# End time: 2024-04-10 17:43:35.726336
# Elapsed time in seconds: 1.9304659199999605


# APPEND TEST SCRIPTS...
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.


print(generated_function("Jackson", "Turner"))  ### Output: Jackson T.
print(generated_function("Caleb", "Mitchell"))  ### Output: Caleb M.
print(generated_function("Olivia", "Parker"))  ### Output: Olivia P.
print(generated_function("Logan", "Smith"))  ### Output: Logan S.
print(generated_function("Sophia", "Coleman"))  ### Output: Sophia C.
print(generated_function("Amelia", "Nelson"))  ### Output: Amelia N.
print(generated_function("Isabella", "Brooks"))  ### Output: Isabella B.
print(generated_function("Zoey", "Turner"))  ### Output: Zoey T.
print(generated_function("Carter", "Edwards"))  ### Output: Carter E.
print(generated_function("Madison", "Foster"))  ### Output: Madison F.
print(generated_function("Owen", "Morgan"))  ### Output: Owen M.
print(generated_function("Elijah", "Foster"))  ### Output: Elijah F.
print(generated_function("Lily", "Anderson"))  ### Output: Lily A.
print(generated_function("Wyatt", "Davis"))  ### Output: Wyatt D.
print(generated_function("Harper", "Taylor"))  ### Output: Harper T.
print(generated_function("Ava", "Bennett"))  ### Output: Ava B.
print(generated_function("Nolan", "Cooper"))  ### Output: Nolan C.
print(generated_function("Chloe", "Adams"))  ### Output: Chloe A.
print(generated_function("Gabriel", "Hayes"))  ### Output: Gabriel H.
print(generated_function("Hannah", "Martin"))  ### Output: Hannah M.
print(generated_function("Abigail", "Cooper"))  ### Output: Abigail C.
print(generated_function("Mason", "Thompson"))  ### Output: Mason T.
print(generated_function("Caleb", "Johnson"))  ### Output: Caleb J.
print(generated_function("Samuel", "Wright"))  ### Output: Samuel W.
print(generated_function("Emma", "Reynolds"))  ### Output: Emma R.
print(generated_function("Liam", "Carter"))  ### Output: Liam C.
print(generated_function("Scarlett", "Walker"))  ### Output: Scarlett W.
print(generated_function("Aiden", "Clark"))  ### Output: Aiden C.
print(generated_function("Grace", "Harrison"))  ### Output: Grace H.
print(generated_function("Benjamin", "Hayes"))  ### Output: Benjamin H.

# TEST SCRIPTS APPENDED!

