def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
       
    """
    if number<0:
        return -1
    if number==1:
        return 1
    else:
        return binary_sqrt(0,number//2,number)
def binary_sqrt(left,right,target):
    mid=(left+right)//2
    if mid**2<=target<(mid+1)**2:
        return mid
    elif mid**2>target:
        return binary_sqrt(left,mid-1,target)
    return binary_sqrt(mid+1,right,target)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
