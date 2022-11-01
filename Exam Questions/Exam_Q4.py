# Determine if a sequence of numbers is increasing


def seq_increase(seq_list):
    base=seq_list[0]
    i=0
    while (i<len(seq_list)-1) and (seq_list[i+1]>base):
        base=seq_list[i+1]
        i+=1
    if i==len(seq_list)-1:
        print("Increasing")
    else:
        print("Not Increasing")

seq_list=[2,5,7,10,22]

seq_increase(seq_list)