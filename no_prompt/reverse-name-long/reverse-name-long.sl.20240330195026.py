# Start time: 2024-03-30 20:03:34.634960

# Content: Given that given input as ['Launa', 'Withers'] output is Withers Launa, given input as ['Lakenya', 'Edison'] output is Edison Lakenya, given input as ['Brendan', 'Hage'] output is Hage Brendan, given input as ['Bradford', 'Lango'] output is Lango Bradford, given input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, given input as ['Lara', 'Constable'] output is Constable Lara, given input as ['Madelaine', 'Ghoston'] output is Ghoston Madelaine, given input as ['Salley', 'Hornak'] output is Hornak Salley, given input as ['Micha', 'Junkin'] output is Junkin Micha, given input as ['Teddy', 'Bobo'] output is Bobo Teddy, given input as ['Coralee', 'Scalia'] output is Scalia Coralee, given input as ['Jeff', 'Quashie'] output is Quashie Jeff, given input as ['Vena', 'Babiarz'] output is Babiarz Vena, given input as ['Karrie', 'Lain'] output is Lain Karrie, given input as ['Tobias', 'Dermody'] output is Dermody Tobias, given input as ['Celsa', 'Hopkins'] output is Hopkins Celsa, given input as ['Kimberley', 'Halpern'] output is Halpern Kimberley, given input as ['Phillip', 'Rowden'] output is Rowden Phillip, given input as ['Elias', 'Neil'] output is Neil Elias, given input as ['Lashanda', 'Cortes'] output is Cortes Lashanda, given input as ['Mackenzie', 'Spell'] output is Spell Mackenzie, given input as ['Kathlyn', 'Eccleston'] output is Eccleston Kathlyn, given input as ['Georgina', 'Brescia'] output is Brescia Georgina, given input as ['Beata', 'Miah'] output is Miah Beata, given input as ['Desiree', 'Seamons'] output is Seamons Desiree, given input as ['Jeanice', 'Soderstrom'] output is Soderstrom Jeanice, given input as ['Mariel', 'Jurgens'] output is Jurgens Mariel, given input as ['Alida', 'Bogle'] output is Bogle Alida, given input as ['Jacqualine', 'Olague'] output is Olague Jacqualine, given input as ['Joaquin', 'Clasen'] output is Clasen Joaquin, given input as ['Samuel', 'Richert'] output is Richert Samuel, given input as ['Malissa', 'Marcus'] output is Marcus Malissa, given input as ['Alaina', 'Partida'] output is Partida Alaina, given input as ['Trinidad', 'Mulloy'] output is Mulloy Trinidad, given input as ['Carlene', 'Garrard'] output is Garrard Carlene, given input as ['Melodi', 'Chism'] output is Chism Melodi, given input as ['Bess', 'Chilcott'] output is Chilcott Bess, given input as ['Chong', 'Aylward'] output is Aylward Chong, given input as ['Jani', 'Ramthun'] output is Ramthun Jani, given input as ['Jacquiline', 'Heintz'] output is Heintz Jacquiline, given input as ['Hayley', 'Marquess'] output is Marquess Hayley, given input as ['Andria', 'Spagnoli'] output is Spagnoli Andria, given input as ['Irwin', 'Covelli'] output is Covelli Irwin, given input as ['Gertude', 'Montiel'] output is Montiel Gertude, given input as ['Stefany', 'Reily'] output is Reily Stefany, given input as ['Rae', 'Mcgaughey'] output is Mcgaughey Rae, given input as ['Cruz', 'Latimore'] output is Latimore Cruz, given input as ['Maryann', 'Casler'] output is Casler Maryann, given input as ['Annalisa', 'Gregori'] output is Gregori Annalisa, given input as ['Jenee', 'Pannell'] output is Pannell Jenee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def rearrange_names(input_str):
    try:
        # Input: "Launa Withers"
        # Output: "Withers Launa"
        first_name, last_name = input_str.split()
        return f"{last_name} {first_name}"
    except ValueError:
        print("Invalid input format. Please provide two names separated by a space.")

# Test cases
print(rearrange_names("Launa Withers"))
print(rearrange_names("Lakenya Edison"))
print(rearrange_names("Brendan Hage"))
print(rearrange_names("Bradford Lango"))
print(rearrange_names("Rudolf Akiyama"))
print(rearrange_names("Lara Constable"))
print(rearrange_names("Madelaine Ghoston"))
print(rearrange_names("Salley Hornak"))
print(rearrange_names("Micha Junkin"))
print(rearrange_names("Teddy Bobo"))
print(rearrange_names("Coralee Scalia"))
print(rearrange_names("Jeff Quashie"))
print(rearrange_names("Vena Babiarz"))
print(rearrange_names("Karrie Lain"))
print(rearrange_names("Tobias Dermody"))
print(rearrange_names("Celsa Hopkins"))
print(rearrange_names("Kimberley Halpern"))
print(rearrange_names("Phillip Rowden"))
print(rearrange_names("Elias Neil"))
print(rearrange_names("Lashanda Cortes"))
print(rearrange_names("Mackenzie Spell"))
print(rearrange_names("Kathlyn Eccleston"))
print(rearrange_names("Georgina Brescia"))
print(rearrange_names("Beata Miah"))
print(rearrange_names("Desiree Seamons"))
print(rearrange_names("Jeanice Soderstrom"))
print(rearrange_names("Mariel Jurgens"))
print(rearrange_names("Alida Bogle"))
print(rearrange_names("Jacqualine Olague"))
print(rearrange_names("Joaquin Clasen"))
print(rearrange_names("Samuel Richert"))
print(rearrange_names("Malissa Marcus"))
print(rearrange_names("Alaina Partida"))
print(rearrange_names("Trinidad Mulloy"))
print(rearrange_names("Carlene Garrard"))
print(rearrange_names("Melodi Chism"))
print(rearrange_names("Bess Chilcott"))
print(rearrange_names("Chong Aylward"))
print(rearrange_names("Jani Ramthun"))
print(rearrange_names("Jacquiline Heintz"))
print(rearrange_names("Hayley Marquess"))
print(rearrange_names("Andria Spagnoli"))
print(rearrange_names("Irwin Covelli"))
print(rearrange_names("Gertude Montiel"))
print(rearrange_names("Stefany Reily"))
print(rearrange_names("Rae Mcgaughey"))
print(rearrange_names("Cruz Latimore"))
print(rearrange_names("Maryann Casler"))
print(rearrange_names("Annalisa Gregori"))
print(rearrange_names("Jenee Pannell"))

# End time: 2024-03-30 20:03:47.257786
# Elapsed time in seconds: 12.62262808899959