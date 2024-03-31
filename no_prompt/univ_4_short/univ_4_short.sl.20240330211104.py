# Start time: 2024-03-30 21:24:26.967477

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, NY, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, given input as ['Columbia University', 'New York, NY, USA'] output is New York, NY, USA, given input as ['NYU', 'New York, New York, USA'] output is New York, NY, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_location(input_str):
    try:
        input_list = input_str.split(', ')
        city_state = input_list[-2]
        country = input_list[-1]
        
        if len(city_state.split(', ')) > 1:
            city, state = city_state.split(', ')
            if len(state.split()) > 1:
                state = ' '.join([word[0].upper() + word[1:].lower() for word in state.split()])
            else:
                state = state.upper()
            return f"{city}, {state}, {country}"
        else:
            return f"{city_state}, {country}"
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
print(get_location('University of Pennsylvania, Phialdelphia, PA, USA'))  # Phialdelphia, PA, USA
print(get_location('UCLA, Los Angeles, CA'))  # Los Angeles, CA, USA
print(get_location('Cornell University, Ithaca, New York, USA'))  # Ithaca, NY, USA
print(get_location('Penn, Philadelphia, PA, USA'))  # Philadelphia, PA, USA
print(get_location('University of Maryland College Park, College Park, MD'))  # College Park, MD, USA
print(get_location('University of Michigan, Ann Arbor, MI, USA'))  # Ann Arbor, MI, USA
print(get_location('Columbia University, New York, NY, USA'))  # New York, NY, USA
print(get_location('NYU, New York, New York, USA'))  # New York, NY, USA

# End time: 2024-03-30 21:24:30.325336
# Elapsed time in seconds: 3.3577612819990463