#1.1 Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()

#1.2 Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()


#**********************MYREDUCE FUNCTION*****************************************
#sums function
def sum(x1, x2): 
    return x1 + x2

#myreduce function taking two arguments: function and sequence(list)
def myreduce(func, seq):
    res = seq[0]
    for x in seq[1:]:
        res = sum(x, res)
    return res


#**********************MYFILTER FUNCTION*****************************************
#function of returning true if integer is positive
def positiveInt(a):
    if a>=0:
        return True
    else:
        return False
    
#myfilter function taking two argument: function and sequence(list)
def myfilter(func, seq):
    new_seq = []
    for x in seq:
        if func(x):
            new_seq.append(x)
    return new_seq


print("Sum function on list using myreduce function : " + str(myreduce(sum, [1, 2, 3, 4])))
print("positive integer function on list using myfilter function: " + str(myfilter(positiveInt, [1, 2, 3, 4, -3, -5])))

