def insertionsort(list1):
    #best case: Time complexity- O(n)
    #worst case: O(n^2)
    #avergage case: O(n^2)
    
    length=len(list1)
    for i in range(1,length):
        key=list1[i]
        j=i-1

        while j>=0 and key<list1[j]:
            list1[j+1]=list1[j]
            j=j-1
        
        list1[j+1]=key
    return list1

if __name__=="__main__":
    list1=[14,25,6,90,5]
    print(insertionsort(list1))