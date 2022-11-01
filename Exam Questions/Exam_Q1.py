
#Determine if a given string is a palindrome

def palindrome(text_pal):
    if text_pal==text_pal[::-1]:
        print(f"The text {text_pal} is a palindrome")
    else:
        print(f"The text {text_pal} is not a palindrome")

text_pal="heidi"
#"saippuakivikauppias"
#"mannam"
palindrome(text_pal)