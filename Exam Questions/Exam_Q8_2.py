import pandas as pd
def frequency_sentence_dict(list_text):
    dict_frec={}
    for word in list_text:
        if word not in dict_frec:
            dict_frec[word]=1
        else:
            dict_frec[word]+=1
    table=pd.DataFrame.from_dict(dict_frec, orient='index',columns=["count"])
    #return (dict_frec)
    return table
list_text=["hi", "I", "am", "Alexa", "I", "would", "just", "like", "to", "say", "hi"]
print(frequency_sentence_dict(list_text))

