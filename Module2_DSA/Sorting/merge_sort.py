def mergesort(list1):
    # best case: time complexity - O(n log n)
    # average case: O(n log n)
    # worst case: O(n log n)
    
    if len(list1)<=1:
        return list1
    
    mid=len(list1)//2
    left=list1[:mid]
    left_list=mergesort(left)
    right=list1[mid:]
    right_list=mergesort(right)
    return join(left_list,right_list)

def join(left,right):
    result=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        
        if left[i]<right[j]:
            result.append(left[i])
            i=i+1
        
        else:
            result.append(right[j])
            j=j+1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__=="__main__":
    list1=[1,5,3,10,8]
    print(mergesort(list1))
