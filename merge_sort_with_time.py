def merge_sort(original_list):
    #create the condition to continue dividing the list
    if len(original_list)>1:
        #define the middle of the list
        middle = len(original_list) // 2
        #generate the division of the list into: left and right from the middle:
        left_list=original_list[:middle]
        right_list=original_list[middle:]
        #print(f"left: {left_list}")  
        #print(f"right: {right_list}")  

        #apply the function to both: left and right listss:
        merge_sort(left_list)

        merge_sort(right_list)

        #initialize auxiliary variable:
        i=0
        j=0
        k=0

        #generate the loops to continue while the len of the lists are larger than the auxiliary variables:
        while i < len(left_list) and j< len(right_list):
            #print(original_list)
            #sort the values comparing left to right and modify if needed
            if left_list[i]<=right_list[j]:
                original_list[k]=left_list[i]
                i+=1
            else:
                original_list[k]=right_list[j]
                j+=1
            k+=1
            
        while i < len(left_list):
            original_list[k] = left_list[i]
            i += 1
            k += 1
 
        while j < len(right_list):
            original_list[k] = right_list[j]
            j += 1
            k += 1
    return original_list

list_order = [12, 11, 13, 5, 6, 7]
merge_sort(list_order)
print(list_order)


#Apply the function to different leghts of input lists, and estimate the time complexity

import random
import time
def run_merge_sort(array,scenario):
    """runs the merge sort function, for the given scenario, a"""
    if scenario == "average":    
        random.shuffle(array)
    elif scenario == "worst":    
        array=array[::-1]
    total_length = 0
    number_of_runs = 0
    time_begin = time.time()
    number_of_runs = number_of_runs + 1
    merge_sort(array)
    time_end = time.time()
    time_to_run = time_end - time_begin
    return time_to_run

def iterate_qs(n_lenghts, scenario):
    """ iterates through the different lenghts of arrays: n_lenghts, for the given scenario"""
    time_results=[]
    for n in n_legths:
        list_to_be_sorted = list(range(1,n))
        time_results.append(run_merge_sort(list_to_be_sorted, scenario))
    return time_results

n_legths=list(range(0,10000,100))

#define 3 list to store the results of the best, average and worst scenario:
best_scenario_ext=[]
average_scenario_ext=[]
worst_scenario_ext=[]
#iterate the function 100 times to obtain a smoothed result
for k in list(range(0,100)):
    best_scenario=iterate_qs(n_legths,"best")
    best_scenario_ext.append(best_scenario)
    average_scenario=iterate_qs(n_legths,"average")
    average_scenario_ext.append(average_scenario)
    worst_scenario=iterate_qs(n_legths,"worst")
    worst_scenario_ext.append(worst_scenario)
    
best_scenario_ext= [sum(sub_list) / len(sub_list) for sub_list in zip(*best_scenario_ext)]
average_scenario_ext= [sum(sub_list) / len(sub_list) for sub_list in zip(*average_scenario_ext)]
worst_scenario_ext= [sum(sub_list) / len(sub_list) for sub_list in zip(*worst_scenario_ext)]

#graph the result for the three scenarios
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.plot(n_legths,best_scenario_ext,label="best", color="deepskyblue", )
plt.plot(n_legths,average_scenario_ext,label="average", color="seagreen")
plt.plot(n_legths,worst_scenario_ext,label="worst",color="blueviolet")

plt.legend()
plt.ylabel('time')
plt.xlabel('size of array')
plt.show()