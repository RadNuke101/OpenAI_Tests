# Start time: 2024-03-30 20:11:08.356983

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, given input as ['MIT', 'Cambridge, MA'] output is MIT, Cambridge, MA, given input as ['Rice University', 'Houston, TX'] output is Rice University, Houston, TX, given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA, given input as ['NYU', 'New York, New York, USA'] output is NYU, New York, New York, USA, given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, given input as ['UIUC', 'Urbana, IL'] output is UIUC, Urbana, IL, given input as ['Temple University', 'Philadelphia, PA'] output is Temple University, Philadelphia, PA, given input as ['Harvard University', 'Cambridge, MA, USA'] output is Harvard University, Cambridge, MA, USA, given input as ['University of Connecticut', 'Storrs, CT, USA'] output is University of Connecticut, Storrs, CT, USA, given input as ['Drexel University', 'Philadelphia, PA'] output is Drexel University, Philadelphia, PA, given input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven University, New Haven, CT, USA, given input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is University of California, Santa Barbara, Santa Barbara, CA, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases
# input: 'University of Pennsylvania', 'Phialdelphia, PA, USA'
# output: 'University of Pennsylvania, Phialdelphia, PA, USA'

# input: 'UCLA', 'Los Angeles, CA'
# output: 'UCLA, Los Angeles, CA'

# input: 'Cornell University', 'Ithaca, New York, USA'
# output: 'Cornell University, Ithaca, New York, USA'

# input: 'Penn', 'Philadelphia, PA, USA'
# output: 'Penn, Philadelphia, PA, USA'

# input: 'University of Maryland College Park', 'College Park, MD'
# output: 'University of Maryland College Park, College Park, MD'

# input: 'University of Michigan', 'Ann Arbor, MI, USA'
# output: 'University of Michigan, Ann Arbor, MI, USA'

# input: 'UC Berkeley', 'Berkeley, CA'
# output: 'UC Berkeley, Berkeley, CA'

# input: 'MIT', 'Cambridge, MA'
# output: 'MIT, Cambridge, MA'

# input: 'Rice University', 'Houston, TX'
# output: 'Rice University, Houston, TX'

# input: 'Yale University', 'New Haven, CT, USA'
# output: 'Yale University, New Haven, CT, USA'

# input: 'Columbia University', 'New York, NY, USA'
# output: 'Columbia University, New York, NY, USA'

# input: 'NYU', 'New York, New York, USA'
# output: 'NYU, New York, New York, USA'

# input: 'UC Berkeley', 'Berkeley, CA'
# output: 'UC Berkeley, Berkeley, CA'

# input: 'UIUC', 'Urbana, IL'
# output: 'UIUC, Urbana, IL'

# input: 'Temple University', 'Philadelphia, PA'
# output: 'Temple University, Philadelphia, PA'

# input: 'Harvard University', 'Cambridge, MA, USA'
# output: 'Harvard University, Cambridge, MA, USA'

# input: 'University of Connecticut', 'Storrs, CT, USA'
# output: 'University of Connecticut, Storrs, CT, USA'

# input: 'Drexel University', 'Philadelphia, PA'
# output: 'Drexel University, Philadelphia, PA'

# input: 'New Haven University', 'New Haven, CT, USA'
# output: 'New Haven University, New Haven, CT, USA'

# input: 'University of California, Santa Barbara', 'Santa Barbara, CA, USA'
# output: 'University of California, Santa Barbara, Santa Barbara, CA, USA'

def format_location(university, location):
    try:
        return university + ', ' + location
    except Exception as e:
        return str(e)

# End time: 2024-03-30 20:11:18.912553
# Elapsed time in seconds: 10.555456209000113