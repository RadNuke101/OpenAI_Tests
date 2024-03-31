# Start time: 2024-03-30 18:50:41.055650

# Content: Given that given input as ['Nancy FreeHafer'] output is Nancy, given input as ['Andrew Cencici'] output is Andrew, given input as ['Jan Kotas'] output is Jan, given input as ['Mariya Sergienko'] output is Mariya, given input as ['Launa Withers'] output is Launa, given input as ['Lakenya Edison'] output is Lakenya, given input as ['Brendan Hage'] output is Brendan, given input as ['Bradford Lango'] output is Bradford, given input as ['Rudolf Akiyama'] output is Rudolf, given input as ['Lara Constable'] output is Lara, given input as ['Madelaine Ghoston'] output is Madelaine, given input as ['Salley Hornak'] output is Salley, given input as ['Micha Junkin'] output is Micha, given input as ['Teddy Bobo'] output is Teddy, given input as ['Coralee Scalia'] output is Coralee, given input as ['Jeff Quashie'] output is Jeff, given input as ['Vena Babiarz'] output is Vena, given input as ['Karrie Lain'] output is Karrie, given input as ['Tobias Dermody'] output is Tobias, given input as ['Celsa Hopkins'] output is Celsa, given input as ['Kimberley Halpern'] output is Kimberley, given input as ['Phillip Rowden'] output is Phillip, given input as ['Elias Neil'] output is Elias, given input as ['Lashanda Cortes'] output is Lashanda, given input as ['Mackenzie Spell'] output is Mackenzie, given input as ['Kathlyn Eccleston'] output is Kathlyn, given input as ['Georgina Brescia'] output is Georgina, given input as ['Beata Miah'] output is Beata, given input as ['Desiree Seamons'] output is Desiree, given input as ['Jeanice Soderstrom'] output is Jeanice, given input as ['Mariel Jurgens'] output is Mariel, given input as ['Alida Bogle'] output is Alida, given input as ['Jacqualine Olague'] output is Jacqualine, given input as ['Joaquin Clasen'] output is Joaquin, given input as ['Samuel Richert'] output is Samuel, given input as ['Malissa Marcus'] output is Malissa, given input as ['Alaina Partida'] output is Alaina, given input as ['Trinidad Mulloy'] output is Trinidad, given input as ['Carlene Garrard'] output is Carlene, given input as ['Melodi Chism'] output is Melodi, given input as ['Bess Chilcott'] output is Bess, given input as ['Chong Aylward'] output is Chong, given input as ['Jani Ramthun'] output is Jani, given input as ['Jacquiline Heintz'] output is Jacquiline, given input as ['Hayley Marquess'] output is Hayley, given input as ['Andria Spagnoli'] output is Andria, given input as ['Irwin Covelli'] output is Irwin, given input as ['Gertude Montiel'] output is Gertude, given input as ['Stefany Reily'] output is Stefany, given input as ['Rae Mcgaughey'] output is Rae, given input as ['Cruz Latimore'] output is Cruz, given input as ['Maryann Casler'] output is Maryann, given input as ['Annalisa Gregori'] output is Annalisa, given input as ['Jenee Pannell'] output is Jenee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_first_name(full_name):
    # Input: 'Nancy FreeHafer' -> Output: 'Nancy'
    # Input: 'Andrew Cencici' -> Output: 'Andrew'
    # Input: 'Jan Kotas' -> Output: 'Jan'
    # Input: 'Mariya Sergienko' -> Output: 'Mariya'
    try:
        first_name = full_name.split()[0]
        return first_name
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(extract_first_name('Nancy FreeHafer'))  # Output: Nancy
print(extract_first_name('Andrew Cencici'))  # Output: Andrew
print(extract_first_name('Jan Kotas'))  # Output: Jan
print(extract_first_name('Mariya Sergienko'))  # Output: Mariya

# End time: 2024-03-30 18:50:45.184858
# Elapsed time in seconds: 4.12912024100001