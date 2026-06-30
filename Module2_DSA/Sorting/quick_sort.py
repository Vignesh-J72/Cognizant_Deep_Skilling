def quicksort(list1):
    #best case : time complexity - O(n log n)
    #average case : time complexity - O(n log n)
    #worst case : time complexity - O(n^2)

    if len(list1)<=1:
        return list1
    
    key=list1[-1]
    left=[]
    right=[]

    for i in range(0,len(list1)-1):
        if list1[i]<key:
            left.append(list1[i])
        else:
            right.append(list1[i])
    
    return quicksort(left)+[key]+quicksort(right)

if __name__=='__main__':
    list1=[1,5,2,9,10,7]
    print(quicksort(list1))