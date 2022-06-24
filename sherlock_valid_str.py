# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Determine if there are either the same instances of each letter or if there can be with 1 deletion.

# a = "aabbcd"
# a = "aabbccddeefghi"
a = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcgggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"
def isValid(s):
    letter_list = []
    letter_occurrence = []
    for letter in s:
        letter_list.append(letter)                                                      # Create a list from the string
    letter_set = set(letter_list)                                                       # Create a set from the list
    for letter in letter_set:
        letter_occurrence.append(letter_list.count(letter))                             # Create a list of the occurrences
    letter_occurrence.sort()                                                            # Sort so that the lower number of occurrences appears first
    occur_len = len(letter_occurrence)                                                  # Length of the occurrence list
    occur_set = len(set(letter_occurrence))                                             # Set of the occurrence list
    comp_one = letter_occurrence[0]
    i = 1
    if occur_set == 1:                                                                  # If all occurrences are the same return YES
        return "YES"
    
    while i < occur_len:                                                                # Iterate through list and compare occurrences
        comp_two = letter_occurrence[i]
        if  comp_two > comp_one and comp_two - comp_one == 1:                           # If the next item is greater than the current item by 1, stop loop
            break
        elif (comp_two > comp_one) and i == 1 and letter_occurrence[0] == 1 and occur_set == 2: # Diff > 1, compare first 2 items, and only 2 items in set
            return "YES"
        elif comp_two > comp_one:
            return "NO"                                                                 # If the next item is greater than the current item (by more than 1), return NO
        else:
            i += 1
    if i == occur_len - 1:                                                              # Determine if the greater item is the last in the list
        return "YES"
    elif i == 1 and occur_set == 2:                                                     # If the differene is 1 and there are 2 items in set
        return "YES"
    else:
        return "NO"

print(isValid(a))