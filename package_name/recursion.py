def sum_array(array):

    ''' Return sum of all items in array'''

    arr = sum(array)
    return arr

def Fibonacci(n): 
   
    '''Return nth term in fibonacci sequence'''

    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
