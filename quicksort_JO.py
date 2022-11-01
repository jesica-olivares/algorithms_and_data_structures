
import sys
sys.setrecursionlimit(10000)

def quicksort(array, pivot_choice="last"):
    """"Function that sorts a given array using the quicksort algorithm.
        Two choices to define the pivot value are given: the last one or the value closest to the mean, this is to run the different scenarios: best, average and worst
    Arg: 
        array: array with numbers to be sorted
        pivot_choice: way of determine the pivot, either last or median

    Return:
        sorted list
    """

    #define the lists that will be used to separate the array, respect the pivot: smaller, equal and larger.
    smaller=[]
    larger=[]
    equal=[]

    #define that the function will run as long as the length of the array evaluated is larger than 1, otherwise, the iteration will end
    if len(array) > 1:
        #assign the pivot as the last item of the array
        if pivot_choice=="median":
            pivot=array[len(array)//2]
        elif pivot_choice=="last":
            pivot=array[-1]
        #generate the conditions to divide the array into the values that are less, larger or equal to the pivot, and append those values to their respective lists
        for i in array:
            if i < pivot :
                smaller.append(i)
            elif i > pivot :
                larger.append(i)
            elif i == pivot :
                equal.append(i)
        #apply recursion to the lists that smaller and larger than the pivot:
        if pivot_choice=="median":
            smaller = quicksort(smaller,"median")
            larger = quicksort(larger,"median")
        else:
            smaller = quicksort(smaller)
            larger = quicksort(larger)
        #concatenate the result to obtain an order list
        rearranged = smaller + equal + larger
        return rearranged
    else:
        #end the recursion when the lenght of the array is not larger than 1
        return array

#run the algorithm for an example        
array =[97, 200, 100, 101, 211, 107, 5, 10, 1, 54, 76]
print(quicksort(array))

# create a function to run the multiple scenarios and obtain the time used to apply the algorithm:
# for the average scenario the initialy ordered list is shuffle, so that the pivot selection will be random
# for the worst case the list is ordered and the pivot will be the last, so it will always separate the arrays in the worst combination: separating only one variable and maintaining all the others to iterate.
# for the best case, the list is ordered and the pivot will try to obtain the middle value of the array

import random
import time
def run_quicksort(array,scenario):
    """runs the quicksort function, for the given scenario, a"""
    if scenario == "average":    
        random.shuffle(array)
    total_length = 0
    number_of_runs = 0
    time_begin = time.time()
    number_of_runs = number_of_runs + 1
    if scenario=="best":
        quicksort(array,"median")
    else:
        quicksort(array)
    time_end = time.time()
    time_to_run = time_end - time_begin
    return time_to_run

def iterate_qs(n_lenghts, scenario):
    """ iterates through the different lenghts of arrays: n_lenghts, for the given scenario"""
    time_results=[]
    for n in n_legths:
        list_to_be_sorted = list(range(1,n))
        time_results.append(run_quicksort(list_to_be_sorted, scenario))
    return time_results



n_legths=[400,800,1200,1800,2200]


#define 3 list to store the results of the best, average and worst scenario:
best_scenario_ext=[]
average_scenario_ext=[]
worst_scenario_ext=[]

for k in list(range(0,10)):
    best_scenario=iterate_qs(n_legths,"best")
    best_scenario_ext.append(best_scenario)
    average_scenario=iterate_qs(n_legths,"average")
    average_scenario_ext.append(average_scenario)
    worst_scenario=iterate_qs(n_legths,"worst")
    worst_scenario_ext.append(worst_scenario)
    
best_scenario_ext= [sum(sub_list) / len(sub_list) for sub_list in zip(*best_scenario_ext)]
average_scenario_ext= [sum(sub_list) / len(sub_list) for sub_list in zip(*average_scenario_ext)]
worst_scenario_ext= [sum(sub_list) / len(sub_list) for sub_list in zip(*worst_scenario_ext)]

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.plot(n_legths,best_scenario_ext,label="best", color="deepskyblue", )
plt.plot(n_legths,average_scenario_ext,label="average", color="seagreen")
plt.plot(n_legths,worst_scenario_ext,label="worst",color="blueviolet")

plt.legend()
plt.ylabel('time')
plt.xlabel('size of array')
plt.show()


## Complexity of Quicksort:
### worst: O (n^2)
### average: O (n log n)
### best:  O (n log n)

### For the case analyzed, unfortunately, due to the restriction of Python about the recursive maximum, it wasn't possible to see the effect of the 3 cases for 
### larger arrays, however, it was possible to see that in all cases, the worst case, performs considerably worst that the other two. Also, for the analyzed array sizes, it was still possible to see, how the time increased, with every increase of the size.
### On the other hand, best case and average case, didn't present a significant difference
