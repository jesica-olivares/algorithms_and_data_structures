#Find all palindromic sections of any given string longer than one
def palindrome(text_pal):
    i=0
    pal=[]
    for j in range(len(text_pal)-1):
        text_aux=text_pal[i]+text_pal[i+1]
        if text_aux==text_aux[::-1]:
            pal.append(text_aux)
            k=1
            text_aux_2=text_aux
            while (text_aux_2==text_aux_2[::-1]) and (len(text_pal)> j+k+1):
                text_aux_2=text_pal[j-k]+text_aux_2+text_pal[j+k+1]
                if text_aux_2==text_aux_2[::-1]:
                        pal.append(text_aux)
                k+=1
        i+=1
    i=0
    for j in range(len(text_pal)-2):
        text_aux=text_pal[i]+text_pal[i+1]+text_pal[i+2]
        if text_aux==text_aux[::-1]:
            pal.append(text_aux)
            k=1
            text_aux_2=text_aux
            while (text_aux_2==text_aux_2[::-1]) and (len(text_pal)> j+k+2):
                text_aux_2=text_pal[j-k]+text_aux_2+text_pal[j+k+2]
                if text_aux_2==text_aux_2[::-1]:
                        pal.append(text_aux_2)
                k+=1
        i+=1
    if pal:
        print(pal)
    else:
        print("No Palindromes")

text_pal="saippuakivikauppias"
#"saippuakivikauppias"
#"mannam"
palindrome(text_pal)