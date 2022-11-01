def palyndrome(number):
    """ Returns true if the enter number is a palyndrome or false if it is not
    Args:
        number: the number to be evaluated as palyndrome
    Return:
        Boolean, true or false
    """

    remaining = number
    reverse = 0
    while remaining > 0:
        rest = remaining % 10
        #print(f"rest: {rest}")
        reverse = reverse * 10 + rest
        #print(f"reverse: {reverse}")
        remaining = remaining //10
    if number == reverse:
        return True
    else: 
        return False

#log base 10 of number0
#O(d), where d is the number of digits of the number 
print(palyndrome(1121))