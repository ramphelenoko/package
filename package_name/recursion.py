def sum_array(array):

    ''' Return sum of all items in array'''

    arr = sum(array)
    return arr

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <= 1:
       return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
