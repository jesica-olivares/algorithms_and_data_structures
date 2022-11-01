#Determine given two strings if one is an anagram of the other
def anagram(string1,string2):

    sort1 = sorted(string1)
    sort2 = sorted(string2)

    if sort1==sort2:
        print(f"The two strings {string1} and {string2} are anagrams")
    else:
        print(f"The two strings {string1} and {string2} are not anagrams")

string1="anagram"
string2="margana"

anagram(string1,string2)
