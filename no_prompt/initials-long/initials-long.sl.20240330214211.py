# Start time: 2024-03-30 21:54:45.722302

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., given input as ['Launa Withers'] output is L.W., given input as ['Lakenya Edison'] output is L.E., given input as ['Brendan Hage'] output is B.H., given input as ['Bradford Lango'] output is B.L., given input as ['Rudolf Akiyama'] output is R.A., given input as ['Lara Constable'] output is L.C., given input as ['Madelaine Ghoston'] output is M.G., given input as ['Salley Hornak'] output is S.H., given input as ['Micha Junkin'] output is M.J., given input as ['Teddy Bobo'] output is T.B., given input as ['Coralee Scalia'] output is C.S., given input as ['Jeff Quashie'] output is J.Q., given input as ['Vena Babiarz'] output is V.B., given input as ['Karrie Lain'] output is K.L., given input as ['Tobias Dermody'] output is T.D., given input as ['Celsa Hopkins'] output is C.H., given input as ['Kimberley Halpern'] output is K.H., given input as ['Phillip Rowden'] output is P.R., given input as ['Elias Neil'] output is E.N., given input as ['Lashanda Cortes'] output is L.C., given input as ['Mackenzie Spell'] output is M.S., given input as ['Kathlyn Eccleston'] output is K.E., given input as ['Georgina Brescia'] output is G.B., given input as ['Beata Miah'] output is B.M., given input as ['Desiree Seamons'] output is D.S., given input as ['Jeanice Soderstrom'] output is J.S., given input as ['Mariel Jurgens'] output is M.J., given input as ['Alida Bogle'] output is A.B., given input as ['Jacqualine Olague'] output is J.O., given input as ['Joaquin Clasen'] output is J.C., given input as ['Samuel Richert'] output is S.R., given input as ['Malissa Marcus'] output is M.M., given input as ['Alaina Partida'] output is A.P., given input as ['Trinidad Mulloy'] output is T.M., given input as ['Carlene Garrard'] output is C.G., given input as ['Melodi Chism'] output is M.C., given input as ['Bess Chilcott'] output is B.C., given input as ['Chong Aylward'] output is C.A., given input as ['Jani Ramthun'] output is J.R., given input as ['Jacquiline Heintz'] output is J.H., given input as ['Hayley Marquess'] output is H.M., given input as ['Andria Spagnoli'] output is A.S., given input as ['Irwin Covelli'] output is I.C., given input as ['Gertude Montiel'] output is G.M., given input as ['Stefany Reily'] output is S.R., given input as ['Rae Mcgaughey'] output is R.M., given input as ['Cruz Latimore'] output is C.L., given input as ['Maryann Casler'] output is M.C., given input as ['Annalisa Gregori'] output is A.G., given input as ['Jenee Pannell'] output is J.P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
# Input: 'Nancy FreeHafer', Output: 'N.F.'
# Input: 'Andrew Cencici', Output: 'A.C.'
# Input: 'Jan Kotas', Output: 'J.K.'
# Input: 'Mariya Sergienko', Output: 'M.S.'
# Input: 'Launa Withers', Output: 'L.W.'
# Input: 'Lakenya Edison', Output: 'L.E.'
# Input: 'Brendan Hage', Output: 'B.H.'
# Input: 'Bradford Lango', Output: 'B.L.'
# Input: 'Rudolf Akiyama', Output: 'R.A.'
# Input: 'Lara Constable', Output: 'L.C.'
# Input: 'Madelaine Ghoston', Output: 'M.G.'
# Input: 'Salley Hornak', Output: 'S.H.'
# Input: 'Micha Junkin', Output: 'M.J.'
# Input: 'Teddy Bobo', Output: 'T.B.'
# Input: 'Coralee Scalia', Output: 'C.S.'
# Input: 'Jeff Quashie', Output: 'J.Q.'
# Input: 'Vena Babiarz', Output: 'V.B.'
# Input: 'Karrie Lain', Output: 'K.L.'
# Input: 'Tobias Dermody', Output: 'T.D.'
# Input: 'Celsa Hopkins', Output: 'C.H.'
# Input: 'Kimberley Halpern', Output: 'K.H.'
# Input: 'Phillip Rowden', Output: 'P.R.'
# Input: 'Elias Neil', Output: 'E.N.'
# Input: 'Lashanda Cortes', Output: 'L.C.'
# Input: 'Mackenzie Spell', Output: 'M.S.'
# Input: 'Kathlyn Eccleston', Output: 'K.E.'
# Input: 'Georgina Brescia', Output: 'G.B.'
# Input: 'Beata Miah', Output: 'B.M.'
# Input: 'Desiree Seamons', Output: 'D.S.'
# Input: 'Jeanice Soderstrom', Output: 'J.S.'
# Input: 'Mariel Jurgens', Output: 'M.J.'
# Input: 'Alida Bogle', Output: 'A.B.'
# Input: 'Jacqualine Olague', Output: 'J.O.'
# Input: 'Joaquin Clasen', Output: 'J.C.'
# Input: 'Samuel Richert', Output: 'S.R.'
# Input: 'Malissa Marcus', Output: 'M.M.'
# Input: 'Alaina Partida', Output: 'A.P.'
# Input: 'Trinidad Mulloy', Output: 'T.M.'
# Input: 'Carlene Garrard', Output: 'C.G.'
# Input: 'Melodi Chism', Output: 'M.C.'
# Input: 'Bess Chilcott', Output: 'B.C.'
# Input: 'Chong Aylward', Output: 'C.A.'
# Input: 'Jani Ramthun', Output: 'J.R.'
# Input: 'Jacquiline Heintz', Output: 'J.H.'
# Input: 'Hayley Marquess', Output: 'H.M.'
# Input: 'Andria Spagnoli', Output: 'A.S.'
# Input: 'Irwin Covelli', Output: 'I.C.'
# Input: 'Gertude Montiel', Output: 'G.M.'
# Input: 'Stefany Reily', Output: 'S.R.'
# Input: 'Rae Mcgaughey', Output: 'R.M.'
# Input: 'Cruz Latimore', Output: 'C.L.'
# Input: 'Maryann Casler', Output: 'M.C.'
# Input: 'Annalisa Gregori', Output: 'A.G.'
# Input: 'Jenee Pannell', Output: 'J.P.'

def generate_initials(name):
    try:
        # Split the name into parts
        parts = name.split()
        
        # Get the first letter of the first name and last name
        first_initial = parts[0][0]
        last_initial = parts[-1][0]
        
        # Return the initials in the format 'F.L.'
        return f'{first_initial.upper()}.{last_initial.upper()}.'
    except:
        return "Invalid input"

# Test the function with the provided test cases
test_cases = ['Nancy FreeHafer', 'Andrew Cencici', 'Jan Kotas', 'Mariya Sergienko', 'Launa Withers', 'Lakenya Edison', 'Brendan Hage', 'Bradford Lango', 'Rudolf Akiyama', 'Lara Constable', 'Madelaine Ghoston', 'Salley Hornak', 'Micha Junkin', 'Teddy Bobo', 'Coralee Scalia', 'Jeff Quashie', 'Vena Babiarz', 'Karrie Lain', 'Tobias Dermody', 'Celsa Hopkins', 'Kimberley Halpern', 'Phillip Rowden', 'Elias Neil', 'Lashanda Cortes', 'Mackenzie Spell', 'Kathlyn Eccleston', 'Georgina Brescia', 'Beata Miah', 'Desiree Seamons', 'Jeanice Soderstrom', 'Mariel Jurgens', 'Alida Bogle', 'Jacqualine Olague', 'Joaquin Clasen', 'Samuel Richert', 'Malissa Marcus', 'Alaina Partida', 'Trinidad Mulloy', 'Carlene Garrard', 'Melodi Chism', 'Bess Chilcott', 'Chong Aylward', 'Jani Ramthun', 'Jacquiline Heintz', 'Hayley Marquess', 'Andria Spagnoli', 'Irwin Covelli', 'Gertude Montiel', 'Stefany Reily', 'Rae Mcgaughey', 'Cruz Latimore', 'Maryann Casler', 'Annalisa Gregori', 'Jenee Pannell']

for test_case in test_cases:
    print(f"Input: '{test_case}', Output: '{generate_initials(test_case)}'")

# End time: 2024-03-30 21:54:57.368064
# Elapsed time in seconds: 11.645431931998246