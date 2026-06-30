def makeHeap(list1,n,i):
    large=i
    left=2*i+1
    right=2*i+2

    if left<n and list1[left]>list1[large]:
        large=left
    
    if right<n and list1[right]>list1[large]:
        large=right

    if large!=i:
        list1[i],list1[large]=list1[large],list1[i]
        makeHeap(list1,n,large)

def heapsort(list1):
    #best case : time complexity - O(n log n)
    #average case : time complexity - O(n log n)
    #worst case : time complexity - O(n log n)

    n=len(list1)

    for i in range(n//2-1,-1,-1):
        makeHeap(list1,n,i)
    
    for i in range(n-1,0,-1):
        list1[0],list1[i]=list1[i],list1[0]
        makeHeap(list1,i,0)
    return list1

if __name__=="__main__":
    list1=[0,10,3,40,9,90]
    print(heapsort(list1))
    
