# Start time: 2024-03-30 00:01:37.093481
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return second input, followed by a space, and then the first input, and given input as ['Launa', 'Withers'] output is Withers Launa, given input as ['Lakenya', 'Edison'] output is Edison Lakenya, given input as ['Brendan', 'Hage'] output is Hage Brendan, given input as ['Bradford', 'Lango'] output is Lango Bradford, given input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, given input as ['Lara', 'Constable'] output is Constable Lara, given input as ['Madelaine', 'Ghoston'] output is Ghoston Madelaine, given input as ['Salley', 'Hornak'] output is Hornak Salley, given input as ['Micha', 'Junkin'] output is Junkin Micha, given input as ['Teddy', 'Bobo'] output is Bobo Teddy, given input as ['Coralee', 'Scalia'] output is Scalia Coralee, given input as ['Jeff', 'Quashie'] output is Quashie Jeff, given input as ['Vena', 'Babiarz'] output is Babiarz Vena, given input as ['Karrie', 'Lain'] output is Lain Karrie, given input as ['Tobias', 'Dermody'] output is Dermody Tobias, given input as ['Celsa', 'Hopkins'] output is Hopkins Celsa, given input as ['Kimberley', 'Halpern'] output is Halpern Kimberley, given input as ['Phillip', 'Rowden'] output is Rowden Phillip, given input as ['Elias', 'Neil'] output is Neil Elias, given input as ['Lashanda', 'Cortes'] output is Cortes Lashanda, given input as ['Mackenzie', 'Spell'] output is Spell Mackenzie, given input as ['Kathlyn', 'Eccleston'] output is Eccleston Kathlyn, given input as ['Georgina', 'Brescia'] output is Brescia Georgina, given input as ['Beata', 'Miah'] output is Miah Beata, given input as ['Desiree', 'Seamons'] output is Seamons Desiree, given input as ['Jeanice', 'Soderstrom'] output is Soderstrom Jeanice, given input as ['Mariel', 'Jurgens'] output is Jurgens Mariel, given input as ['Alida', 'Bogle'] output is Bogle Alida, given input as ['Jacqualine', 'Olague'] output is Olague Jacqualine, given input as ['Joaquin', 'Clasen'] output is Clasen Joaquin, given input as ['Samuel', 'Richert'] output is Richert Samuel, given input as ['Malissa', 'Marcus'] output is Marcus Malissa, given input as ['Alaina', 'Partida'] output is Partida Alaina, given input as ['Trinidad', 'Mulloy'] output is Mulloy Trinidad, given input as ['Carlene', 'Garrard'] output is Garrard Carlene, given input as ['Melodi', 'Chism'] output is Chism Melodi, given input as ['Bess', 'Chilcott'] output is Chilcott Bess, given input as ['Chong', 'Aylward'] output is Aylward Chong, given input as ['Jani', 'Ramthun'] output is Ramthun Jani, given input as ['Jacquiline', 'Heintz'] output is Heintz Jacquiline, given input as ['Hayley', 'Marquess'] output is Marquess Hayley, given input as ['Andria', 'Spagnoli'] output is Spagnoli Andria, given input as ['Irwin', 'Covelli'] output is Covelli Irwin, given input as ['Gertude', 'Montiel'] output is Montiel Gertude, given input as ['Stefany', 'Reily'] output is Reily Stefany, given input as ['Rae', 'Mcgaughey'] output is Mcgaughey Rae, given input as ['Cruz', 'Latimore'] output is Latimore Cruz, given input as ['Maryann', 'Casler'] output is Casler Maryann, given input as ['Annalisa', 'Gregori'] output is Gregori Annalisa, given input as ['Jenee', 'Pannell'] output is Pannell Jenee, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def reverse_names(input_str):
    try:
        input_list = input_str.split(',')
        first_name = input_list[0].strip()
        last_name = input_list[1].strip()
        return f"{last_name} {first_name}"
    except IndexError:
        return "Invalid input format. Please provide two names separated by a comma."

# Input: "Launa, Withers"
# Output: "Withers Launa"
# Prompt: return second input, followed by a space, and then the first input

# Test cases
print(reverse_names("Launa, Withers"))
print(reverse_names("Lakenya, Edison"))
print(reverse_names("Brendan, Hage"))
print(reverse_names("Bradford, Lango"))
print(reverse_names("Rudolf, Akiyama"))
print(reverse_names("Lara, Constable"))
print(reverse_names("Madelaine, Ghoston"))
print(reverse_names("Salley, Hornak"))
print(reverse_names("Micha, Junkin"))
print(reverse_names("Teddy, Bobo"))
print(reverse_names("Coralee, Scalia"))
print(reverse_names("Jeff, Quashie"))
print(reverse_names("Vena, Babiarz"))
print(reverse_names("Karrie, Lain"))
print(reverse_names("Tobias, Dermody"))
print(reverse_names("Celsa, Hopkins"))
print(reverse_names("Kimberley, Halpern"))
print(reverse_names("Phillip, Rowden"))
print(reverse_names("Elias, Neil"))
print(reverse_names("Lashanda, Cortes"))
print(reverse_names("Mackenzie, Spell"))
print(reverse_names("Kathlyn, Eccleston"))
print(reverse_names("Georgina, Brescia"))
print(reverse_names("Beata, Miah"))
print(reverse_names("Desiree, Seamons"))
print(reverse_names("Jeanice, Soderstrom"))
print(reverse_names("Mariel, Jurgens"))
print(reverse_names("Alida, Bogle"))
print(reverse_names("Jacqualine, Olague"))
print(reverse_names("Joaquin, Clasen"))
print(reverse_names("Samuel, Richert"))
print(reverse_names("Malissa, Marcus"))
print(reverse_names("Alaina, Partida"))
print(reverse_names("Trinidad, Mulloy"))
print(reverse_names("Carlene, Garrard"))
print(reverse_names("Melodi, Chism"))
print(reverse_names("Bess, Chilcott"))
print(reverse_names("Chong, Aylward"))
print(reverse_names("Jani, Ramthun"))
print(reverse_names("Jacquiline, Heintz"))
print(reverse_names("Hayley, Marquess"))
print(reverse_names("Andria, Spagnoli"))
print(reverse_names("Irwin, Covelli"))
print(reverse_names("Gertude, Montiel"))
print(reverse_names("Stefany, Reily"))
print(reverse_names("Rae, Mcgaughey"))
print(reverse_names("Cruz, Latimore"))
print(reverse_names("Maryann, Casler"))
print(reverse_names("Annalisa, Gregori"))
print(reverse_names("Jenee, Pannell"))

# End time: 2024-03-30 00:01:52.375421
# Elapsed time in seconds: 15.281492545999981