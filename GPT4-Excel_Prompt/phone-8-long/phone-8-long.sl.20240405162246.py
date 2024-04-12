# Start time: 2024-04-05 16:45:14.231006

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last three numbers in input, and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, input as ['+174 594-539-946'] output is 946, input as ['+155 927-275-860'] output is 860, input as ['+167 405-461-331'] output is 331, input as ['+10 538-347-401'] output is 401, input as ['+60 971-986-103'] output is 103, input as ['+13 258-276-941'] output is 941, input as ['+2 604-746-137'] output is 137, input as ['+25 998-898-180'] output is 180, input as ['+151 862-946-541'] output is 541, input as ['+118 165-041-038'] output is 038, input as ['+144 170-592-272'] output is 272, input as ['+94 462-008-482'] output is 482, input as ['+82 685-122-086'] output is 086, input as ['+82 675-366-472'] output is 472, input as ['+80 066-433-096'] output is 096, input as ['+163 039-436-166'] output is 166, input as ['+138 808-083-074'] output is 074, input as ['+42 643-245-738'] output is 738, input as ['+169 822-542-726'] output is 726, input as ['+176 767-782-369'] output is 369, input as ['+47 414-369-343'] output is 343, input as ['+138 885-618-512'] output is 512, input as ['+104 158-671-355'] output is 355, input as ['+188 280-087-526'] output is 526, input as ['+50 268-571-336'] output is 336, input as ['+183 225-960-024'] output is 024, input as ['+58 191-982-491'] output is 491, input as ['+9 507-092-535'] output is 535, input as ['+64 061-601-398'] output is 398, input as ['+189 831-591-877'] output is 877, input as ['+129 425-765-844'] output is 844, input as ['+94 856-734-046'] output is 046, input as ['+35 082-845-261'] output is 261, input as ['+185 394-622-272'] output is 272, input as ['+163 905-707-740'] output is 740, input as ['+23 448-213-807'] output is 807, input as ['+42 634-077-089'] output is 089, input as ['+18 051-287-382'] output is 382, input as ['+29 773-545-520'] output is 520, input as ['+43 249-097-743'] output is 743, input as ['+158 674-736-891'] output is 891, input as ['+45 124-771-454'] output is 454, input as ['+180 029-457-654'] output is 654, input as ['+75 227-250-652'] output is 652, input as ['+5 528-317-854'] output is 854, input as ['+81 849-629-290'] output is 290, input as ['+46 005-119-176'] output is 176, input as ['+108 150-380-705'] output is 705, input as ['+40 122-224-247'] output is 247, input as ['+68 890-680-027'] output is 027, input as ['+169 060-204-504'] output is 504, input as ['+95 620-820-945'] output is 945, input as ['+43 592-938-846'] output is 846, input as ['+7 023-296-647'] output is 647, input as ['+20 541-401-396'] output is 396, input as ['+64 751-365-934'] output is 934, input as ['+163 546-119-476'] output is 476, input as ['+198 557-666-779'] output is 779, input as ['+14 673-759-017'] output is 017, input as ['+161 086-020-168'] output is 168, input as ['+65 970-575-488'] output is 488, input as ['+2 455-126-377'] output is 377, input as ['+196 728-585-376'] output is 376, input as ['+33 117-430-125'] output is 125, input as ['+195 488-831-768'] output is 768, input as ['+86 468-718-108'] output is 108, input as ['+194 278-716-950'] output is 950, input as ['+43 730-685-847'] output is 847, input as ['+140 794-289-551'] output is 551, input as ['+21 679-740-834'] output is 834, input as ['+98 717-997-323'] output is 323, input as ['+47 401-100-231'] output is 231, input as ['+143 726-462-368'] output is 368, input as ['+147 864-005-968'] output is 968, input as ['+130 590-757-665'] output is 665, input as ['+197 700-858-976'] output is 976, input as ['+158 344-541-946'] output is 946, input as ['+56 242-901-234'] output is 234, input as ['+132 313-075-754'] output is 754, input as ['+130 517-953-149'] output is 149, input as ['+158 684-878-743'] output is 743, input as ['+52 836-582-035'] output is 035, input as ['+138 117-484-671'] output is 671, input as ['+50 012-148-873'] output is 873, input as ['+105 048-919-483'] output is 483, input as ['+18 209-851-997'] output is 997, input as ['+176 938-056-084'] output is 084, input as ['+141 018-132-973'] output is 973, input as ['+199 936-162-415'] output is 415, input as ['+33 547-051-264'] output is 264, input as ['+161 233-981-513'] output is 513, input as ['+115 101-728-328'] output is 328, input as ['+45 095-746-635'] output is 635, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Extracting the last three numbers from the input phone number string
    return phone_number[-3:]

# Test cases based on the provided examples
print(generated_function('+106 769-858-438'))  # Expected output: 438
print(generated_function('+83 973-757-831'))  # Expected output: 831
print(generated_function('+62 647-787-775'))  # Expected output: 775
print(generated_function('+172 027-507-632'))  # Expected output: 632
print(generated_function('+72 001-050-856'))  # Expected output: 856
print(generated_function('+95 310-537-401'))  # Expected output: 401
print(generated_function('+6 775-969-238'))  # Expected output: 238
print(generated_function('+174 594-539-946'))  # Expected output: 946
print(generated_function('+155 927-275-860'))  # Expected output: 860
print(generated_function('+167 405-461-331'))  # Expected output: 331
# Additional test cases based on the pattern
print(generated_function('+10 538-347-401'))  # Expected output: 401
print(generated_function('+60 971-986-103'))  # Expected output: 103
print(generated_function('+13 258-276-941'))  # Expected output: 941
print(generated_function('+2 604-746-137'))  # Expected output: 137
print(generated_function('+25 998-898-180'))  # Expected output: 180
print(generated_function('+151 862-946-541'))  # Expected output: 541
print(generated_function('+118 165-041-038'))  # Expected output: 038
print(generated_function('+144 170-592-272'))  # Expected output: 272
print(generated_function('+94 462-008-482'))  # Expected output: 482
print(generated_function('+82 685-122-086'))  # Expected output: 086
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238
print(generated_function("+174 594-539-946"))  ## Output: 946
print(generated_function("+155 927-275-860"))  ## Output: 860
print(generated_function("+167 405-461-331"))  ## Output: 331
print(generated_function("+10 538-347-401"))  ## Output: 401
print(generated_function("+60 971-986-103"))  ## Output: 103
print(generated_function("+13 258-276-941"))  ## Output: 941
print(generated_function("+2 604-746-137"))  ## Output: 137
print(generated_function("+25 998-898-180"))  ## Output: 180
print(generated_function("+151 862-946-541"))  ## Output: 541
print(generated_function("+118 165-041-038"))  ## Output: 038
print(generated_function("+144 170-592-272"))  ## Output: 272
print(generated_function("+94 462-008-482"))  ## Output: 482
print(generated_function("+82 685-122-086"))  ## Output: 086
print(generated_function("+82 675-366-472"))  ## Output: 472
print(generated_function("+80 066-433-096"))  ## Output: 096
print(generated_function("+163 039-436-166"))  ## Output: 166
print(generated_function("+138 808-083-074"))  ## Output: 074
print(generated_function("+42 643-245-738"))  ## Output: 738
print(generated_function("+169 822-542-726"))  ## Output: 726
print(generated_function("+176 767-782-369"))  ## Output: 369
print(generated_function("+47 414-369-343"))  ## Output: 343
print(generated_function("+138 885-618-512"))  ## Output: 512
print(generated_function("+104 158-671-355"))  ## Output: 355
print(generated_function("+188 280-087-526"))  ## Output: 526
print(generated_function("+50 268-571-336"))  ## Output: 336
print(generated_function("+183 225-960-024"))  ## Output: 024
print(generated_function("+58 191-982-491"))  ## Output: 491
print(generated_function("+9 507-092-535"))  ## Output: 535
print(generated_function("+64 061-601-398"))  ## Output: 398
print(generated_function("+189 831-591-877"))  ## Output: 877
print(generated_function("+129 425-765-844"))  ## Output: 844
print(generated_function("+94 856-734-046"))  ## Output: 046
print(generated_function("+35 082-845-261"))  ## Output: 261
print(generated_function("+185 394-622-272"))  ## Output: 272
print(generated_function("+163 905-707-740"))  ## Output: 740
print(generated_function("+23 448-213-807"))  ## Output: 807
print(generated_function("+42 634-077-089"))  ## Output: 089
print(generated_function("+18 051-287-382"))  ## Output: 382
print(generated_function("+29 773-545-520"))  ## Output: 520
print(generated_function("+43 249-097-743"))  ## Output: 743
print(generated_function("+158 674-736-891"))  ## Output: 891
print(generated_function("+45 124-771-454"))  ## Output: 454
print(generated_function("+180 029-457-654"))  ## Output: 654
print(generated_function("+75 227-250-652"))  ## Output: 652
print(generated_function("+5 528-317-854"))  ## Output: 854
print(generated_function("+81 849-629-290"))  ## Output: 290
print(generated_function("+46 005-119-176"))  ## Output: 176
print(generated_function("+108 150-380-705"))  ## Output: 705
print(generated_function("+40 122-224-247"))  ## Output: 247
print(generated_function("+68 890-680-027"))  ## Output: 027
print(generated_function("+169 060-204-504"))  ## Output: 504
print(generated_function("+95 620-820-945"))  ## Output: 945
print(generated_function("+43 592-938-846"))  ## Output: 846
print(generated_function("+7 023-296-647"))  ## Output: 647
print(generated_function("+20 541-401-396"))  ## Output: 396
print(generated_function("+64 751-365-934"))  ## Output: 934
print(generated_function("+163 546-119-476"))  ## Output: 476
print(generated_function("+198 557-666-779"))  ## Output: 779
print(generated_function("+14 673-759-017"))  ## Output: 017
print(generated_function("+161 086-020-168"))  ## Output: 168
print(generated_function("+65 970-575-488"))  ## Output: 488
print(generated_function("+2 455-126-377"))  ## Output: 377
print(generated_function("+196 728-585-376"))  ## Output: 376
print(generated_function("+33 117-430-125"))  ## Output: 125
print(generated_function("+195 488-831-768"))  ## Output: 768
print(generated_function("+86 468-718-108"))  ## Output: 108
print(generated_function("+194 278-716-950"))  ## Output: 950
print(generated_function("+43 730-685-847"))  ## Output: 847
print(generated_function("+140 794-289-551"))  ## Output: 551
print(generated_function("+21 679-740-834"))  ## Output: 834
print(generated_function("+98 717-997-323"))  ## Output: 323
print(generated_function("+47 401-100-231"))  ## Output: 231
print(generated_function("+143 726-462-368"))  ## Output: 368
print(generated_function("+147 864-005-968"))  ## Output: 968
print(generated_function("+130 590-757-665"))  ## Output: 665
print(generated_function("+197 700-858-976"))  ## Output: 976
print(generated_function("+158 344-541-946"))  ## Output: 946
print(generated_function("+56 242-901-234"))  ## Output: 234
print(generated_function("+132 313-075-754"))  ## Output: 754
print(generated_function("+130 517-953-149"))  ## Output: 149
print(generated_function("+158 684-878-743"))  ## Output: 743
print(generated_function("+52 836-582-035"))  ## Output: 035
print(generated_function("+138 117-484-671"))  ## Output: 671
print(generated_function("+50 012-148-873"))  ## Output: 873
print(generated_function("+105 048-919-483"))  ## Output: 483
print(generated_function("+18 209-851-997"))  ## Output: 997
print(generated_function("+176 938-056-084"))  ## Output: 084
print(generated_function("+141 018-132-973"))  ## Output: 973
print(generated_function("+199 936-162-415"))  ## Output: 415
print(generated_function("+33 547-051-264"))  ## Output: 264
print(generated_function("+161 233-981-513"))  ## Output: 513
print(generated_function("+115 101-728-328"))  ## Output: 328
print(generated_function("+45 095-746-635"))  ## Output: 635

# End time: 2024-04-05 16:45:28.442432
# Elapsed time in seconds: 14.211258753000038