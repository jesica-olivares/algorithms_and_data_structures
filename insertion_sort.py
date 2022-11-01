
def insertion_sort(list_):
    i=1
    while i<len(list_):
        key=list_[i]
        j = i-1
        while list_[j]>key and j>=0:
            list_[j+1] = list_[j]
            j=j-1
        list_[j+1]=key
        i=i+1
    print(list_)

