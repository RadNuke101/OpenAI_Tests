# Start time: 2024-03-30 22:42:00.686245

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, USA, given input as ['MIT', 'Cambridge, MA'] output is MIT, Cambridge, MA, USA, given input as ['Rice University', 'Houston, TX'] output is Rice University, Houston, TX, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA, given input as ['NYU', 'New York, New York, USA'] output is NYU, New York, New York, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, USA, given input as ['UIUC', 'Urbana, IL'] output is UIUC, Urbana, IL, USA, given input as ['Temple University', 'Philadelphia, PA'] output is Temple University, Philadelphia, PA, USA, given input as ['Harvard University', 'Cambridge, MA, USA'] output is Harvard University, Cambridge, MA, USA, given input as ['University of Connecticut', 'Storrs, CT, USA'] output is University of Connecticut, Storrs, CT, USA, given input as ['Drexel University', 'Philadelphia, PA'] output is Drexel University, Philadelphia, PA, USA, given input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven University, New Haven, CT, USA, given input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is University of California, Santa Barbara, Santa Barbara, CA, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_university_details(input_str):
    # Input: "['University of Pennsylvania', 'Phialdelphia, PA, USA']"
    # Output: "University of Pennsylvania, Phialdelphia, PA, USA"
    
    try:
        input_list = input_str.strip("[]").replace("'", "").split(", ")
        university_name = input_list[0]
        location = input_list[1]
        
        if "USA" not in location:
            location += ", USA"
        
        return university_name + ", " + location
    except Exception as e:
        return "Invalid input format"

# Test cases
print(format_university_details("['University of Pennsylvania', 'Phialdelphia, PA, USA']"))
print(format_university_details("['UCLA', 'Los Angeles, CA']"))
print(format_university_details("['Cornell University', 'Ithaca, New York, USA']"))
print(format_university_details("['Penn', 'Philadelphia, PA, USA']"))
print(format_university_details("['University of Maryland College Park', 'College Park, MD']"))
print(format_university_details("['University of Michigan', 'Ann Arbor, MI, USA']"))
print(format_university_details("['UC Berkeley', 'Berkeley, CA']"))
print(format_university_details("['MIT', 'Cambridge, MA']"))
print(format_university_details("['Rice University', 'Houston, TX']"))
print(format_university_details("['Yale University', 'New Haven, CT, USA']"))
print(format_university_details("['Columbia University', 'New York, NY, USA']"))
print(format_university_details("['NYU', 'New York, New York, USA']"))
print(format_university_details("['UC Berkeley', 'Berkeley, CA']"))
print(format_university_details("['UIUC', 'Urbana, IL']"))
print(format_university_details("['Temple University', 'Philadelphia, PA']"))
print(format_university_details("['Harvard University', 'Cambridge, MA, USA']"))
print(format_university_details("['University of Connecticut', 'Storrs, CT, USA']"))
print(format_university_details("['Drexel University', 'Philadelphia, PA']"))
print(format_university_details("['New Haven University', 'New Haven, CT, USA']"))
print(format_university_details("['University of California, Santa Barbara', 'Santa Barbara, CA, USA']"))

# End time: 2024-03-30 22:42:04.979053
# Elapsed time in seconds: 4.292697867000243