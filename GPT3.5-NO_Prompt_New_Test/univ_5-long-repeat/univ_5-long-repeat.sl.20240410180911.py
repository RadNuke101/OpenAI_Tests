# Start time: 2024-04-10 18:14:53.848741

'''
Prompt:
Given that input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, NY, USA, input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, input as ['MIT', 'Cambridge, MA'] output is Cambridge, MA, USA, input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, input as ['MIT', 'Cambridge, MA'] output is Cambridge, MA, USA, input as ['Rice University', 'Houston, TX'] output is Houston, TX, USA, input as ['Yale University', 'New Haven, CT, USA'] output is New Haven, CT, USA, input as ['Columbia University', 'New York, NY, USA'] output is New York, NY, USA, input as ['NYU', 'New York, New York, USA'] output is New York, NY, USA, input as ['Drexel University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, input as ['UC Berkeley', 'Berkeley, CA'] output is Berkeley, CA, USA, input as ['UIUC', 'Urbana, IL'] output is Urbana, IL, USA, input as ['Temple University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, input as ['Harvard University', 'Cambridge, MA, USA'] output is Cambridge, MA, USA, input as ['University of Connecticut', 'Storrs, CT, USA'] output is Storrs, CT, USA, input as ['Drexel University', 'Philadelphia, PA'] output is Philadelphia, PA, USA, input as ['NYU', 'New York, New York, USA'] output is New York, NY, USA, input as ['UIUC', 'Urbana, IL'] output is Urbana, IL, USA, input as ['New Haven University', 'New Haven, CT, USA'] output is New Haven, CT, USA, input as ['University of California, Santa Barbara', 'Santa Barbara, CA, USA'] output is Santa Barbara, CA, USA, input as ['University of Connecticut', 'Storrs, CT, USA'] output is Storrs, CT, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.strip('[]').split(', ')
        city_state = input_list[1].split(', ')
        city = city_state[0]
        state = city_state[1]
        country = 'USA'
        return f'{city}, {state}, {country}'
    except:
        return "Invalid input format"

# Test cases
print(generated_function("['UC Berkeley', 'Berkeley, CA']"))  # Berkeley, CA, USA
print(generated_function("['University of Pennsylvania', 'Phialdelphia, PA, USA']"))  # Phialdelphia, PA, USA
print(generated_function("['Cornell University', 'Ithaca, New York, USA']"))  # Ithaca, NY, USA
print(generated_function("['Penn', 'Philadelphia, PA, USA']"))  # Philadelphia, PA, USA
print(generated_function("['University of Michigan', 'Ann Arbor, MI, USA']"))  # Ann Arbor, MI, USA
print(generated_function("['UC Berkeley', 'Berkeley, CA']"))  # Berkeley, CA, USA
print(generated_function("['MIT', 'Cambridge, MA']"))  # Cambridge, MA, USA
print(generated_function("['University of Pennsylvania', 'Phialdelphia, PA, USA']"))  # Phialdelphia, PA, USA
print(generated_function("['UCLA', 'Los Angeles, CA']"))  # Los Angeles, CA, USA
print(generated_function("['University of Maryland College Park', 'College Park, MD']"))  # College Park, MD, USA
print(generated_function("['University of Michigan', 'Ann Arbor, MI, USA']"))  # Ann Arbor, MI, USA
print(generated_function("['UC Berkeley', 'Berkeley, CA']"))  # Berkeley, CA, USA
print(generated_function("['MIT', 'Cambridge, MA']"))  # Cambridge, MA, USA
print(generated_function("['Rice University', 'Houston, TX']"))  # Houston, TX, USA
print(generated_function("['Yale University', 'New Haven, CT, USA']"))  # New Haven, CT, USA
print(generated_function("['Columbia University', 'New York, NY, USA']"))  # New York, NY, USA
print(generated_function("['NYU', 'New York, New York, USA']"))  # New York, NY, USA
print(generated_function("['Drexel University', 'Philadelphia, PA']"))  # Philadelphia, PA, USA
print(generated_function("['UC Berkeley', 'Berkeley, CA']"))  # Berkeley, CA, USA
print(generated_function("['UIUC', 'Urbana, IL']"))  # Urbana, IL, USA
print(generated_function("['Temple University', 'Philadelphia, PA']"))  # Philadelphia, PA, USA
print(generated_function("['Harvard University', 'Cambridge, MA, USA']"))  # Cambridge, MA, USA
print(generated_function("['University of Connecticut', 'Storrs, CT, USA']"))  # Storrs, CT, USA
print(generated_function("['Drexel University', 'Philadelphia, PA']"))  # Philadelphia, PA, USA
print(generated_function("['NYU', 'New York, New York, USA']"))  # New York, NY, USA
print(generated_function("['UIUC', 'Urbana, IL']"))  # Urbana, IL, USA
print(generated_function("['New Haven University', 'New Haven, CT, USA']"))  # New Haven, CT, USA
print(generated_function("['University of California, Santa Barbara', 'Santa Barbara, CA, USA']"))  # Santa Barbara, CA, USA
print(generated_function("['University of Connecticut', 'Storrs, CT, USA']"))  # Storrs, CT, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: Phialdelphia, PA, USA
print(generated_function("Cornell University", "Ithaca, New York, USA"))  ## Output: Ithaca, NY, USA
print(generated_function("Penn", "Philadelphia, PA, USA"))  ## Output: Philadelphia, PA, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: Ann Arbor, MI, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("MIT", "Cambridge, MA"))  ## Output: Cambridge, MA, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: Phialdelphia, PA, USA
print(generated_function("UCLA", "Los Angeles, CA"))  ## Output: Los Angeles, CA, USA
print(generated_function("University of Maryland College Park", "College Park, MD"))  ## Output: College Park, MD, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: Ann Arbor, MI, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("MIT", "Cambridge, MA"))  ## Output: Cambridge, MA, USA
print(generated_function("Rice University", "Houston, TX"))  ## Output: Houston, TX, USA
print(generated_function("Yale University", "New Haven, CT, USA"))  ## Output: New Haven, CT, USA
print(generated_function("Columbia University", "New York, NY, USA"))  ## Output: New York, NY, USA
print(generated_function("NYU", "New York, New York, USA"))  ## Output: New York, NY, USA
print(generated_function("Drexel University", "Philadelphia, PA"))  ## Output: Philadelphia, PA, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("UIUC", "Urbana, IL"))  ## Output: Urbana, IL, USA
print(generated_function("Temple University", "Philadelphia, PA"))  ## Output: Philadelphia, PA, USA
print(generated_function("Harvard University", "Cambridge, MA, USA"))  ## Output: Cambridge, MA, USA
print(generated_function("University of Connecticut", "Storrs, CT, USA"))  ## Output: Storrs, CT, USA
print(generated_function("Drexel University", "Philadelphia, PA"))  ## Output: Philadelphia, PA, USA
print(generated_function("NYU", "New York, New York, USA"))  ## Output: New York, NY, USA
print(generated_function("UIUC", "Urbana, IL"))  ## Output: Urbana, IL, USA
print(generated_function("New Haven University", "New Haven, CT, USA"))  ## Output: New Haven, CT, USA
print(generated_function("University of California, Santa Barbara", "Santa Barbara, CA, USA"))  ## Output: Santa Barbara, CA, USA
print(generated_function("University of Connecticut", "Storrs, CT, USA"))  ## Output: Storrs, CT, USA

# End time: 2024-04-10 18:15:09.770313
# Elapsed time in seconds: 15.92127605099995


# APPEND TEST SCRIPTS...
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: Phialdelphia, PA, USA
print(generated_function("Cornell University", "Ithaca, New York, USA"))  ## Output: Ithaca, NY, USA
print(generated_function("Penn", "Philadelphia, PA, USA"))  ## Output: Philadelphia, PA, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: Ann Arbor, MI, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("MIT", "Cambridge, MA"))  ## Output: Cambridge, MA, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: Phialdelphia, PA, USA
print(generated_function("UCLA", "Los Angeles, CA"))  ## Output: Los Angeles, CA, USA
print(generated_function("University of Maryland College Park", "College Park, MD"))  ## Output: College Park, MD, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: Ann Arbor, MI, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("MIT", "Cambridge, MA"))  ## Output: Cambridge, MA, USA
print(generated_function("Rice University", "Houston, TX"))  ## Output: Houston, TX, USA
print(generated_function("Yale University", "New Haven, CT, USA"))  ## Output: New Haven, CT, USA
print(generated_function("Columbia University", "New York, NY, USA"))  ## Output: New York, NY, USA
print(generated_function("NYU", "New York, New York, USA"))  ## Output: New York, NY, USA
print(generated_function("Drexel University", "Philadelphia, PA"))  ## Output: Philadelphia, PA, USA
print(generated_function("UC Berkeley", "Berkeley, CA"))  ## Output: Berkeley, CA, USA
print(generated_function("UIUC", "Urbana, IL"))  ## Output: Urbana, IL, USA
print(generated_function("Temple University", "Philadelphia, PA"))  ## Output: Philadelphia, PA, USA
print(generated_function("Harvard University", "Cambridge, MA, USA"))  ## Output: Cambridge, MA, USA
print(generated_function("University of Connecticut", "Storrs, CT, USA"))  ## Output: Storrs, CT, USA
print(generated_function("Drexel University", "Philadelphia, PA"))  ## Output: Philadelphia, PA, USA
print(generated_function("NYU", "New York, New York, USA"))  ## Output: New York, NY, USA
print(generated_function("UIUC", "Urbana, IL"))  ## Output: Urbana, IL, USA
print(generated_function("New Haven University", "New Haven, CT, USA"))  ## Output: New Haven, CT, USA
print(generated_function("University of California, Santa Barbara", "Santa Barbara, CA, USA"))  ## Output: Santa Barbara, CA, USA
print(generated_function("University of Connecticut", "Storrs, CT, USA"))  ## Output: Storrs, CT, USA


print(generated_function("Johns Hopkins University", "Baltimore, MD"))  ### Output: Baltimore, MD, USA
print(generated_function("Virginia Tech", "Blacksburg, VA, USA"))  ### Output: Blacksburg, VA, USA
print(generated_function("University of Oregon", "Eugene, OR, USA"))  ### Output: Eugene, OR, USA
print(generated_function("University of Iowa", "Iowa City, IA, USA"))  ### Output: Iowa City, IA, USA
print(generated_function("University of Minnesota Twin Cities", "Minneapolis, MN, USA"))  ### Output: Minneapolis, MN, USA
print(generated_function("Rutgers, The State University of New Jersey", "New Brunswick, NJ, USA"))  ### Output: New Brunswick, NJ, USA
print(generated_function("University of Miami", "Coral Gables, FL, USA"))  ### Output: Coral Gables, FL, USA
print(generated_function("University of Virginia", "Charlottesville, VA"))  ### Output: Charlottesville, VA, USA
print(generated_function("Ohio State University", "Columbus, OH, USA"))  ### Output: Columbus, OH, USA
print(generated_function("Indiana University Bloomington", "Bloomington, IN, USA"))  ### Output: Bloomington, IN, USA
print(generated_function("University of North Carolina at Chapel Hill", "Chapel Hill, NC"))  ### Output: Chapel Hill, NC, USA
print(generated_function("University of Wisconsin Madison", "Madison, WI, USA"))  ### Output: Madison, WI, USA
print(generated_function("University of Georgia", "Athens, GA, USA"))  ### Output: Athens, GA, USA
print(generated_function("University of Arizona", "Tucson, AZ, USA"))  ### Output: Tucson, AZ, USA
print(generated_function("University of Texas at Austin", "Austin, TX"))  ### Output: Austin, TX, USA
print(generated_function("Northwestern University", "Evanston, IL"))  ### Output: Evanston, IL, USA
print(generated_function("University of Pittsburgh", "Pittsburgh, PA, USA"))  ### Output: Pittsburgh, PA, USA
print(generated_function("Brown University", "Providence, RI"))  ### Output: Providence, RI, USA
print(generated_function("University of Colorado Boulder", "Boulder, CO, USA"))  ### Output: Boulder, CO, USA
print(generated_function("Duke University", "Durham, NC"))  ### Output: Durham, NC, USA
print(generated_function("California Institute of Technology", "Pasadena, CA"))  ### Output: Pasadena, CA, USA
print(generated_function("University of Washington", "Seattle, WA"))  ### Output: Seattle, WA, USA
print(generated_function("University of Florida", "Gainesville, FL"))  ### Output: Gainesville, FL, USA
print(generated_function("Pennsylvania State University", "University Park, PA, USA"))  ### Output: University Park, PA, USA
print(generated_function("Georgia Institute of Technology", "Atlanta, GA"))  ### Output: Atlanta, GA, USA
print(generated_function("TAMU", "College Station, TX"))  ### Output: College Station, TX, USA
print(generated_function("Florida State University", "Tallahassee, FL, USA"))  ### Output: Tallahassee, FL, USA
print(generated_function("UCSD", "La Jolla, CA"))  ### Output: La Jolla, CA, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ### Output: Phialdelphia, PA, USA
print(generated_function("Carnegie Mellon University", "Pittsburgh, PA"))  ### Output: Pittsburgh, PA, USA
print(generated_function("University of Maryland, College Park", "College Park, MD, USA"))  ### Output: College Park, MD, USA
print(generated_function("USC", "Los Angeles, CA"))  ### Output: Los Angeles, CA, USA

# TEST SCRIPTS APPENDED!

