def factorSum(x):
    """
    sum all the divide prime numbers

    :param x:the number from the user
    :return:the sum
    """
    if x <= 1:
        print("error")
        return 0
    d = 2
    gruop = set()
    while d < x:
        if x % d == 0:
            gruop.add(d)
            x = x / d
        else:
            d += 1
    if d == x:
        gruop.add(d)
    print(sum(gruop))



def f(x):
    return x+1

def onlyPositive(f):
    """
    this funcuion get an another function and add 1 to the number we sent if is negative we make him positive
    and add one

    :param f: the function
    :return: return a function that check the number
    """
    def calc(x):
        if x>=0:
            return f(x)
        else:
            return f(abs(x))
    return calc




def interceptPoint(p1,p2):
    """
    the function get two line and check if there are any Cutting point

    to check if there are any cutting point we solve An equation with two vanishing points
    :param p1:line 1
    :param p2:line 2
    :return:cutting point
    """
    x1,c1=p1
    x2,c2=p2
    if (x1-x2)==0:
        return
    x3=(c2-c1)/(x1-x2)
    y3=x1*x3+c1
    p3=(x3,y3)
    return p3



def printNumbers(x,y,z):
    """
    print all the number in the range besides the z variable

    the function check all the cases:the beginning and the end of the range
    :param x:the start of the range
    :param y:end of the range
    :param z:the number we dont want in the range
    :return:the new range
    """
    if x==z and x<y:
        x+=1
    if x==z and x>y:
        x-=1
    print(x)
    if x==y:
        return
    if x<y:
        printNumbers(x+1,y,z)
    if x>y:
        printNumbers(x-1,y,z)



def arrProduct(arr1,arr2):
    """
    the function get 2 array's with the same size and make new array with the amount of index in the second array to the
    first array

    the size of the new array is the sum of all the index in the second array,we put the numbers in the new array with
    nested Loop
    :param arr1:first array
    :param arr2:second array
    :return:new array
    """
    arr3=[]
    for i in range(len(arr2)):
        for j in range (arr2[i]):
            arr3.append(arr1[i])
    return arr3




def analyze(str):
    """"
    check in the str number greater than 75

    str convert to array
    than check every index in the array if he greater than 75
    """
    count=0
    arr=str.split(',')
    arr_size=len(arr)
    for i in range(arr_size):
        if float(arr[i])>75:
            count+=1
    return count