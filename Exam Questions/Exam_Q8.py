#Calculate the frequency of items in a given sequence
#Given a sequence of elements (that support equality function), calculate the frequency of
#each distinct element. For example, given the sequence [‘hi’, ‘I’, ‘am’, ‘Alexa’, ‘I’, ‘would’, ‘just’,
#‘like’, ‘to’, ‘say’, ‘hi’]. The output should be:

def frequency_sentence(list_text):
    list_unique=[]
    count_unique=[]
    for i in list_text:
        if i not in list_unique:
            list_unique.append(i)
            count_unique.append(1)
        else:
            count_unique[list_unique.index(i)]=count_unique[list_unique.index(i)]+1



    for i in range(len(list_unique)):
        print(f"{list_unique[i]}: {count_unique[i]}")

list_text=["hi", "I", "am", "Alexa", "I", "would", "just", "like", "to", "say", "hi"]
frequency_sentence(list_text)



