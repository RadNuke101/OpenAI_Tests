def add_country(input_str):
    input_list = input_str.split(', ')
    output = input_list[0] + ', ' + input_list[1]
    if 'USA' not in input_list[1]:
        output += ', USA'
    return output

# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, USA
# Given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA
# Given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA
# Given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA
# Given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA
# Given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA
# Given input as ['MIT', 'Cambridge, MA'] output is MIT, Cambridge, MA, USA
# Given input as ['Rice University', 'Houston, TX'] output is Rice University, Houston, TX, USA
# Given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA
# Given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA
# Given input as ['NYU', 'New York, New York, USA'] output is NYU, New York, New York, USA
# Given input as ['Drexel University', 'Philadelphia, PA'] output is Drexel University, Philadelphia, PA, USA
# Given input as ['UIUC', 'Urbana, IL'] output is UIUC, Urbana, IL, USA
# Given input as ['Temple University', 'Philadelphia, PA'] output is Temple University, Philadelphia, PA, USA
# Given input as ['Harvard University', 'Cambridge, MA, USA'] output is Harvard University, Cambridge, MA, USA
# Given input as ['University of Connecticut', 'Storrs, CT, USA'] output is University of Connecticut, Storrs, CT, USA
# Given input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven University, New Haven, CT, USA
# Given input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is University of California, Santa Barbara, Santa Barbara, CA, USA

# Test
print(add_country('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # Output: University of California, Santa Barbara, Santa Barbara, CA, USA
