# Start time: 2024-03-30 19:31:00.526632

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., given input as ['Launa Withers'] output is L.W., given input as ['Lakenya Edison'] output is L.E., given input as ['Brendan Hage'] output is B.H., given input as ['Bradford Lango'] output is B.L., given input as ['Rudolf Akiyama'] output is R.A., given input as ['Lara Constable'] output is L.C., given input as ['Madelaine Ghoston'] output is M.G., given input as ['Salley Hornak'] output is S.H., given input as ['Micha Junkin'] output is M.J., given input as ['Teddy Bobo'] output is T.B., given input as ['Coralee Scalia'] output is C.S., given input as ['Jeff Quashie'] output is J.Q., given input as ['Vena Babiarz'] output is V.B., given input as ['Karrie Lain'] output is K.L., given input as ['Tobias Dermody'] output is T.D., given input as ['Celsa Hopkins'] output is C.H., given input as ['Kimberley Halpern'] output is K.H., given input as ['Phillip Rowden'] output is P.R., given input as ['Elias Neil'] output is E.N., given input as ['Lashanda Cortes'] output is L.C., given input as ['Mackenzie Spell'] output is M.S., given input as ['Kathlyn Eccleston'] output is K.E., given input as ['Georgina Brescia'] output is G.B., given input as ['Beata Miah'] output is B.M., given input as ['Desiree Seamons'] output is D.S., given input as ['Jeanice Soderstrom'] output is J.S., given input as ['Mariel Jurgens'] output is M.J., given input as ['Alida Bogle'] output is A.B., given input as ['Jacqualine Olague'] output is J.O., given input as ['Joaquin Clasen'] output is J.C., given input as ['Samuel Richert'] output is S.R., given input as ['Malissa Marcus'] output is M.M., given input as ['Alaina Partida'] output is A.P., given input as ['Trinidad Mulloy'] output is T.M., given input as ['Carlene Garrard'] output is C.G., given input as ['Melodi Chism'] output is M.C., given input as ['Bess Chilcott'] output is B.C., given input as ['Chong Aylward'] output is C.A., given input as ['Jani Ramthun'] output is J.R., given input as ['Jacquiline Heintz'] output is J.H., given input as ['Hayley Marquess'] output is H.M., given input as ['Andria Spagnoli'] output is A.S., given input as ['Irwin Covelli'] output is I.C., given input as ['Gertude Montiel'] output is G.M., given input as ['Stefany Reily'] output is S.R., given input as ['Rae Mcgaughey'] output is R.M., given input as ['Cruz Latimore'] output is C.L., given input as ['Maryann Casler'] output is M.C., given input as ['Annalisa Gregori'] output is A.G., given input as ['Jenee Pannell'] output is J.P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'Nancy FreeHafer', output: 'N.F.'
# input: 'Andrew Cencici', output: 'A.C.'
# input: 'Jan Kotas', output: 'J.K.'
# input: 'Mariya Sergienko', output: 'M.S.'
# input: 'Launa Withers', output: 'L.W.'
# input: 'Lakenya Edison', output: 'L.E.'
# input: 'Brendan Hage', output: 'B.H.'
# input: 'Bradford Lango', output: 'B.L.'
# input: 'Rudolf Akiyama', output: 'R.A.'
# input: 'Lara Constable', output: 'L.C.'
# input: 'Madelaine Ghoston', output: 'M.G.'
# input: 'Salley Hornak', output: 'S.H.'
# input: 'Micha Junkin', output: 'M.J.'
# input: 'Teddy Bobo', output: 'T.B.'
# input: 'Coralee Scalia', output: 'C.S.'
# input: 'Jeff Quashie', output: 'J.Q.'
# input: 'Vena Babiarz', output: 'V.B.'
# input: 'Karrie Lain', output: 'K.L.'
# input: 'Tobias Dermody', output: 'T.D.'
# input: 'Celsa Hopkins', output: 'C.H.'
# input: 'Kimberley Halpern', output: 'K.H.'
# input: 'Phillip Rowden', output: 'P.R.'
# input: 'Elias Neil', output: 'E.N.'
# input: 'Lashanda Cortes', output: 'L.C.'
# input: 'Mackenzie Spell', output: 'M.S.'
# input: 'Kathlyn Eccleston', output: 'K.E.'
# input: 'Georgina Brescia', output: 'G.B.'
# input: 'Beata Miah', output: 'B.M.'
# input: 'Desiree Seamons', output: 'D.S.'
# input: 'Jeanice Soderstrom', output: 'J.S.'
# input: 'Mariel Jurgens', output: 'M.J.'
# input: 'Alida Bogle', output: 'A.B.'
# input: 'Jacqualine Olague', output: 'J.O.'
# input: 'Joaquin Clasen', output: 'J.C.'
# input: 'Samuel Richert', output: 'S.R.'
# input: 'Malissa Marcus', output: 'M.M.'
# input: 'Alaina Partida', output: 'A.P.'
# input: 'Trinidad Mulloy', output: 'T.M.'
# input: 'Carlene Garrard', output: 'C.G.'
# input: 'Melodi Chism', output: 'M.C.'
# input: 'Bess Chilcott', output: 'B.C.'
# input: 'Chong Aylward', output: 'C.A.'
# input: 'Jani Ramthun', output: 'J.R.'
# input: 'Jacquiline Heintz', output: 'J.H.'
# input: 'Hayley Marquess', output: 'H.M.'
# input: 'Andria Spagnoli', output: 'A.S.'
# input: 'Irwin Covelli', output: 'I.C.'
# input: 'Gertude Montiel', output: 'G.M.'
# input: 'Stefany Reily', output: 'S.R.'
# input: 'Rae Mcgaughey', output: 'R.M.'
# input: 'Cruz Latimore', output: 'C.L.'
# input: 'Maryann Casler', output: 'M.C.'
# input: 'Annalisa Gregori', output: 'A.G.'
# input: 'Jenee Pannell', output: 'J.P.'

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
print(generate_initials('Nancy FreeHafer'))
print(generate_initials('Andrew Cencici'))
print(generate_initials('Jan Kotas'))
print(generate_initials('Mariya Sergienko'))
print(generate_initials('Launa Withers'))
print(generate_initials('Lakenya Edison'))
print(generate_initials('Brendan Hage'))
print(generate_initials('Bradford Lango'))
print(generate_initials('Rudolf Akiyama'))
print(generate_initials('Lara Constable'))
print(generate_initials('Madelaine Ghoston'))
print(generate_initials('Salley Hornak'))
print(generate_initials('Micha Junkin'))
print(generate_initials('Teddy Bobo'))
print(generate_initials('Coralee Scalia'))
print(generate_initials('Jeff Quashie'))
print(generate_initials('Vena Babiarz'))
print(generate_initials('Karrie Lain'))
print(generate_initials('Tobias Dermody'))
print(generate_initials('Celsa Hopkins'))
print(generate_initials('Kimberley Halpern'))
print(generate_initials('Phillip Rowden'))
print(generate_initials('Elias Neil'))
print(generate_initials('Lashanda Cortes'))
print(generate_initials('Mackenzie Spell'))
print(generate_initials('Kathlyn Eccleston'))
print(generate_initials('Georgina Brescia'))
print(generate_initials('Beata Miah'))
print(generate_initials('Desiree Seamons'))
print(generate_initials('Jeanice Soderstrom'))
print(generate_initials('Mariel Jurgens'))
print(generate_initials('Alida Bogle'))
print(generate_initials('Jacqualine Olague'))
print(generate_initials('Joaquin Clasen'))
print(generate_initials('Samuel Richert'))
print(generate_initials('Malissa Marcus'))
print(generate_initials('Alaina Partida'))
print(generate_initials('Trinidad Mulloy'))
print(generate_initials('Carlene Garrard'))
print(generate_initials('Melodi Chism'))
print(generate_initials('Bess Chilcott'))
print(generate_initials('Chong Aylward'))
print(generate_initials('Jani Ramthun'))
print(generate_initials('Jacquiline Heintz'))
print(generate_initials('Hayley Marquess'))
print(generate_initials('Andria Spagnoli'))
print(generate_initials('Irwin Covelli'))
print(generate_initials('Gertude Montiel'))
print(generate_initials('Stefany Reily'))
print(generate_initials('Rae Mcgaughey'))
print(generate_initials('Cruz Latimore'))
print(generate_initials('Maryann Casler'))
print(generate_initials('Annalisa Gregori'))
print(generate_initials('Jenee Pannell'))

# End time: 2024-03-30 19:31:23.029146
# Elapsed time in seconds: 22.501838035999754