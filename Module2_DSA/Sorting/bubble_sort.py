def bubblesort(list1):
    #best case: Time complexity- O(n)
    #worst case: O(n^2)
    #avergage case: O(n^2)
    
    length=len(list1)
    
    for i in range(length):
        moved=False

        for j in range(0,length-i-1):
            if list1[j]> list1[j+1]:
                list1[j], list1[j+1]= list1[j+1], list1[j]
                moved=True
        
        if moved==False:
            break

if __name__=="__main__":
    ex=[45,90,11,94,60]
    bubblesort(ex)
    print(ex)