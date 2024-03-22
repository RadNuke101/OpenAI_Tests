def return_second_input(input_str):
    input_list = input_str.split(', ')
    if 'USA' not in input_list[1]:
        return input_list[1] + ', USA'
    return input_list[1]

# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA

# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA

# Input: ['Cornell University', 'Ithaca, New York, USA']
# Output: Ithaca, NY, USA

# Input: ['Penn', 'Philadelphia, PA, USA']
# Output: Philadelphia, PA, USA

# Input: ['University of Maryland College Park', 'College Park, MD']
# Output: College Park, MD, USA

# Input: ['University of Michigan', 'Ann Arbor, MI, USA']
# Output: Ann Arbor, MI, USA

# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

# Input: ['MIT', 'Cambridge, MA']
# Output: Cambridge, MA, USA

# Input: ['Rice University', 'Houston, TX']
# Output: Houston, TX, USA

# Input: ['Yale University', 'New Haven, CT, USA']
# Output: New Haven, CT, USA

# Input: ['Columbia University', 'New York, NY, USA']
# Output: New York, NY, USA

# Input: ['NYU', 'New York, New York, USA']
# Output: New York, NY, USA

# Input: ['UC Berkeley', 'Berkeley, CA']
# Output: Berkeley, CA, USA

# Input: ['UIUC', 'Urbana, IL']
# Output: Urbana, IL, USA

# Input: ['Temple University', 'Philadelphia, PA']
# Output: Philadelphia, PA, USA

# Input: ['Harvard University', 'Cambridge, MA, USA']
# Output: Cambridge, MA, USA

# Input: ['University of Connecticut', 'Storrs, CT, USA']
# Output: Storrs, CT, USA

# Input: ['Drexel University', 'Philadelphia, PA']
# Output: Philadelphia, PA, USA

# Input: ['New Haven University', 'New Haven, CT, USA']
# Output: New Haven, CT, USA

# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

# Input: 'UC Berkeley, Berkeley, CA'
# Output: Berkeley, CA, USA

# Input: 'MIT, Cambridge, MA'
# Output: Cambridge, MA, USA

# Input: 'Rice University, Houston, TX'
# Output: Houston, TX, USA

# Input: 'Yale University, New Haven, CT, USA'
# Output: New Haven, CT, USA

# Input: 'Columbia University, New York, NY, USA'
# Output: New York, NY, USA

# Input: 'NYU, New York, New York, USA'
# Output: New York, NY, USA

# Input: 'UC Berkeley, Berkeley, CA'
# Output: Berkeley, CA, USA

# Input: 'UIUC, Urbana, IL'
# Output: Urbana, IL, USA

# Input: 'Temple University, Philadelphia, PA'
# Output: Philadelphia, PA, USA

# Input: 'Harvard University, Cambridge, MA, USA'
# Output: Cambridge, MA, USA

# Input: 'University of Connecticut, Storrs, CT, USA'
# Output: Storrs, CT, USA

# Input: 'Drexel University, Philadelphia, PA'
# Output: Philadelphia, PA, USA

# Input: 'New Haven University, New Haven, CT, USA'
# Output: New Haven, CT, USA

# Input: 'University of California, Santa Barbara, Santa Barbara, CA'
# Output: Santa Barbara, CA, USA
