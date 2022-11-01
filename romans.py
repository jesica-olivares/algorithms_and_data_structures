def roman_numbers(number):
    """transforms the given number to the equivalent in roman numbers, for integer numbers between and 3999"""

    #test if the given number is between the range of the function, otherwise, ask for another input
    while not int(number) in range(1, 3999):
        number = int(input("Please enter a number in the range [1 - 3999] : "))
    #define an empty variable to store the roman equivalent
    roman=""
    #all numbers and/or special cases are defined with their equivalent:
    number_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_symbol = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    #define a variable remaining, corresponding to what is still not transformed:
    remaining = number

    #initialize a loop that will start from the larger numbers downward and will keep running until the remaining is zero or the final number of the preciously defined list is reached
    i=12
    while (remaining > 0) and (i >= 0):
        #defined a variable that will represent the number of times that for each symbol
        transformed = remaining //  number_list[i]
        if transformed > 0:
            #if  the previous sumber is larger than 0, then the symbol is printed:
            while transformed > 0:
                #the symbol should be printed as many times as the defined transformed variable
                #print(roman_symbol[i],end="") 
                roman += roman_symbol[i]
                #as the symbol is printed, 1 is substracted from the variable to exit the loop
                transformed -= 1
            #the remaining from the division corresponds to the part of the number that is still not converted to roman numbers
            remaining = remaining % number_list[i]
        #one is substracted from the i variable, to go to the next item on the list in the next iteration
        i -= 1
    return(roman)

number = 1348
print(roman_numbers(number))
