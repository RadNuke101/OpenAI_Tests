def return_last_three_numbers(input_str):
    # Prompt: return last three numbers in input
    # Given input as ['+106 769-858-438'] output is 438
    # Given input as ['+83 973-757-831'] output is 831
    # Given input as ['+62 647-787-775'] output is 775
    # Given input as ['+172 027-507-632'] output is 632
    # Given input as ['+72 001-050-856'] output is 856
    # Given input as ['+95 310-537-401'] output is 401
    # Given input as ['+6 775-969-238'] output is 238
    # Given input as ['+174 594-539-946'] output is 946
    # Given input as ['+155 927-275-860'] output is 860
    # Given input as ['+167 405-461-331'] output is 331
    # Given input as ['+10 538-347-401'] output is 401
    # Given input as ['+60 971-986-103'] output is 103
    # Given input as ['+13 258-276-941'] output is 941
    # Given input as ['+2 604-746-137'] output is 137
    # Given input as ['+25 998-898-180'] output is 180
    # Given input as ['+151 862-946-541'] output is 541
    # Given input as ['+118 165-041-038'] output is 038
    # Given input as ['+144 170-592-272'] output is 272
    # Given input as ['+94 462-008-482'] output is 482
    # Given input as ['+82 685-122-086'] output is 086
    # Given input as ['+82 675-366-472'] output is 472
    # Given input as ['+80 066-433-096'] output is 096
    # Given input as ['+163 039-436-166'] output is 166
    # Given input as ['+138 808-083-074'] output is 074
    # Given input as ['+42 643-245-738'] output is 738
    # Given input as ['+169 822-542-726'] output is 726
    # Given input as ['+176 767-782-369'] output is 369
    # Given input as ['+47 414-369-343'] output is 343
    # Given input as ['+138 885-618-512'] output is 512
    # Given input as ['+104 158-671-355'] output is 355
    # Given input as ['+188 280-087-526'] output is 526
    # Given input as ['+50 268-571-336'] output is 336
    # Given input as ['+183 225-960-024'] output is 024
    # Given input as ['+58 191-982-491'] output is 491
    # Given input as ['+9 507-092-535'] output is 535
    # Given input as ['+64 061-601-398'] output is 398
    # Given input as ['+189 831-591-877'] output is 877
    # Given input as ['+129 425-765-844'] output is 844
    # Given input as ['+94 856-734-046'] output is 046
    # Given input as ['+35 082-845-261'] output is 261
    # Given input as ['+185 394-622-272'] output is 272
    # Given input as ['+163 905-707-740'] output is 740
    # Given input as ['+23 448-213-807'] output is 807
    # Given input as ['+42 634-077-089'] output is 089
    # Given input as ['+18 051-287-382'] output is 382
    # Given input as ['+29 773-545-520'] output is 520
    # Given input as ['+43 249-097-743'] output is 743
    # Given input as ['+158 674-736-891'] output is 891
    # Given input as ['+45 124-771-454'] output is 454
    # Given input as ['+180 029-457-654'] output is 654
    # Given input as ['+75 227-250-652'] output is 652
    # Given input as ['+5 528-317-854'] output is 854
    # Given input as ['+81 849-629-290'] output is 290
    # Given input as ['+46 005-119-176'] output is 176
    # Given input as ['+108 150-380-705'] output is 705
    # Given input as ['+40 122-224-247'] output is 247
    # Given input as ['+68 890-680-027'] output is 027
    # Given input as ['+169 060-204-504'] output is 504
    # Given input as ['+95 620-820-945'] output is 945
    # Given input as ['+43 592-938-846'] output is 846
    # Given input as ['+7 023-296-647'] output is 647
    # Given input as ['+20 541-401-396'] output is 396
    # Given input as ['+64 751-365-934'] output is 934
    # Given input as ['+163 546-119-476'] output is 476
    # Given input as ['+198 557-666-779'] output is 779
    # Given input as ['+14 673-759-017'] output is 017
    # Given input as ['+161 086-020-168'] output is 168
    # Given input as ['+65 970-575-488'] output is 488
    # Given input as ['+2 455-126-377'] output is 377
    # Given input as ['+196 728-585-376'] output is 376
    # Given input as ['+33 117-430-125'] output is 125
    # Given input as ['+195 488-831-768'] output is 768
    # Given input as ['+86 468-718-108'] output is 108
    # Given input as ['+194 278-716-950'] output is 950
    # Given input as ['+43 730-685-847'] output is 847
    # Given input as ['+140 794-289-551'] output is 551
    # Given input as ['+21 679-740-834'] output is 834
    # Given input as ['+98 717-997-323'] output is 323
    # Given input as ['+47 401-100-231'] output is 231
    # Given input as ['+143 726-462-368'] output is 368
    # Given input as ['+147 864-005-968'] output is 968
    # Given input as ['+130 590-757-665'] output is 665
    # Given input as ['+197 700-858-976'] output is 976
    # Given input as ['+158 344-541-946'] output is 946
    # Given input as ['+56 242-901-234'] output is 234
    # Given input as ['+132 313-075-754'] output is 754
    # Given input as ['+130 517-953-149'] output is 149
    # Given input as ['+158 684-878-743'] output is 743
    # Given input as ['+52 836-582-035'] output is 035
    # Given input as ['+138 117-484-671'] output is 671
    # Given input as ['+50 012-148-873'] output is 873
    # Given input as ['+105 048-919-483'] output is 483
    # Given input as ['+18 209-851-997'] output is 997
    # Given input as ['+176 938-056-084'] output is 084
    # Given input as ['+141 018-132-973'] output is 973
    # Given input as ['+199 936-162-415'] output is 415
    # Given input as ['+33 547-051-264'] output is 264
    # Given input as ['+161 233-981-513'] output is 513
    # Given input as ['+115 101-728-328'] output is 328
    # Given input as ['+45 095-746-635'] output is 635

    return input_str[-3:]

# Test cases
print(return_last_three_numbers('+106 769-858-438'))  # Output: 438
print(return_last_three_numbers('+83 973-757-831'))  # Output: 831
print(return_last_three_numbers('+62 647-787-775'))  # Output: 775
