# Start time: 2024-03-30 18:34:26.204778

# Content: Given that given input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, NY, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, given input as ['MIT', 'Cambridge, MA'] output is Cambridge, MA, USA, given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, given input as ['MIT', 'Cambridge, MA'] output is Cambridge, MA, USA, given input as ['Rice University', 'Houston, TX'] output is Houston, TX, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is New York, NY, USA, given input as ['NYU', 'New York, New York, USA'] output is New York, NY, USA, given input as ['Drexel University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, given input as ['UIUC', 'Urbana, IL'] output is Urbana, IL, USA, given input as ['Temple University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, given input as ['Harvard University', 'Cambridge, MA, USA'] output is Cambridge, MA, USA, given input as ['University of Connecticut', 'Storrs, CT, USA'] output is Storrs, CT, USA, given input as ['Drexel University', 'Philadelphia, PA'] output is DPhiladelphia, PA, USA, given input as ['NYU', 'New York, New York, USA'] output is New York, NY, USA, given input as ['UIUC', 'Urbana, IL'] output is Urbana, IL, USA, given input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven, CT, USA, given input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is Santa Barbara, CA, USA, given input as ['University of Connecticut', 'Storrs, CT, USA'] output is Storrs, CT, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_location(input_str):
    try:
        # Input: 'UC Berkeley, Berkeley, CA'
        # Output: 'Berkeley, CA, USA'
        parts = input_str.split(', ')
        city = parts[-1]
        state = parts[-2]
        if len(parts) == 3:
            return f'{city}, {state}, USA'
        else:
            return f'{parts[0]}, {city}, {state}, USA'
    except Exception as e:
        return f'Error: {e}'

# Test cases
print(format_location('UC Berkeley, Berkeley, CA'))
print(format_location('University of Pennsylvania, Phialdelphia, PA, USA'))
print(format_location('UCLA, Los Angeles, CA'))
print(format_location('Cornell University, Ithaca, New York, USA'))
print(format_location('Penn, Philadelphia, PA, USA'))
print(format_location('University of Michigan, Ann Arbor, MI, USA'))
print(format_location('UC Berkeley, Berkeley, CA'))
print(format_location('MIT, Cambridge, MA'))
print(format_location('University of Pennsylvania, Phialdelphia, PA, USA'))
print(format_location('UCLA, Los Angeles, CA'))
print(format_location('University of Maryland College Park, College Park, MD'))
print(format_location('University of Michigan, Ann Arbor, MI, USA'))
print(format_location('UC Berkeley, Berkeley, CA'))
print(format_location('MIT, Cambridge, MA'))
print(format_location('Rice University, Houston, TX'))
print(format_location('Yale University, New Haven, CT, USA'))
print(format_location('Columbia University, New York, NY, USA'))
print(format_location('NYU, New York, New York, USA'))
print(format_location('Drexel University, Philadelphia, PA'))
print(format_location('UC Berkeley, Berkeley, CA'))
print(format_location('UIUC, Urbana, IL'))
print(format_location('Temple University, Philadelphia, PA'))
print(format_location('Harvard University, Cambridge, MA, USA'))
print(format_location('University of Connecticut, Storrs, CT, USA'))
print(format_location('Drexel University, Philadelphia, PA'))
print(format_location('NYU, New York, New York, USA'))
print(format_location('UIUC, Urbana, IL'))
print(format_location('New Haven University, New Haven, CT, USA'))
print(format_location('University of California, Santa Barbara, Santa Barbara, CA, USA'))
print(format_location('University of Connecticut, Storrs, CT, USA'))

# End time: 2024-03-30 18:34:32.641285
# Elapsed time in seconds: 6.436324171000024