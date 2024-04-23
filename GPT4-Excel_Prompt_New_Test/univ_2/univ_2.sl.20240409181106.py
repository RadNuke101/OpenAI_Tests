# Start time: 2024-04-09 19:23:00.433268

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two distinct columns, each containing specific pieces of information about various universities in the United States. The first column provides the name of the university, which can range from well-known abbreviations (e.g., "UCLA") to the full official names (e.g., "University of Pennsylvania"). The second column offers geographical details, specifying the city and state where the university is located. In some instances, the country ("USA") is also included, while in others, it is omitted, leaving just the city and state.

### Output Column Summary:

The output data consolidates the information provided in the two input columns into a single, cohesive format. It presents the name of the university followed by its geographical location, including the city, state, and, when initially omitted, the country ("USA") is appended to ensure uniformity across all entries. This format provides a clear and concise way to identify each university's name and its specific location within the United States, making it easier to understand and reference.

### Relationship Between Input and Output:

The transformation from input to output demonstrates a process of standardization and completeness. By merging the two input columns into one and ensuring that the geographical location always includes the country (when not originally specified), the output offers a more standardized and comprehensive way to present the information. This process highlights the importance of consistency in data presentation, especially when dealing with qualitative data that involves names and locations. The output makes it easier for the information to be understood and utilized, regardless of the initial format or level of detail provided in the input., and input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(university_name, location):
    """
    This function takes the name of a university and its geographical location as inputs,
    and returns a standardized string format that combines both pieces of information,
    appending ", USA" to the location if it is not already included.
    
    Parameters:
    university_name (str): The name of the university.
    location (str): The geographical location of the university, including city and state.
    
    Returns:
    str: A standardized string combining the university name and its location, with ", USA"
         appended if the country is not specified in the input.
    """
    # Check if the location already includes "USA"
    if "USA" not in location:
        # Append ", USA" if it's not included
        location += ", USA"
    
    # Combine the university name and location into a single string
    output = f"{university_name}, {location}"
    
    return output

# Test cases
print(generated_function('University of Pennsylvania', 'Phialdelphia, PA, USA'))
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

# End time: 2024-04-09 19:23:11.597153
# Elapsed time in seconds: 11.163610378000158


# APPEND TEST SCRIPTS...
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ## Output: University of Pennsylvania, Phialdelphia, PA, USA
print(generated_function("UCLA", "Los Angeles, CA"))  ## Output: UCLA, Los Angeles, CA, USA
print(generated_function("Cornell University", "Ithaca, New York, USA"))  ## Output: Cornell University, Ithaca, New York, USA
print(generated_function("Penn", "Philadelphia, PA, USA"))  ## Output: Penn, Philadelphia, PA, USA
print(generated_function("University of Maryland College Park", "College Park, MD"))  ## Output: University of Maryland College Park, College Park, MD, USA
print(generated_function("University of Michigan", "Ann Arbor, MI, USA"))  ## Output: University of Michigan, Ann Arbor, MI, USA


print(generated_function("Indiana University Bloomington", "Bloomington, IN, USA"))  ### Output: Indiana University Bloomington, Bloomington, IN, USA
print(generated_function("University of Colorado Boulder", "Boulder, CO, USA"))  ### Output: University of Colorado Boulder, Boulder, CO, USA
print(generated_function("Carnegie Mellon University", "Pittsburgh, PA"))  ### Output: Carnegie Mellon University, Pittsburgh, PA, USA
print(generated_function("University of Virginia", "Charlottesville, VA"))  ### Output: University of Virginia, Charlottesville, VA, USA
print(generated_function("Brown University", "Providence, RI"))  ### Output: Brown University, Providence, RI, USA
print(generated_function("University of Arizona", "Tucson, AZ, USA"))  ### Output: University of Arizona, Tucson, AZ, USA
print(generated_function("University of Miami", "Coral Gables, FL, USA"))  ### Output: University of Miami, Coral Gables, FL, USA
print(generated_function("Virginia Tech", "Blacksburg, VA, USA"))  ### Output: Virginia Tech, Blacksburg, VA, USA
print(generated_function("University of Iowa", "Iowa City, IA, USA"))  ### Output: University of Iowa, Iowa City, IA, USA
print(generated_function("University of Washington", "Seattle, WA"))  ### Output: University of Washington, Seattle, WA, USA
print(generated_function("University of Florida", "Gainesville, FL"))  ### Output: University of Florida, Gainesville, FL, USA
print(generated_function("UCSD", "La Jolla, CA"))  ### Output: UCSD, La Jolla, CA, USA
print(generated_function("University of Maryland, College Park", "College Park, MD, USA"))  ### Output: University of Maryland, College Park, College Park, MD, USA
print(generated_function("TAMU", "College Station, TX"))  ### Output: TAMU, College Station, TX, USA
print(generated_function("University of Oregon", "Eugene, OR, USA"))  ### Output: University of Oregon, Eugene, OR, USA
print(generated_function("Duke University", "Durham, NC"))  ### Output: Duke University, Durham, NC, USA
print(generated_function("University of Texas at Austin", "Austin, TX"))  ### Output: University of Texas at Austin, Austin, TX, USA
print(generated_function("Rutgers, The State University of New Jersey", "New Brunswick, NJ, USA"))  ### Output: Rutgers, The State University of New Jersey, New Brunswick, NJ, USA
print(generated_function("University of Pittsburgh", "Pittsburgh, PA, USA"))  ### Output: University of Pittsburgh, Pittsburgh, PA, USA
print(generated_function("Ohio State University", "Columbus, OH, USA"))  ### Output: Ohio State University, Columbus, OH, USA
print(generated_function("Johns Hopkins University", "Baltimore, MD"))  ### Output: Johns Hopkins University, Baltimore, MD, USA
print(generated_function("Northwestern University", "Evanston, IL"))  ### Output: Northwestern University, Evanston, IL, USA
print(generated_function("Georgia Institute of Technology", "Atlanta, GA"))  ### Output: Georgia Institute of Technology, Atlanta, GA, USA
print(generated_function("USC", "Los Angeles, CA"))  ### Output: USC, Los Angeles, CA, USA
print(generated_function("Pennsylvania State University", "University Park, PA, USA"))  ### Output: Pennsylvania State University, University Park, PA, USA
print(generated_function("California Institute of Technology", "Pasadena, CA"))  ### Output: California Institute of Technology, Pasadena, CA, USA
print(generated_function("Florida State University", "Tallahassee, FL, USA"))  ### Output: Florida State University, Tallahassee, FL, USA
print(generated_function("University of Minnesota Twin Cities", "Minneapolis, MN, USA"))  ### Output: University of Minnesota Twin Cities, Minneapolis, MN, USA
print(generated_function("University of Pennsylvania", "Phialdelphia, PA, USA"))  ### Output: University of Pennsylvania, Phialdelphia, PA, USA
print(generated_function("University of North Carolina at Chapel Hill", "Chapel Hill, NC"))  ### Output: University of North Carolina at Chapel Hill, Chapel Hill, NC, USA
print(generated_function("University of Wisconsin Madison", "Madison, WI, USA"))  ### Output: University of Wisconsin Madison, Madison, WI, USA
print(generated_function("University of Georgia", "Athens, GA, USA"))  ### Output: University of Georgia, Athens, GA, USA

# TEST SCRIPTS APPENDED!

