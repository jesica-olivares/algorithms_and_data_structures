#Print out all Fibonacci numbers smaller or equal to a given number

def fibonacci(num):
    list=[]
    num_i=0
    list.append(num_i)
    num_i=1
    list.append(num_i)
    i=0
    while num_i<=num:
        list.append(num_i)
        num_i+=list[i]
        i+=1

    print(list)

fibonacci(200)