# Start time: 2024-04-09 13:49:54.493182

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two distinct columns. The first column contains the names of various universities, including prestigious institutions such as the University of Pennsylvania, UCLA, Cornell University, Penn (an informal name for the University of Pennsylvania), University of Maryland College Park, and the University of Michigan. These universities are recognized for their academic excellence and are located across different states in the USA.

The second column provides specific geographic locations associated with each university listed in the first column. These locations include cities and states within the USA, such as Philadelphia, PA; Los Angeles, CA; Ithaca, New York; College Park, MD; and Ann Arbor, MI. Some entries in this column also explicitly include "USA" to denote the country, while others omit it, assuming it to be understood.

### Output Column Summary:

The output data combines the information from the two input columns into a single, cohesive format. Each output entry consists of the university's name followed by its geographic location, including the city, state, and, where initially omitted, the country (USA) is explicitly added. This standardized format ensures clarity and uniformity across all entries, making it easier to understand the specific location of each university within the United States. The addition of "USA" to entries that originally lacked this detail helps to provide a complete and consistent geographic context for each university.

### Relationship Summary:

The transformation from input to output data demonstrates a process of standardization and clarification. The input data, split into two columns, provides basic information about various universities and their locations. The output data then synthesizes this information into a single, more informative format by combining the university names with their full geographic locations, including the addition of "USA" where necessary. This process not only ensures consistency across all entries but also enhances the clarity of the information presented, making it immediately clear that all the universities listed are located within the United States. This relationship between the input and output data underscores the importance of data presentation in conveying clear and comprehensive information., and input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(university_name, location):
    """
    This function takes the name of a university and its geographic location as inputs,
    and returns a single string that combines both pieces of information in a standardized format.
    If the location does not already include 'USA', it is added to ensure clarity and consistency.
    
    Parameters:
    university_name (str): The name of the university.
    location (str): The geographic location of the university, including city and state.
    
    Returns:
    str: A standardized string combining the university's name and its full geographic location.
    """
    # Check if 'USA' is already part of the location string
    if 'USA' not in location:
        # If 'USA' is not included, add it to the location
        location += ', USA'
    
    # Combine the university name and the location into a single string
    output = f"{university_name}, {location}"
    
    return output

# Test cases
print(generated_function('University of Pennsylvania', 'Philadelphia, PA, USA'))
print(generated_function('UCLA', 'Los Angeles, CA'))
print(generated_function('Cornell University', 'Ithaca, New York, USA'))
print(generated_function('Penn', 'Philadelphia, PA, USA'))
print(generated_function('University of Maryland College Park', 'College Park, MD'))
print(generated_function('University of Michigan', 'Ann Arbor, MI, USA'))
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: University of Pennsylvania, Phialdelphia, PA, USA
print(generated_function("UCLA", "Los Angeles, CA"))  ## Output: UCLA, Los Angeles, CA, USA
print(generated_function("Cornell University", "Ithaca, New York, USA"))  ## Output: Cornell University, Ithaca, New York, USA
print(generated_function("Penn", "Philadelphia, PA, USA"))  ## Output: Penn, Philadelphia, PA, USA
print(generated_function("University of Maryland College Park", "College Park, MD"))  ## Output: University of Maryland College Park, College Park, MD, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: University of Michigan, Ann Arbor, MI, USA

# End time: 2024-04-09 13:50:08.905427
# Elapsed time in seconds: 14.411829872999988


# APPEND TEST SCRIPTS...
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: University of Pennsylvania, Phialdelphia, PA, USA
print(generated_function("UCLA", "Los Angeles, CA"))  ## Output: UCLA, Los Angeles, CA, USA
print(generated_function("Cornell University", "Ithaca, New York, USA"))  ## Output: Cornell University, Ithaca, New York, USA
print(generated_function("Penn", "Philadelphia, PA, USA"))  ## Output: Penn, Philadelphia, PA, USA
print(generated_function("University of Maryland College Park", "College Park, MD"))  ## Output: University of Maryland College Park, College Park, MD, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: University of Michigan, Ann Arbor, MI, USA


print(generated_function("University of Pittsburgh", "Pittsburgh, PA, USA"))  ### Output: University of Pittsburgh, Pittsburgh, PA, USA
print(generated_function("Duke University", "Durham, NC"))  ### Output: Duke University, Durham, NC, USA
print(generated_function("UCSD", "La Jolla, CA"))  ### Output: UCSD, La Jolla, CA, USA
print(generated_function("California Institute of Technology", "Pasadena, CA"))  ### Output: California Institute of Technology, Pasadena, CA, USA
print(generated_function("Pennsylvania State University", "University Park, PA, USA"))  ### Output: Pennsylvania State University, University Park, PA, USA
print(generated_function("University of Oregon", "Eugene, OR, USA"))  ### Output: University of Oregon, Eugene, OR, USA
print(generated_function("University of Maryland, College Park", "College Park, MD, USA"))  ### Output: University of Maryland, College Park, College Park, MD, USA
print(generated_function("Florida State University", "Tallahassee, FL, USA"))  ### Output: Florida State University, Tallahassee, FL, USA
print(generated_function("Northwestern University", "Evanston, IL"))  ### Output: Northwestern University, Evanston, IL, USA
print(generated_function("University of North Carolina at Chapel Hill", "Chapel Hill, NC"))  ### Output: University of North Carolina at Chapel Hill, Chapel Hill, NC, USA
print(generated_function("Georgia Institute of Technology", "Atlanta, GA"))  ### Output: Georgia Institute of Technology, Atlanta, GA, USA
print(generated_function("University of Minnesota Twin Cities", "Minneapolis, MN, USA"))  ### Output: University of Minnesota Twin Cities, Minneapolis, MN, USA
print(generated_function("Rutgers, The State University of New Jersey", "New Brunswick, NJ, USA"))  ### Output: Rutgers, The State University of New Jersey, New Brunswick, NJ, USA
print(generated_function("University of Florida", "Gainesville, FL"))  ### Output: University of Florida, Gainesville, FL, USA
print(generated_function("University of Texas at Austin", "Austin, TX"))  ### Output: University of Texas at Austin, Austin, TX, USA
print(generated_function("University of Iowa", "Iowa City, IA, USA"))  ### Output: University of Iowa, Iowa City, IA, USA
print(generated_function("University of Miami", "Coral Gables, FL, USA"))  ### Output: University of Miami, Coral Gables, FL, USA
print(generated_function("University of Georgia", "Athens, GA, USA"))  ### Output: University of Georgia, Athens, GA, USA
print(generated_function("University of Washington", "Seattle, WA"))  ### Output: University of Washington, Seattle, WA, USA
print(generated_function("University of Arizona", "Tucson, AZ, USA"))  ### Output: University of Arizona, Tucson, AZ, USA
print(generated_function("USC", "Los Angeles, CA"))  ### Output: USC, Los Angeles, CA, USA
print(generated_function("University of Wisconsin Madison", "Madison, WI, USA"))  ### Output: University of Wisconsin Madison, Madison, WI, USA
print(generated_function("TAMU", "College Station, TX"))  ### Output: TAMU, College Station, TX, USA
print(generated_function("Indiana University Bloomington", "Bloomington, IN, USA"))  ### Output: Indiana University Bloomington, Bloomington, IN, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ### Output: University of Pennsylvania, Phialdelphia, PA, USA
print(generated_function("Virginia Tech", "Blacksburg, VA, USA"))  ### Output: Virginia Tech, Blacksburg, VA, USA
print(generated_function("Brown University", "Providence, RI"))  ### Output: Brown University, Providence, RI, USA
print(generated_function("Johns Hopkins University", "Baltimore, MD"))  ### Output: Johns Hopkins University, Baltimore, MD, USA
print(generated_function("University of Virginia", "Charlottesville, VA"))  ### Output: University of Virginia, Charlottesville, VA, USA
print(generated_function("University of Colorado Boulder", "Boulder, CO, USA"))  ### Output: University of Colorado Boulder, Boulder, CO, USA
print(generated_function("Carnegie Mellon University", "Pittsburgh, PA"))  ### Output: Carnegie Mellon University, Pittsburgh, PA, USA
print(generated_function("Ohio State University", "Columbus, OH, USA"))  ### Output: Ohio State University, Columbus, OH, USA

# TEST SCRIPTS APPENDED!

