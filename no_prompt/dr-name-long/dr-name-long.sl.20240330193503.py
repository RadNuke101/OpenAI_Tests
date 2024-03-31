# Start time: 2024-03-30 19:50:13.965608

# Content: Given that given input as ['Launa Withers'] output is Dr. Launa, given input as ['Lakenya Edison'] output is Dr. Lakenya, given input as ['Brendan Hage'] output is Dr. Brendan, given input as ['Bradford Lango'] output is Dr. Bradford, given input as ['Rudolf Akiyama'] output is Dr. Rudolf, given input as ['Lara Constable'] output is Dr. Lara, given input as ['Madelaine Ghoston'] output is Dr. Madelaine, given input as ['Salley Hornak'] output is Dr. Salley, given input as ['Micha Junkin'] output is Dr. Micha, given input as ['Teddy Bobo'] output is Dr. Teddy, given input as ['Coralee Scalia'] output is Dr. Coralee, given input as ['Jeff Quashie'] output is Dr. Jeff, given input as ['Vena Babiarz'] output is Dr. Vena, given input as ['Karrie Lain'] output is Dr. Karrie, given input as ['Tobias Dermody'] output is Dr. Tobias, given input as ['Celsa Hopkins'] output is Dr. Celsa, given input as ['Kimberley Halpern'] output is Dr. Kimberley, given input as ['Phillip Rowden'] output is Dr. Phillip, given input as ['Elias Neil'] output is Dr. Elias, given input as ['Lashanda Cortes'] output is Dr. Lashanda, given input as ['Mackenzie Spell'] output is Dr. Mackenzie, given input as ['Kathlyn Eccleston'] output is Dr. Kathlyn, given input as ['Georgina Brescia'] output is Dr. Georgina, given input as ['Beata Miah'] output is Dr. Beata, given input as ['Desiree Seamons'] output is Dr. Desiree, given input as ['Jeanice Soderstrom'] output is Dr. Jeanice, given input as ['Mariel Jurgens'] output is Dr. Mariel, given input as ['Alida Bogle'] output is Dr. Alida, given input as ['Jacqualine Olague'] output is Dr. Jacqualine, given input as ['Joaquin Clasen'] output is Dr. Joaquin, given input as ['Samuel Richert'] output is Dr. Samuel, given input as ['Malissa Marcus'] output is Dr. Malissa, given input as ['Alaina Partida'] output is Dr. Alaina, given input as ['Trinidad Mulloy'] output is Dr. Trinidad, given input as ['Carlene Garrard'] output is Dr. Carlene, given input as ['Melodi Chism'] output is Dr. Melodi, given input as ['Bess Chilcott'] output is Dr. Bess, given input as ['Chong Aylward'] output is Dr. Chong, given input as ['Jani Ramthun'] output is Dr. Jani, given input as ['Jacquiline Heintz'] output is Dr. Jacquiline, given input as ['Hayley Marquess'] output is Dr. Hayley, given input as ['Andria Spagnoli'] output is Dr. Andria, given input as ['Irwin Covelli'] output is Dr. Irwin, given input as ['Gertude Montiel'] output is Dr. Gertude, given input as ['Stefany Reily'] output is Dr. Stefany, given input as ['Rae Mcgaughey'] output is Dr. Rae, given input as ['Cruz Latimore'] output is Dr. Cruz, given input as ['Maryann Casler'] output is Dr. Maryann, given input as ['Annalisa Gregori'] output is Dr. Annalisa, given input as ['Jenee Pannell'] output is Dr. Jenee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_doctor_name(input_name):
    try:
        # Input: 'Launa Withers'
        # Output: 'Dr. Launa'
        first_name = input_name.split()[0]
        return 'Dr. ' + first_name
    except Exception as e:
        print("Error: ", e)

# Test cases
print(get_doctor_name('Launa Withers'))
print(get_doctor_name('Lakenya Edison'))
print(get_doctor_name('Brendan Hage'))
print(get_doctor_name('Bradford Lango'))
print(get_doctor_name('Rudolf Akiyama'))
print(get_doctor_name('Lara Constable'))
print(get_doctor_name('Madelaine Ghoston'))
print(get_doctor_name('Salley Hornak'))
print(get_doctor_name('Micha Junkin'))
print(get_doctor_name('Teddy Bobo'))
print(get_doctor_name('Coralee Scalia'))
print(get_doctor_name('Jeff Quashie'))
print(get_doctor_name('Vena Babiarz'))
print(get_doctor_name('Karrie Lain'))
print(get_doctor_name('Tobias Dermody'))
print(get_doctor_name('Celsa Hopkins'))
print(get_doctor_name('Kimberley Halpern'))
print(get_doctor_name('Phillip Rowden'))
print(get_doctor_name('Elias Neil'))
print(get_doctor_name('Lashanda Cortes'))
print(get_doctor_name('Mackenzie Spell'))
print(get_doctor_name('Kathlyn Eccleston'))
print(get_doctor_name('Georgina Brescia'))
print(get_doctor_name('Beata Miah'))
print(get_doctor_name('Desiree Seamons'))
print(get_doctor_name('Jeanice Soderstrom'))
print(get_doctor_name('Mariel Jurgens'))
print(get_doctor_name('Alida Bogle'))
print(get_doctor_name('Jacqualine Olague'))
print(get_doctor_name('Joaquin Clasen'))
print(get_doctor_name('Samuel Richert'))
print(get_doctor_name('Malissa Marcus'))
print(get_doctor_name('Alaina Partida'))
print(get_doctor_name('Trinidad Mulloy'))
print(get_doctor_name('Carlene Garrard'))
print(get_doctor_name('Melodi Chism'))
print(get_doctor_name('Bess Chilcott'))
print(get_doctor_name('Chong Aylward'))
print(get_doctor_name('Jani Ramthun'))
print(get_doctor_name('Jacquiline Heintz'))
print(get_doctor_name('Hayley Marquess'))
print(get_doctor_name('Andria Spagnoli'))
print(get_doctor_name('Irwin Covelli'))
print(get_doctor_name('Gertude Montiel'))
print(get_doctor_name('Stefany Reily'))
print(get_doctor_name('Rae Mcgaughey'))
print(get_doctor_name('Cruz Latimore'))
print(get_doctor_name('Maryann Casler'))
print(get_doctor_name('Annalisa Gregori'))
print(get_doctor_name('Jenee Pannell'))

# End time: 2024-03-30 19:50:21.102344
# Elapsed time in seconds: 7.136534320999999