from functools import reduce
def factorial (input):
    #function print as a result the factorial of given number
    #as a input, there is a number, for which we whant the factorial
    print(reduce(lambda x,y:x*y,range(1,input+1)))
    

