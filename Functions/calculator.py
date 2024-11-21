def cal(a,b):
    """
    This function calculates the sum,subration,multiplication,division of all numbers passed as arguments.
    """
    return a+b, a-b,a*b,a/b
    
result = cal(34,5)
print(result)
print(type(result))