# Start time: 2024-03-30 21:30:22.479004

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, NY, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, given input as ['MIT', 'Cambridge, MA'] output is Cambridge, MA, USA, given input as ['Rice University', 'Houston, TX'] output is Houston, TX, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is New York, NY, USA, given input as ['NYU', 'New York, New York, USA'] output is New York, NY, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, given input as ['UIUC', 'Urbana, IL'] output is Urbana, IL, USA, given input as ['Temple University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, given input as ['Harvard University', 'Cambridge, MA, USA'] output is Cambridge, MA, USA, given input as ['University of Connecticut', 'Storrs, CT, USA'] output is Storrs, CT, USA, given input as ['Drexel University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, given input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven, CT, USA, given input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is Santa Barbara, CA, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_location(input_str):
    try:
        input_list = input_str.split(', ')
        city_state = input_list[-2]
        country = input_list[-1]
        if len(city_state.split(', ')) > 1:
            city, state = city_state.split(', ')
            if len(state.split()) > 1:
                state = ' '.join([word[0].upper() + word[1:].lower() for word in state.split()])
            location = f"{city}, {state}, {country}"
        else:
            location = f"{city_state}, {country}"
        return location
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
# Input: 'University of Pennsylvania, Phialdelphia, PA, USA'
# Output: 'Phialdelphia, PA, USA'
print(get_location('University of Pennsylvania, Phialdelphia, PA, USA'))

# Input: 'UCLA, Los Angeles, CA'
# Output: 'Los Angeles, CA, USA'
print(get_location('UCLA, Los Angeles, CA'))

# Input: 'Cornell University, Ithaca, New York, USA'
# Output: 'Ithaca, NY, USA'
print(get_location('Cornell University, Ithaca, New York, USA'))

# Input: 'Penn, Philadelphia, PA, USA'
# Output: 'Philadelphia, PA, USA'
print(get_location('Penn, Philadelphia, PA, USA'))

# Input: 'University of Maryland College Park, College Park, MD'
# Output: 'College Park, MD, USA'
print(get_location('University of Maryland College Park, College Park, MD'))

# Input: 'University of Michigan, Ann Arbor, MI, USA'
# Output: 'Ann Arbor, MI, USA'
print(get_location('University of Michigan, Ann Arbor, MI, USA'))

# Input: 'UC Berkeley, Berkeley, CA'
# Output: 'Berkeley, CA, USA'
print(get_location('UC Berkeley, Berkeley, CA'))

# Input: 'MIT, Cambridge, MA'
# Output: 'Cambridge, MA, USA'
print(get_location('MIT, Cambridge, MA'))

# Input: 'Rice University, Houston, TX'
# Output: 'Houston, TX, USA'
print(get_location('Rice University, Houston, TX'))

# Input: 'Yale University, New Haven, CT, USA'
# Output: 'New Haven, CT, USA'
print(get_location('Yale University, New Haven, CT, USA'))

# Input: 'Columbia University, New York, NY, USA'
# Output: 'New York, NY, USA'
print(get_location('Columbia University, New York, NY, USA'))

# Input: 'NYU, New York, New York, USA'
# Output: 'New York, NY, USA'
print(get_location('NYU, New York, New York, USA'))

# Input: 'UC Berkeley, Berkeley, CA'
# Output: 'Berkeley, CA, USA'
print(get_location('UC Berkeley, Berkeley, CA'))

# Input: 'UIUC, Urbana, IL'
# Output: 'Urbana, IL, USA'
print(get_location('UIUC, Urbana, IL'))

# Input: 'Temple University, Philadelphia, PA'
# Output: 'Philadelphia, PA, USA'
print(get_location('Temple University, Philadelphia, PA'))

# Input: 'Harvard University, Cambridge, MA, USA'
# Output: 'Cambridge, MA, USA'
print(get_location('Harvard University, Cambridge, MA, USA'))

# Input: 'University of Connecticut, Storrs, CT, USA'
# Output: 'Storrs, CT, USA'
print(get_location('University of Connecticut, Storrs, CT, USA'))

# Input: 'Drexel University, Philadelphia, PA'
# Output: 'Philadelphia, PA, USA'
print(get_location('Drexel University, Philadelphia, PA'))

# Input: 'New Haven University, New Haven, CT, USA'
# Output: 'New Haven, CT, USA'
print(get_location('New Haven University, New Haven, CT, USA'))

# Input: 'University of California, Santa Barbara, Santa Barbara, CA, USA'
# Output: 'Santa Barbara, CA, USA'
print(get_location('University of California, Santa Barbara, Santa Barbara, CA, USA'))

# End time: 2024-03-30 21:30:36.923882
# Elapsed time in seconds: 14.4444459059996