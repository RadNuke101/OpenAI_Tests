# Start time: 2024-04-09 20:37:29.379934

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of strings that follow a specific pattern: a plus sign (+) followed by a country code (one or more digits), a space, and then a sequence of three groups of digits separated by hyphens. The first group after the country code consists of three digits, the second and third groups vary in length but are also purely numerical. This pattern is consistent across all entries, suggesting that the data represents phone numbers with an international format. The country code and the specific format imply that these numbers could be from various countries, indicating a diverse dataset in terms of geographical representation.

### Output Column Summary:

The output data consistently extracts the first group of three digits that immediately follow the country code from the input data. This group of digits appears to be the focus of the extraction process, ignoring the country code, and the subsequent groups of numbers. The output is always a three-digit number, which suggests that the relationship between the input and output is a targeted extraction of a specific part of the input string, likely representing an area or city code within the broader phone number format.

### Relationship Summary:

The relationship between the input and output data is a structured extraction process where the output is derived by isolating the first group of three digits that follow the country code in the input phone number. This process ignores the country code and the rest of the phone number, focusing solely on this specific segment. The consistency in this extraction across the dataset indicates a systematic approach to identifying a particular component of the phone numbers, possibly for analysis or categorization purposes based on area or city codes. This method suggests an interest in the geographical or regional segmentation of the dataset, rather than the individual phone numbers or the country codes., and input as ['+106 769-858-438'] output is 769, input as ['+106 769-858-438'] output is 769, input as ['+106 769-858-438'] output is 769, input as ['+83 973-757-831'] output is 973, input as ['+83 973-757-831'] output is 973, input as ['+83 973-757-831'] output is 973, input as ['+62 647-787-775'] output is 647, input as ['+62 647-787-775'] output is 647, input as ['+62 647-787-775'] output is 647, input as ['+172 027-507-632'] output is 027, input as ['+172 027-507-632'] output is 027, input as ['+172 027-507-632'] output is 027, input as ['+72 001-050-856'] output is 001, input as ['+72 001-050-856'] output is 001, input as ['+72 001-050-856'] output is 001, input as ['+95 310-537-401'] output is 310, input as ['+95 310-537-401'] output is 310, input as ['+95 310-537-401'] output is 310, input as ['+6 775-969-238'] output is 775, input as ['+6 775-969-238'] output is 775, input as ['+6 775-969-238'] output is 775, input as ['+174 594-539-946'] output is 594, input as ['+174 594-539-946'] output is 594, input as ['+174 594-539-946'] output is 594, input as ['+155 927-275-860'] output is 927, input as ['+155 927-275-860'] output is 927, input as ['+155 927-275-860'] output is 927, input as ['+167 405-461-331'] output is 405, input as ['+167 405-461-331'] output is 405, input as ['+167 405-461-331'] output is 405, input as ['+10 538-347-401'] output is 538, input as ['+10 538-347-401'] output is 538, input as ['+10 538-347-401'] output is 538, input as ['+60 971-986-103'] output is 971, input as ['+60 971-986-103'] output is 971, input as ['+60 971-986-103'] output is 971, input as ['+13 258-276-941'] output is 258, input as ['+13 258-276-941'] output is 258, input as ['+13 258-276-941'] output is 258, input as ['+2 604-746-137'] output is 604, input as ['+2 604-746-137'] output is 604, input as ['+2 604-746-137'] output is 604, input as ['+25 998-898-180'] output is 998, input as ['+25 998-898-180'] output is 998, input as ['+25 998-898-180'] output is 998, input as ['+151 862-946-541'] output is 862, input as ['+151 862-946-541'] output is 862, input as ['+151 862-946-541'] output is 862, input as ['+118 165-041-038'] output is 165, input as ['+118 165-041-038'] output is 165, input as ['+118 165-041-038'] output is 165, input as ['+144 170-592-272'] output is 170, input as ['+144 170-592-272'] output is 170, input as ['+144 170-592-272'] output is 170, input as ['+94 462-008-482'] output is 462, input as ['+94 462-008-482'] output is 462, input as ['+94 462-008-482'] output is 462, input as ['+82 685-122-086'] output is 685, input as ['+82 685-122-086'] output is 685, input as ['+82 685-122-086'] output is 685, input as ['+82 675-366-472'] output is 675, input as ['+82 675-366-472'] output is 675, input as ['+82 675-366-472'] output is 675, input as ['+80 066-433-096'] output is 066, input as ['+80 066-433-096'] output is 066, input as ['+80 066-433-096'] output is 066, input as ['+163 039-436-166'] output is 039, input as ['+163 039-436-166'] output is 039, input as ['+163 039-436-166'] output is 039, input as ['+138 808-083-074'] output is 808, input as ['+138 808-083-074'] output is 808, input as ['+138 808-083-074'] output is 808, input as ['+42 643-245-738'] output is 643, input as ['+42 643-245-738'] output is 643, input as ['+42 643-245-738'] output is 643, input as ['+169 822-542-726'] output is 822, input as ['+169 822-542-726'] output is 822, input as ['+169 822-542-726'] output is 822, input as ['+176 767-782-369'] output is 767, input as ['+176 767-782-369'] output is 767, input as ['+176 767-782-369'] output is 767, input as ['+47 414-369-343'] output is 414, input as ['+47 414-369-343'] output is 414, input as ['+47 414-369-343'] output is 414, input as ['+138 885-618-512'] output is 885, input as ['+138 885-618-512'] output is 885, input as ['+138 885-618-512'] output is 885, input as ['+104 158-671-355'] output is 158, input as ['+104 158-671-355'] output is 158, input as ['+104 158-671-355'] output is 158, input as ['+188 280-087-526'] output is 280, input as ['+188 280-087-526'] output is 280, input as ['+188 280-087-526'] output is 280, input as ['+50 268-571-336'] output is 268, input as ['+50 268-571-336'] output is 268, input as ['+50 268-571-336'] output is 268, input as ['+183 225-960-024'] output is 225, input as ['+183 225-960-024'] output is 225, input as ['+183 225-960-024'] output is 225, input as ['+58 191-982-491'] output is 191, input as ['+58 191-982-491'] output is 191, input as ['+58 191-982-491'] output is 191, input as ['+9 507-092-535'] output is 507, input as ['+9 507-092-535'] output is 507, input as ['+9 507-092-535'] output is 507, input as ['+64 061-601-398'] output is 061, input as ['+64 061-601-398'] output is 061, input as ['+64 061-601-398'] output is 061, input as ['+189 831-591-877'] output is 831, input as ['+189 831-591-877'] output is 831, input as ['+189 831-591-877'] output is 831, input as ['+129 425-765-844'] output is 425, input as ['+129 425-765-844'] output is 425, input as ['+129 425-765-844'] output is 425, input as ['+94 856-734-046'] output is 856, input as ['+94 856-734-046'] output is 856, input as ['+94 856-734-046'] output is 856, input as ['+35 082-845-261'] output is 082, input as ['+35 082-845-261'] output is 082, input as ['+35 082-845-261'] output is 082, input as ['+185 394-622-272'] output is 394, input as ['+185 394-622-272'] output is 394, input as ['+185 394-622-272'] output is 394, input as ['+163 905-707-740'] output is 905, input as ['+163 905-707-740'] output is 905, input as ['+163 905-707-740'] output is 905, input as ['+23 448-213-807'] output is 448, input as ['+23 448-213-807'] output is 448, input as ['+23 448-213-807'] output is 448, input as ['+42 634-077-089'] output is 634, input as ['+42 634-077-089'] output is 634, input as ['+42 634-077-089'] output is 634, input as ['+18 051-287-382'] output is 051, input as ['+18 051-287-382'] output is 051, input as ['+18 051-287-382'] output is 051, input as ['+29 773-545-520'] output is 773, input as ['+29 773-545-520'] output is 773, input as ['+29 773-545-520'] output is 773, input as ['+43 249-097-743'] output is 249, input as ['+43 249-097-743'] output is 249, input as ['+43 249-097-743'] output is 249, input as ['+158 674-736-891'] output is 674, input as ['+158 674-736-891'] output is 674, input as ['+158 674-736-891'] output is 674, input as ['+45 124-771-454'] output is 124, input as ['+45 124-771-454'] output is 124, input as ['+45 124-771-454'] output is 124, input as ['+180 029-457-654'] output is 029, input as ['+180 029-457-654'] output is 029, input as ['+180 029-457-654'] output is 029, input as ['+75 227-250-652'] output is 227, input as ['+75 227-250-652'] output is 227, input as ['+75 227-250-652'] output is 227, input as ['+5 528-317-854'] output is 528, input as ['+5 528-317-854'] output is 528, input as ['+5 528-317-854'] output is 528, input as ['+81 849-629-290'] output is 849, input as ['+81 849-629-290'] output is 849, input as ['+81 849-629-290'] output is 849, input as ['+46 005-119-176'] output is 005, input as ['+46 005-119-176'] output is 005, input as ['+46 005-119-176'] output is 005, input as ['+108 150-380-705'] output is 150, input as ['+108 150-380-705'] output is 150, input as ['+108 150-380-705'] output is 150, input as ['+40 122-224-247'] output is 122, input as ['+40 122-224-247'] output is 122, input as ['+40 122-224-247'] output is 122, input as ['+68 890-680-027'] output is 890, input as ['+68 890-680-027'] output is 890, input as ['+68 890-680-027'] output is 890, input as ['+169 060-204-504'] output is 060, input as ['+169 060-204-504'] output is 060, input as ['+169 060-204-504'] output is 060, input as ['+95 620-820-945'] output is 620, input as ['+95 620-820-945'] output is 620, input as ['+95 620-820-945'] output is 620, input as ['+43 592-938-846'] output is 592, input as ['+43 592-938-846'] output is 592, input as ['+43 592-938-846'] output is 592, input as ['+7 023-296-647'] output is 023, input as ['+7 023-296-647'] output is 023, input as ['+7 023-296-647'] output is 023, input as ['+20 541-401-396'] output is 541, input as ['+20 541-401-396'] output is 541, input as ['+20 541-401-396'] output is 541, input as ['+64 751-365-934'] output is 751, input as ['+64 751-365-934'] output is 751, input as ['+64 751-365-934'] output is 751, input as ['+163 546-119-476'] output is 546, input as ['+163 546-119-476'] output is 546, input as ['+163 546-119-476'] output is 546, input as ['+198 557-666-779'] output is 557, input as ['+198 557-666-779'] output is 557, input as ['+198 557-666-779'] output is 557, input as ['+14 673-759-017'] output is 673, input as ['+14 673-759-017'] output is 673, input as ['+14 673-759-017'] output is 673, input as ['+161 086-020-168'] output is 086, input as ['+161 086-020-168'] output is 086, input as ['+161 086-020-168'] output is 086, input as ['+65 970-575-488'] output is 970, input as ['+65 970-575-488'] output is 970, input as ['+65 970-575-488'] output is 970, input as ['+2 455-126-377'] output is 455, input as ['+2 455-126-377'] output is 455, input as ['+2 455-126-377'] output is 455, input as ['+196 728-585-376'] output is 728, input as ['+196 728-585-376'] output is 728, input as ['+196 728-585-376'] output is 728, input as ['+33 117-430-125'] output is 117, input as ['+33 117-430-125'] output is 117, input as ['+33 117-430-125'] output is 117, input as ['+195 488-831-768'] output is 488, input as ['+195 488-831-768'] output is 488, input as ['+195 488-831-768'] output is 488, input as ['+86 468-718-108'] output is 468, input as ['+86 468-718-108'] output is 468, input as ['+86 468-718-108'] output is 468, input as ['+194 278-716-950'] output is 278, input as ['+194 278-716-950'] output is 278, input as ['+194 278-716-950'] output is 278, input as ['+43 730-685-847'] output is 730, input as ['+43 730-685-847'] output is 730, input as ['+43 730-685-847'] output is 730, input as ['+140 794-289-551'] output is 794, input as ['+140 794-289-551'] output is 794, input as ['+140 794-289-551'] output is 794, input as ['+21 679-740-834'] output is 679, input as ['+21 679-740-834'] output is 679, input as ['+21 679-740-834'] output is 679, input as ['+98 717-997-323'] output is 717, input as ['+98 717-997-323'] output is 717, input as ['+98 717-997-323'] output is 717, input as ['+47 401-100-231'] output is 401, input as ['+47 401-100-231'] output is 401, input as ['+47 401-100-231'] output is 401, input as ['+143 726-462-368'] output is 726, input as ['+143 726-462-368'] output is 726, input as ['+143 726-462-368'] output is 726, input as ['+147 864-005-968'] output is 864, input as ['+147 864-005-968'] output is 864, input as ['+147 864-005-968'] output is 864, input as ['+130 590-757-665'] output is 590, input as ['+130 590-757-665'] output is 590, input as ['+130 590-757-665'] output is 590, input as ['+197 700-858-976'] output is 700, input as ['+197 700-858-976'] output is 700, input as ['+197 700-858-976'] output is 700, input as ['+158 344-541-946'] output is 344, input as ['+158 344-541-946'] output is 344, input as ['+158 344-541-946'] output is 344, input as ['+56 242-901-234'] output is 242, input as ['+56 242-901-234'] output is 242, input as ['+56 242-901-234'] output is 242, input as ['+132 313-075-754'] output is 313, input as ['+132 313-075-754'] output is 313, input as ['+132 313-075-754'] output is 313, input as ['+130 517-953-149'] output is 517, input as ['+130 517-953-149'] output is 517, input as ['+130 517-953-149'] output is 517, input as ['+158 684-878-743'] output is 684, input as ['+158 684-878-743'] output is 684, input as ['+158 684-878-743'] output is 684, input as ['+52 836-582-035'] output is 836, input as ['+52 836-582-035'] output is 836, input as ['+52 836-582-035'] output is 836, input as ['+138 117-484-671'] output is 117, input as ['+138 117-484-671'] output is 117, input as ['+138 117-484-671'] output is 117, input as ['+50 012-148-873'] output is 012, input as ['+50 012-148-873'] output is 012, input as ['+50 012-148-873'] output is 012, input as ['+105 048-919-483'] output is 048, input as ['+105 048-919-483'] output is 048, input as ['+105 048-919-483'] output is 048, input as ['+18 209-851-997'] output is 209, input as ['+18 209-851-997'] output is 209, input as ['+18 209-851-997'] output is 209, input as ['+176 938-056-084'] output is 938, input as ['+176 938-056-084'] output is 938, input as ['+176 938-056-084'] output is 938, input as ['+141 018-132-973'] output is 018, input as ['+141 018-132-973'] output is 018, input as ['+141 018-132-973'] output is 018, input as ['+199 936-162-415'] output is 936, input as ['+199 936-162-415'] output is 936, input as ['+199 936-162-415'] output is 936, input as ['+33 547-051-264'] output is 547, input as ['+33 547-051-264'] output is 547, input as ['+33 547-051-264'] output is 547, input as ['+161 233-981-513'] output is 233, input as ['+161 233-981-513'] output is 233, input as ['+161 233-981-513'] output is 233, input as ['+115 101-728-328'] output is 101, input as ['+115 101-728-328'] output is 101, input as ['+115 101-728-328'] output is 101, input as ['+45 095-746-635'] output is 095, input as ['+45 095-746-635'] output is 095, input as ['+45 095-746-635'] output is 095, input as ['+106 769-858-438'] output is 769, input as ['+83 973-757-831'] output is 973, input as ['+62 647-787-775'] output is 647, input as ['+172 027-507-632'] output is 027, input as ['+72 001-050-856'] output is 001, input as ['+95 310-537-401'] output is 310, input as ['+6 775-969-238'] output is 775, input as ['+174 594-539-946'] output is 594, input as ['+155 927-275-860'] output is 927, input as ['+167 405-461-331'] output is 405, input as ['+10 538-347-401'] output is 538, input as ['+60 971-986-103'] output is 971, input as ['+13 258-276-941'] output is 258, input as ['+2 604-746-137'] output is 604, input as ['+25 998-898-180'] output is 998, input as ['+151 862-946-541'] output is 862, input as ['+118 165-041-038'] output is 165, input as ['+144 170-592-272'] output is 170, input as ['+94 462-008-482'] output is 462, input as ['+82 685-122-086'] output is 685, input as ['+82 675-366-472'] output is 675, input as ['+80 066-433-096'] output is 066, input as ['+163 039-436-166'] output is 039, input as ['+138 808-083-074'] output is 808, input as ['+42 643-245-738'] output is 643, input as ['+169 822-542-726'] output is 822, input as ['+176 767-782-369'] output is 767, input as ['+47 414-369-343'] output is 414, input as ['+138 885-618-512'] output is 885, input as ['+104 158-671-355'] output is 158, input as ['+188 280-087-526'] output is 280, input as ['+50 268-571-336'] output is 268, input as ['+183 225-960-024'] output is 225, input as ['+58 191-982-491'] output is 191, input as ['+9 507-092-535'] output is 507, input as ['+64 061-601-398'] output is 061, input as ['+189 831-591-877'] output is 831, input as ['+129 425-765-844'] output is 425, input as ['+94 856-734-046'] output is 856, input as ['+35 082-845-261'] output is 082, input as ['+185 394-622-272'] output is 394, input as ['+163 905-707-740'] output is 905, input as ['+23 448-213-807'] output is 448, input as ['+42 634-077-089'] output is 634, input as ['+18 051-287-382'] output is 051, input as ['+29 773-545-520'] output is 773, input as ['+43 249-097-743'] output is 249, input as ['+158 674-736-891'] output is 674, input as ['+45 124-771-454'] output is 124, input as ['+180 029-457-654'] output is 029, input as ['+75 227-250-652'] output is 227, input as ['+5 528-317-854'] output is 528, input as ['+81 849-629-290'] output is 849, input as ['+46 005-119-176'] output is 005, input as ['+108 150-380-705'] output is 150, input as ['+40 122-224-247'] output is 122, input as ['+68 890-680-027'] output is 890, input as ['+169 060-204-504'] output is 060, input as ['+95 620-820-945'] output is 620, input as ['+43 592-938-846'] output is 592, input as ['+7 023-296-647'] output is 023, input as ['+20 541-401-396'] output is 541, input as ['+64 751-365-934'] output is 751, input as ['+163 546-119-476'] output is 546, input as ['+198 557-666-779'] output is 557, input as ['+14 673-759-017'] output is 673, input as ['+161 086-020-168'] output is 086, input as ['+65 970-575-488'] output is 970, input as ['+2 455-126-377'] output is 455, input as ['+196 728-585-376'] output is 728, input as ['+33 117-430-125'] output is 117, input as ['+195 488-831-768'] output is 488, input as ['+86 468-718-108'] output is 468, input as ['+194 278-716-950'] output is 278, input as ['+43 730-685-847'] output is 730, input as ['+140 794-289-551'] output is 794, input as ['+21 679-740-834'] output is 679, input as ['+98 717-997-323'] output is 717, input as ['+47 401-100-231'] output is 401, input as ['+143 726-462-368'] output is 726, input as ['+147 864-005-968'] output is 864, input as ['+130 590-757-665'] output is 590, input as ['+197 700-858-976'] output is 700, input as ['+158 344-541-946'] output is 344, input as ['+56 242-901-234'] output is 242, input as ['+132 313-075-754'] output is 313, input as ['+130 517-953-149'] output is 517, input as ['+158 684-878-743'] output is 684, input as ['+52 836-582-035'] output is 836, input as ['+138 117-484-671'] output is 117, input as ['+50 012-148-873'] output is 012, input as ['+105 048-919-483'] output is 048, input as ['+18 209-851-997'] output is 209, input as ['+176 938-056-084'] output is 938, input as ['+141 018-132-973'] output is 018, input as ['+199 936-162-415'] output is 936, input as ['+33 547-051-264'] output is 547, input as ['+161 233-981-513'] output is 233, input as ['+115 101-728-328'] output is 101, input as ['+45 095-746-635'] output is 095, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Extracting the first group of three digits after the country code
    # Assuming the input phone_number follows the described pattern
    parts = phone_number.split(' ')
    if len(parts) > 1:
        number_parts = parts[1].split('-')
        if len(number_parts) > 0:
            return number_parts[0]  # Return the first group of three digits
    return ""  # Return an empty string if the pattern does not match

# Test cases based on the provided inputs
print(generated_function('+106 769-858-438'))  # Expected output: 769
print(generated_function('+83 973-757-831'))  # Expected output: 973
print(generated_function('+62 647-787-775'))  # Expected output: 647
print(generated_function('+172 027-507-632'))  # Expected output: 027
print(generated_function('+72 001-050-856'))  # Expected output: 001
print(generated_function('+95 310-537-401'))  # Expected output: 310
print(generated_function('+6 775-969-238'))  # Expected output: 775
print(generated_function('+174 594-539-946'))  # Expected output: 594
print(generated_function('+155 927-275-860'))  # Expected output: 927
print(generated_function('+167 405-461-331'))  # Expected output: 405
print(generated_function('+10 538-347-401'))  # Expected output: 538
print(generated_function('+60 971-986-103'))  # Expected output: 971
print(generated_function('+13 258-276-941'))  # Expected output: 258
print(generated_function('+2 604-746-137'))  # Expected output: 604
print(generated_function('+25 998-898-180'))  # Expected output: 998
print(generated_function('+151 862-946-541'))  # Expected output: 862
print(generated_function('+118 165-041-038'))  # Expected output: 165
print(generated_function('+144 170-592-272'))  # Expected output: 170
print(generated_function('+94 462-008-482'))  # Expected output: 462
print(generated_function('+82 685-122-086'))  # Expected output: 685
print(generated_function('+82 675-366-472'))  # Expected output: 675
print(generated_function('+80 066-433-096'))  # Expected output: 066
print(generated_function('+163 039-436-166'))  # Expected output: 039
print(generated_function('+138 808-083-074'))  # Expected output: 808
print(generated_function('+42 643-245-738'))  # Expected output: 643
print(generated_function('+169 822-542-726'))  # Expected output: 822
print(generated_function('+176 767-782-369'))  # Expected output: 767
print(generated_function('+47 414-369-343'))  # Expected output: 414
print(generated_function('+138 885-618-512'))  # Expected output: 885
print(generated_function('+104 158-671-355'))  # Expected output: 158
print(generated_function('+188 280-087-526'))  # Expected output: 280
print(generated_function('+50 268-571-336'))  # Expected output: 268
print(generated_function('+183 225-960-024'))  # Expected output: 225
print(generated_function('+58 191-982-491'))  # Expected output: 191
print(generated_function('+9 507-092-535'))  # Expected output: 507
print(generated_function('+64 061-601-398'))  # Expected output: 061
print(generated_function('+189 831-591-877'))  # Expected output: 831
print(generated_function('+129 425-765-844'))  # Expected output: 425
print(generated_function('+94 856-734-046'))  # Expected output: 856
print(generated_function('+35 082-845-261'))  # Expected output: 082
print(generated_function('+185 394-622-272'))  # Expected output: 394
print(generated_function('+163 905-707-740'))  # Expected output: 905
print(generated_function('+23 448-213-807'))  # Expected output: 448
print(generated_function('+42 634-077-089'))  # Expected output: 634
print(generated_function('+18 051-287-382'))  # Expected output: 051
print(generated_function('+29 773-545-520'))  # Expected output: 773
print(generated_function('+43 249-097-743'))  # Expected output: 249
print(generated_function('+158 674-736-891'))  # Expected output: 674
print(generated_function('+45 124-771-454'))  # Expected output: 124
print(generated_function('+180 029-457-654'))  # Expected output: 029
print(generated_function('+75 227-250-652'))  # Expected output: 227
print(generated_function('+5 528-317-854'))  # Expected output: 528
print(generated_function('+81 849-629-290'))  # Expected output: 849
print(generated_function('+46 005-119-176'))  # Expected output: 005
print(generated_function('+108 150-380-705'))  # Expected output: 150
print(generated_function('+40 122-224-247'))  # Expected output: 122
print(generated_function('+68 890-680-027'))  # Expected output: 890
print(generated_function('+169 060-204-504'))  # Expected output: 060
print(generated_function('+95 620-820-945'))  # Expected output: 620
print(generated_function('+43 592-938-846'))  # Expected output: 592
print(generated_function('+7 023-296-647'))  # Expected output: 023
print(generated_function('+20 541-401-396'))  # Expected output: 541
print(generated_function('+64 751-365-934'))  # Expected output: 751
print(generated_function('+163 546-119-476'))  # Expected output: 546
print(generated_function('+198 557-666-779'))  # Expected output: 557
print(generated_function('+14 673-759-017'))  # Expected output: 673
print(generated_function('+161 086-020-168'))  # Expected output: 086
print(generated_function('+65 970-575-488'))  # Expected output: 970
print(generated_function('+2 455-126-377'))  # Expected output: 455
print(generated_function('+196 728-585-376'))  # Expected output: 728
print(generated_function('+33 117-430-125'))  # Expected output: 117
print(generated_function('+195 488-831-768'))  # Expected output: 488
print(generated_function('+86 468-718-108'))  # Expected output: 468
print(generated_function('+194 278-716-950'))  # Expected output: 278
print(generated_function('+43 730-685-847'))  # Expected output: 730
print(generated_function('+140 794-289-551'))  # Expected output: 794
print(generated_function('+21 679-740-834'))  # Expected output: 679
print(generated_function('+98 717-997-323'))  # Expected output: 717
print(generated_function('+47 401-100-231'))  # Expected output: 401
print(generated_function('+143 726-462-368'))  # Expected output: 726
print(generated_function('+147 864-005-968'))  # Expected output: 864
print(generated_function('+130 590-757-665'))  # Expected output: 590
print(generated_function('+197 700-858-976'))  # Expected output: 700
print(generated_function('+158 344-541-946'))  # Expected output: 344
print(generated_function('+56 242-901-234'))  # Expected output: 242
print(generated_function('+132 313-075-754'))  # Expected output: 313
print(generated_function('+130 517-953-149'))  # Expected output: 517
print(generated_function('+158 684-878-743'))  # Expected output: 684
print(generated_function('+52 836-582-035'))  # Expected output: 836
print(generated_function('+138 117-484-671'))  # Expected output: 117
print(generated_function('+50 012-148-873'))  # Expected output: 012
print(generated_function('+105 048-919-483'))  # Expected output: 048
print(generated_function('+18 209-851-997'))  # Expected output: 209
print(generated_function('+176 938-056-084'))  # Expected output: 938
print(generated_function('+141 018-132-973'))  # Expected output: 018
print(generated_function('+199 936-162-415'))  # Expected output: 936
print(generated_function('+33 547-051-264'))  # Expected output: 547
print(generated_function('+161 233-981-513'))  # Expected output: 233
print(generated_function('+115 101-728-328'))  # Expected output: 101
print(generated_function('+45 095-746-635'))  # Expected output: 095
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775
print(generated_function("+6 775-969-238"))  ## Output: 775
print(generated_function("+6 775-969-238"))  ## Output: 775
print(generated_function("+174 594-539-946"))  ## Output: 594
print(generated_function("+174 594-539-946"))  ## Output: 594
print(generated_function("+174 594-539-946"))  ## Output: 594
print(generated_function("+155 927-275-860"))  ## Output: 927
print(generated_function("+155 927-275-860"))  ## Output: 927
print(generated_function("+155 927-275-860"))  ## Output: 927
print(generated_function("+167 405-461-331"))  ## Output: 405
print(generated_function("+167 405-461-331"))  ## Output: 405
print(generated_function("+167 405-461-331"))  ## Output: 405
print(generated_function("+10 538-347-401"))  ## Output: 538
print(generated_function("+10 538-347-401"))  ## Output: 538
print(generated_function("+10 538-347-401"))  ## Output: 538
print(generated_function("+60 971-986-103"))  ## Output: 971
print(generated_function("+60 971-986-103"))  ## Output: 971
print(generated_function("+60 971-986-103"))  ## Output: 971
print(generated_function("+13 258-276-941"))  ## Output: 258
print(generated_function("+13 258-276-941"))  ## Output: 258
print(generated_function("+13 258-276-941"))  ## Output: 258
print(generated_function("+2 604-746-137"))  ## Output: 604
print(generated_function("+2 604-746-137"))  ## Output: 604
print(generated_function("+2 604-746-137"))  ## Output: 604
print(generated_function("+25 998-898-180"))  ## Output: 998
print(generated_function("+25 998-898-180"))  ## Output: 998
print(generated_function("+25 998-898-180"))  ## Output: 998
print(generated_function("+151 862-946-541"))  ## Output: 862
print(generated_function("+151 862-946-541"))  ## Output: 862
print(generated_function("+151 862-946-541"))  ## Output: 862
print(generated_function("+118 165-041-038"))  ## Output: 165
print(generated_function("+118 165-041-038"))  ## Output: 165
print(generated_function("+118 165-041-038"))  ## Output: 165
print(generated_function("+144 170-592-272"))  ## Output: 170
print(generated_function("+144 170-592-272"))  ## Output: 170
print(generated_function("+144 170-592-272"))  ## Output: 170
print(generated_function("+94 462-008-482"))  ## Output: 462
print(generated_function("+94 462-008-482"))  ## Output: 462
print(generated_function("+94 462-008-482"))  ## Output: 462
print(generated_function("+82 685-122-086"))  ## Output: 685
print(generated_function("+82 685-122-086"))  ## Output: 685
print(generated_function("+82 685-122-086"))  ## Output: 685
print(generated_function("+82 675-366-472"))  ## Output: 675
print(generated_function("+82 675-366-472"))  ## Output: 675
print(generated_function("+82 675-366-472"))  ## Output: 675
print(generated_function("+80 066-433-096"))  ## Output: 066
print(generated_function("+80 066-433-096"))  ## Output: 066
print(generated_function("+80 066-433-096"))  ## Output: 066
print(generated_function("+163 039-436-166"))  ## Output: 039
print(generated_function("+163 039-436-166"))  ## Output: 039
print(generated_function("+163 039-436-166"))  ## Output: 039
print(generated_function("+138 808-083-074"))  ## Output: 808
print(generated_function("+138 808-083-074"))  ## Output: 808
print(generated_function("+138 808-083-074"))  ## Output: 808
print(generated_function("+42 643-245-738"))  ## Output: 643
print(generated_function("+42 643-245-738"))  ## Output: 643
print(generated_function("+42 643-245-738"))  ## Output: 643
print(generated_function("+169 822-542-726"))  ## Output: 822
print(generated_function("+169 822-542-726"))  ## Output: 822
print(generated_function("+169 822-542-726"))  ## Output: 822
print(generated_function("+176 767-782-369"))  ## Output: 767
print(generated_function("+176 767-782-369"))  ## Output: 767
print(generated_function("+176 767-782-369"))  ## Output: 767
print(generated_function("+47 414-369-343"))  ## Output: 414
print(generated_function("+47 414-369-343"))  ## Output: 414
print(generated_function("+47 414-369-343"))  ## Output: 414
print(generated_function("+138 885-618-512"))  ## Output: 885
print(generated_function("+138 885-618-512"))  ## Output: 885
print(generated_function("+138 885-618-512"))  ## Output: 885
print(generated_function("+104 158-671-355"))  ## Output: 158
print(generated_function("+104 158-671-355"))  ## Output: 158
print(generated_function("+104 158-671-355"))  ## Output: 158
print(generated_function("+188 280-087-526"))  ## Output: 280
print(generated_function("+188 280-087-526"))  ## Output: 280
print(generated_function("+188 280-087-526"))  ## Output: 280
print(generated_function("+50 268-571-336"))  ## Output: 268
print(generated_function("+50 268-571-336"))  ## Output: 268
print(generated_function("+50 268-571-336"))  ## Output: 268
print(generated_function("+183 225-960-024"))  ## Output: 225
print(generated_function("+183 225-960-024"))  ## Output: 225
print(generated_function("+183 225-960-024"))  ## Output: 225
print(generated_function("+58 191-982-491"))  ## Output: 191
print(generated_function("+58 191-982-491"))  ## Output: 191
print(generated_function("+58 191-982-491"))  ## Output: 191
print(generated_function("+9 507-092-535"))  ## Output: 507
print(generated_function("+9 507-092-535"))  ## Output: 507
print(generated_function("+9 507-092-535"))  ## Output: 507
print(generated_function("+64 061-601-398"))  ## Output: 061
print(generated_function("+64 061-601-398"))  ## Output: 061
print(generated_function("+64 061-601-398"))  ## Output: 061
print(generated_function("+189 831-591-877"))  ## Output: 831
print(generated_function("+189 831-591-877"))  ## Output: 831
print(generated_function("+189 831-591-877"))  ## Output: 831
print(generated_function("+129 425-765-844"))  ## Output: 425
print(generated_function("+129 425-765-844"))  ## Output: 425
print(generated_function("+129 425-765-844"))  ## Output: 425
print(generated_function("+94 856-734-046"))  ## Output: 856
print(generated_function("+94 856-734-046"))  ## Output: 856
print(generated_function("+94 856-734-046"))  ## Output: 856
print(generated_function("+35 082-845-261"))  ## Output: 082
print(generated_function("+35 082-845-261"))  ## Output: 082
print(generated_function("+35 082-845-261"))  ## Output: 082
print(generated_function("+185 394-622-272"))  ## Output: 394
print(generated_function("+185 394-622-272"))  ## Output: 394
print(generated_function("+185 394-622-272"))  ## Output: 394
print(generated_function("+163 905-707-740"))  ## Output: 905
print(generated_function("+163 905-707-740"))  ## Output: 905
print(generated_function("+163 905-707-740"))  ## Output: 905
print(generated_function("+23 448-213-807"))  ## Output: 448
print(generated_function("+23 448-213-807"))  ## Output: 448
print(generated_function("+23 448-213-807"))  ## Output: 448
print(generated_function("+42 634-077-089"))  ## Output: 634
print(generated_function("+42 634-077-089"))  ## Output: 634
print(generated_function("+42 634-077-089"))  ## Output: 634
print(generated_function("+18 051-287-382"))  ## Output: 051
print(generated_function("+18 051-287-382"))  ## Output: 051
print(generated_function("+18 051-287-382"))  ## Output: 051
print(generated_function("+29 773-545-520"))  ## Output: 773
print(generated_function("+29 773-545-520"))  ## Output: 773
print(generated_function("+29 773-545-520"))  ## Output: 773
print(generated_function("+43 249-097-743"))  ## Output: 249
print(generated_function("+43 249-097-743"))  ## Output: 249
print(generated_function("+43 249-097-743"))  ## Output: 249
print(generated_function("+158 674-736-891"))  ## Output: 674
print(generated_function("+158 674-736-891"))  ## Output: 674
print(generated_function("+158 674-736-891"))  ## Output: 674
print(generated_function("+45 124-771-454"))  ## Output: 124
print(generated_function("+45 124-771-454"))  ## Output: 124
print(generated_function("+45 124-771-454"))  ## Output: 124
print(generated_function("+180 029-457-654"))  ## Output: 029
print(generated_function("+180 029-457-654"))  ## Output: 029
print(generated_function("+180 029-457-654"))  ## Output: 029
print(generated_function("+75 227-250-652"))  ## Output: 227
print(generated_function("+75 227-250-652"))  ## Output: 227
print(generated_function("+75 227-250-652"))  ## Output: 227
print(generated_function("+5 528-317-854"))  ## Output: 528
print(generated_function("+5 528-317-854"))  ## Output: 528
print(generated_function("+5 528-317-854"))  ## Output: 528
print(generated_function("+81 849-629-290"))  ## Output: 849
print(generated_function("+81 849-629-290"))  ## Output: 849
print(generated_function("+81 849-629-290"))  ## Output: 849
print(generated_function("+46 005-119-176"))  ## Output: 005
print(generated_function("+46 005-119-176"))  ## Output: 005
print(generated_function("+46 005-119-176"))  ## Output: 005
print(generated_function("+108 150-380-705"))  ## Output: 150
print(generated_function("+108 150-380-705"))  ## Output: 150
print(generated_function("+108 150-380-705"))  ## Output: 150
print(generated_function("+40 122-224-247"))  ## Output: 122
print(generated_function("+40 122-224-247"))  ## Output: 122
print(generated_function("+40 122-224-247"))  ## Output: 122
print(generated_function("+68 890-680-027"))  ## Output: 890
print(generated_function("+68 890-680-027"))  ## Output: 890
print(generated_function("+68 890-680-027"))  ## Output: 890
print(generated_function("+169 060-204-504"))  ## Output: 060
print(generated_function("+169 060-204-504"))  ## Output: 060
print(generated_function("+169 060-204-504"))  ## Output: 060
print(generated_function("+95 620-820-945"))  ## Output: 620
print(generated_function("+95 620-820-945"))  ## Output: 620
print(generated_function("+95 620-820-945"))  ## Output: 620
print(generated_function("+43 592-938-846"))  ## Output: 592
print(generated_function("+43 592-938-846"))  ## Output: 592
print(generated_function("+43 592-938-846"))  ## Output: 592
print(generated_function("+7 023-296-647"))  ## Output: 023
print(generated_function("+7 023-296-647"))  ## Output: 023
print(generated_function("+7 023-296-647"))  ## Output: 023
print(generated_function("+20 541-401-396"))  ## Output: 541
print(generated_function("+20 541-401-396"))  ## Output: 541
print(generated_function("+20 541-401-396"))  ## Output: 541
print(generated_function("+64 751-365-934"))  ## Output: 751
print(generated_function("+64 751-365-934"))  ## Output: 751
print(generated_function("+64 751-365-934"))  ## Output: 751
print(generated_function("+163 546-119-476"))  ## Output: 546
print(generated_function("+163 546-119-476"))  ## Output: 546
print(generated_function("+163 546-119-476"))  ## Output: 546
print(generated_function("+198 557-666-779"))  ## Output: 557
print(generated_function("+198 557-666-779"))  ## Output: 557
print(generated_function("+198 557-666-779"))  ## Output: 557
print(generated_function("+14 673-759-017"))  ## Output: 673
print(generated_function("+14 673-759-017"))  ## Output: 673
print(generated_function("+14 673-759-017"))  ## Output: 673
print(generated_function("+161 086-020-168"))  ## Output: 086
print(generated_function("+161 086-020-168"))  ## Output: 086
print(generated_function("+161 086-020-168"))  ## Output: 086
print(generated_function("+65 970-575-488"))  ## Output: 970
print(generated_function("+65 970-575-488"))  ## Output: 970
print(generated_function("+65 970-575-488"))  ## Output: 970
print(generated_function("+2 455-126-377"))  ## Output: 455
print(generated_function("+2 455-126-377"))  ## Output: 455
print(generated_function("+2 455-126-377"))  ## Output: 455
print(generated_function("+196 728-585-376"))  ## Output: 728
print(generated_function("+196 728-585-376"))  ## Output: 728
print(generated_function("+196 728-585-376"))  ## Output: 728
print(generated_function("+33 117-430-125"))  ## Output: 117
print(generated_function("+33 117-430-125"))  ## Output: 117
print(generated_function("+33 117-430-125"))  ## Output: 117
print(generated_function("+195 488-831-768"))  ## Output: 488
print(generated_function("+195 488-831-768"))  ## Output: 488
print(generated_function("+195 488-831-768"))  ## Output: 488
print(generated_function("+86 468-718-108"))  ## Output: 468
print(generated_function("+86 468-718-108"))  ## Output: 468
print(generated_function("+86 468-718-108"))  ## Output: 468
print(generated_function("+194 278-716-950"))  ## Output: 278
print(generated_function("+194 278-716-950"))  ## Output: 278
print(generated_function("+194 278-716-950"))  ## Output: 278
print(generated_function("+43 730-685-847"))  ## Output: 730
print(generated_function("+43 730-685-847"))  ## Output: 730
print(generated_function("+43 730-685-847"))  ## Output: 730
print(generated_function("+140 794-289-551"))  ## Output: 794
print(generated_function("+140 794-289-551"))  ## Output: 794
print(generated_function("+140 794-289-551"))  ## Output: 794
print(generated_function("+21 679-740-834"))  ## Output: 679
print(generated_function("+21 679-740-834"))  ## Output: 679
print(generated_function("+21 679-740-834"))  ## Output: 679
print(generated_function("+98 717-997-323"))  ## Output: 717
print(generated_function("+98 717-997-323"))  ## Output: 717
print(generated_function("+98 717-997-323"))  ## Output: 717
print(generated_function("+47 401-100-231"))  ## Output: 401
print(generated_function("+47 401-100-231"))  ## Output: 401
print(generated_function("+47 401-100-231"))  ## Output: 401
print(generated_function("+143 726-462-368"))  ## Output: 726
print(generated_function("+143 726-462-368"))  ## Output: 726
print(generated_function("+143 726-462-368"))  ## Output: 726
print(generated_function("+147 864-005-968"))  ## Output: 864
print(generated_function("+147 864-005-968"))  ## Output: 864
print(generated_function("+147 864-005-968"))  ## Output: 864
print(generated_function("+130 590-757-665"))  ## Output: 590
print(generated_function("+130 590-757-665"))  ## Output: 590
print(generated_function("+130 590-757-665"))  ## Output: 590
print(generated_function("+197 700-858-976"))  ## Output: 700
print(generated_function("+197 700-858-976"))  ## Output: 700
print(generated_function("+197 700-858-976"))  ## Output: 700
print(generated_function("+158 344-541-946"))  ## Output: 344
print(generated_function("+158 344-541-946"))  ## Output: 344
print(generated_function("+158 344-541-946"))  ## Output: 344
print(generated_function("+56 242-901-234"))  ## Output: 242
print(generated_function("+56 242-901-234"))  ## Output: 242
print(generated_function("+56 242-901-234"))  ## Output: 242
print(generated_function("+132 313-075-754"))  ## Output: 313
print(generated_function("+132 313-075-754"))  ## Output: 313
print(generated_function("+132 313-075-754"))  ## Output: 313
print(generated_function("+130 517-953-149"))  ## Output: 517
print(generated_function("+130 517-953-149"))  ## Output: 517
print(generated_function("+130 517-953-149"))  ## Output: 517
print(generated_function("+158 684-878-743"))  ## Output: 684
print(generated_function("+158 684-878-743"))  ## Output: 684
print(generated_function("+158 684-878-743"))  ## Output: 684
print(generated_function("+52 836-582-035"))  ## Output: 836
print(generated_function("+52 836-582-035"))  ## Output: 836
print(generated_function("+52 836-582-035"))  ## Output: 836
print(generated_function("+138 117-484-671"))  ## Output: 117
print(generated_function("+138 117-484-671"))  ## Output: 117
print(generated_function("+138 117-484-671"))  ## Output: 117
print(generated_function("+50 012-148-873"))  ## Output: 012
print(generated_function("+50 012-148-873"))  ## Output: 012
print(generated_function("+50 012-148-873"))  ## Output: 012
print(generated_function("+105 048-919-483"))  ## Output: 048
print(generated_function("+105 048-919-483"))  ## Output: 048
print(generated_function("+105 048-919-483"))  ## Output: 048
print(generated_function("+18 209-851-997"))  ## Output: 209
print(generated_function("+18 209-851-997"))  ## Output: 209
print(generated_function("+18 209-851-997"))  ## Output: 209
print(generated_function("+176 938-056-084"))  ## Output: 938
print(generated_function("+176 938-056-084"))  ## Output: 938
print(generated_function("+176 938-056-084"))  ## Output: 938
print(generated_function("+141 018-132-973"))  ## Output: 018
print(generated_function("+141 018-132-973"))  ## Output: 018
print(generated_function("+141 018-132-973"))  ## Output: 018
print(generated_function("+199 936-162-415"))  ## Output: 936
print(generated_function("+199 936-162-415"))  ## Output: 936
print(generated_function("+199 936-162-415"))  ## Output: 936
print(generated_function("+33 547-051-264"))  ## Output: 547
print(generated_function("+33 547-051-264"))  ## Output: 547
print(generated_function("+33 547-051-264"))  ## Output: 547
print(generated_function("+161 233-981-513"))  ## Output: 233
print(generated_function("+161 233-981-513"))  ## Output: 233
print(generated_function("+161 233-981-513"))  ## Output: 233
print(generated_function("+115 101-728-328"))  ## Output: 101
print(generated_function("+115 101-728-328"))  ## Output: 101
print(generated_function("+115 101-728-328"))  ## Output: 101
print(generated_function("+45 095-746-635"))  ## Output: 095
print(generated_function("+45 095-746-635"))  ## Output: 095
print(generated_function("+45 095-746-635"))  ## Output: 095
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775
print(generated_function("+174 594-539-946"))  ## Output: 594
print(generated_function("+155 927-275-860"))  ## Output: 927
print(generated_function("+167 405-461-331"))  ## Output: 405
print(generated_function("+10 538-347-401"))  ## Output: 538
print(generated_function("+60 971-986-103"))  ## Output: 971
print(generated_function("+13 258-276-941"))  ## Output: 258
print(generated_function("+2 604-746-137"))  ## Output: 604
print(generated_function("+25 998-898-180"))  ## Output: 998
print(generated_function("+151 862-946-541"))  ## Output: 862
print(generated_function("+118 165-041-038"))  ## Output: 165
print(generated_function("+144 170-592-272"))  ## Output: 170
print(generated_function("+94 462-008-482"))  ## Output: 462
print(generated_function("+82 685-122-086"))  ## Output: 685
print(generated_function("+82 675-366-472"))  ## Output: 675
print(generated_function("+80 066-433-096"))  ## Output: 066
print(generated_function("+163 039-436-166"))  ## Output: 039
print(generated_function("+138 808-083-074"))  ## Output: 808
print(generated_function("+42 643-245-738"))  ## Output: 643
print(generated_function("+169 822-542-726"))  ## Output: 822
print(generated_function("+176 767-782-369"))  ## Output: 767
print(generated_function("+47 414-369-343"))  ## Output: 414
print(generated_function("+138 885-618-512"))  ## Output: 885
print(generated_function("+104 158-671-355"))  ## Output: 158
print(generated_function("+188 280-087-526"))  ## Output: 280
print(generated_function("+50 268-571-336"))  ## Output: 268
print(generated_function("+183 225-960-024"))  ## Output: 225
print(generated_function("+58 191-982-491"))  ## Output: 191
print(generated_function("+9 507-092-535"))  ## Output: 507
print(generated_function("+64 061-601-398"))  ## Output: 061
print(generated_function("+189 831-591-877"))  ## Output: 831
print(generated_function("+129 425-765-844"))  ## Output: 425
print(generated_function("+94 856-734-046"))  ## Output: 856
print(generated_function("+35 082-845-261"))  ## Output: 082
print(generated_function("+185 394-622-272"))  ## Output: 394
print(generated_function("+163 905-707-740"))  ## Output: 905
print(generated_function("+23 448-213-807"))  ## Output: 448
print(generated_function("+42 634-077-089"))  ## Output: 634
print(generated_function("+18 051-287-382"))  ## Output: 051
print(generated_function("+29 773-545-520"))  ## Output: 773
print(generated_function("+43 249-097-743"))  ## Output: 249
print(generated_function("+158 674-736-891"))  ## Output: 674
print(generated_function("+45 124-771-454"))  ## Output: 124
print(generated_function("+180 029-457-654"))  ## Output: 029
print(generated_function("+75 227-250-652"))  ## Output: 227
print(generated_function("+5 528-317-854"))  ## Output: 528
print(generated_function("+81 849-629-290"))  ## Output: 849
print(generated_function("+46 005-119-176"))  ## Output: 005
print(generated_function("+108 150-380-705"))  ## Output: 150
print(generated_function("+40 122-224-247"))  ## Output: 122
print(generated_function("+68 890-680-027"))  ## Output: 890
print(generated_function("+169 060-204-504"))  ## Output: 060
print(generated_function("+95 620-820-945"))  ## Output: 620
print(generated_function("+43 592-938-846"))  ## Output: 592
print(generated_function("+7 023-296-647"))  ## Output: 023
print(generated_function("+20 541-401-396"))  ## Output: 541
print(generated_function("+64 751-365-934"))  ## Output: 751
print(generated_function("+163 546-119-476"))  ## Output: 546
print(generated_function("+198 557-666-779"))  ## Output: 557
print(generated_function("+14 673-759-017"))  ## Output: 673
print(generated_function("+161 086-020-168"))  ## Output: 086
print(generated_function("+65 970-575-488"))  ## Output: 970
print(generated_function("+2 455-126-377"))  ## Output: 455
print(generated_function("+196 728-585-376"))  ## Output: 728
print(generated_function("+33 117-430-125"))  ## Output: 117
print(generated_function("+195 488-831-768"))  ## Output: 488
print(generated_function("+86 468-718-108"))  ## Output: 468
print(generated_function("+194 278-716-950"))  ## Output: 278
print(generated_function("+43 730-685-847"))  ## Output: 730
print(generated_function("+140 794-289-551"))  ## Output: 794
print(generated_function("+21 679-740-834"))  ## Output: 679
print(generated_function("+98 717-997-323"))  ## Output: 717
print(generated_function("+47 401-100-231"))  ## Output: 401
print(generated_function("+143 726-462-368"))  ## Output: 726
print(generated_function("+147 864-005-968"))  ## Output: 864
print(generated_function("+130 590-757-665"))  ## Output: 590
print(generated_function("+197 700-858-976"))  ## Output: 700
print(generated_function("+158 344-541-946"))  ## Output: 344
print(generated_function("+56 242-901-234"))  ## Output: 242
print(generated_function("+132 313-075-754"))  ## Output: 313
print(generated_function("+130 517-953-149"))  ## Output: 517
print(generated_function("+158 684-878-743"))  ## Output: 684
print(generated_function("+52 836-582-035"))  ## Output: 836
print(generated_function("+138 117-484-671"))  ## Output: 117
print(generated_function("+50 012-148-873"))  ## Output: 012
print(generated_function("+105 048-919-483"))  ## Output: 048
print(generated_function("+18 209-851-997"))  ## Output: 209
print(generated_function("+176 938-056-084"))  ## Output: 938
print(generated_function("+141 018-132-973"))  ## Output: 018
print(generated_function("+199 936-162-415"))  ## Output: 936
print(generated_function("+33 547-051-264"))  ## Output: 547
print(generated_function("+161 233-981-513"))  ## Output: 233
print(generated_function("+115 101-728-328"))  ## Output: 101
print(generated_function("+45 095-746-635"))  ## Output: 095

# End time: 2024-04-09 20:38:51.930839
# Elapsed time in seconds: 82.54875825399722