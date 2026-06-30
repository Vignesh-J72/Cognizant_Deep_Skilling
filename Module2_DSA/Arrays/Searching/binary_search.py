def binary_search(array,left,right,target):
    # best case: time complexity - O(1)
    # average case: O(log n)
    # worst case: O(log n)
    if right>=left:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        
        elif array[mid]>target:
            return binary_search(array,left,mid-1,target)
        
        else:
            return binary_search(array,mid+1,right,target)
    
    else:
        return -1

if __name__=="__main__":
    array=[1,2,3,4,5,6,7,8,9,10]
    target=9
    result=binary_search(array,0,len(array)-1,target)
    if result!=-1:
        print(result)
    else:
        print("Target not in array")
        