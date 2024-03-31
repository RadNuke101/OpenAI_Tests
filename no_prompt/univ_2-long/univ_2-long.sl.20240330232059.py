# Start time: 2024-03-30 23:30:09.609015

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, USA, given input as ['MIT', 'Cambridge, MA'] output is MIT, Cambridge, MA, USA, given input as ['Rice University', 'Houston, TX'] output is Rice University, Houston, TX, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA, given input as ['NYU', 'New York, New York, USA'] output is NYU, New York, New York, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, USA, given input as ['UIUC', 'Urbana, IL'] output is UIUC, Urbana, IL, USA, given input as ['Temple University', 'Philadelphia, PA'] output is Temple University, Philadelphia, PA, USA, given input as ['Harvard University', 'Cambridge, MA, USA'] output is Harvard University, Cambridge, MA, USA, given input as ['University of Connecticut', 'Storrs, CT, USA'] output is University of Connecticut, Storrs, CT, USA, given input as ['Drexel University', 'Philadelphia, PA'] output is Drexel University, Philadelphia, PA, USA, given input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven University, New Haven, CT, USA, given input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is University of California, Santa Barbara, Santa Barbara, CA, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_university_info(input_str):
    try:
        input_list = input_str.split(', ')
        university = input_list[0]
        location = input_list[1]
        if len(input_list) == 3:
            country = input_list[2]
            return f"{university}, {location}, {country}"
        else:
            return f"{university}, {location}, USA"
    except IndexError:
        return "Invalid input format"

# Test cases
print(format_university_info('University of Pennsylvania, Phialdelphia, PA, USA'))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_university_info('UCLA, Los Angeles, CA'))  # UCLA, Los Angeles, CA, USA
print(format_university_info('Cornell University, Ithaca, New York, USA'))  # Cornell University, Ithaca, New York, USA
print(format_university_info('Penn, Philadelphia, PA, USA'))  # Penn, Philadelphia, PA, USA
print(format_university_info('University of Maryland College Park, College Park, MD'))  # University of Maryland College Park, College Park, MD, USA
print(format_university_info('University of Michigan, Ann Arbor, MI, USA'))  # University of Michigan, Ann Arbor, MI, USA
print(format_university_info('UC Berkeley, Berkeley, CA'))  # UC Berkeley, Berkeley, CA, USA
print(format_university_info('MIT, Cambridge, MA'))  # MIT, Cambridge, MA, USA
print(format_university_info('Rice University, Houston, TX'))  # Rice University, Houston, TX, USA
print(format_university_info('Yale University, New Haven, CT, USA'))  # Yale University, New Haven, CT, USA
print(format_university_info('Columbia University, New York, NY, USA'))  # Columbia University, New York, NY, USA
print(format_university_info('NYU, New York, New York, USA'))  # NYU, New York, New York, USA
print(format_university_info('UC Berkeley, Berkeley, CA'))  # UC Berkeley, Berkeley, CA, USA
print(format_university_info('UIUC, Urbana, IL'))  # UIUC, Urbana, IL, USA
print(format_university_info('Temple University, Philadelphia, PA'))  # Temple University, Philadelphia, PA, USA
print(format_university_info('Harvard University, Cambridge, MA, USA'))  # Harvard University, Cambridge, MA, USA
print(format_university_info('University of Connecticut, Storrs, CT, USA'))  # University of Connecticut, Storrs, CT, USA
print(format_university_info('Drexel University, Philadelphia, PA'))  # Drexel University, Philadelphia, PA, USA
print(format_university_info('New Haven University, New Haven, CT, USA'))  # New Haven University, New Haven, CT, USA
print(format_university_info('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # University of California, Santa Barbara, Santa Barbara, CA, USA

# End time: 2024-03-30 23:30:15.356989
# Elapsed time in seconds: 5.74780269799885