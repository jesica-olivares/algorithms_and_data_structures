# Determine the longest sequence of increasing numbers in a list of number
def seq_increase(seq_list):
    base=seq_list[0]
    i=0
    max=[]
    aux_max=[]
    aux_max.append(base)
    while (i<len(seq_list)-1):
        
        if seq_list[i+1]>base:
            aux_max.append(seq_list[i+1])
        else:
            aux_max=[]
            aux_max.append(seq_list[i+1])
        if len(aux_max)> len(max):
            max=aux_max
        base=seq_list[i+1]
        i+=1
    print(max)

seq_list=[1, 2, 5, 7 , 9 , 3, 8, 9, 13, 24, 25,5]

seq_increase(seq_list)