def linear_search(array,target):
    # best case: time complexity - O(1)
    # average case: time complexity - O(n)
    # worst case: time complexity - O(n)
    for i in range(len(array)):
        if array[i]==target:
            return i
    else:
        return -1

if __name__=="__main__":
    array=[1,3,9,0,4]
    a=linear_search(array,9)
    if a!=-1:
        print(a)
    else:
        print("Element not found")