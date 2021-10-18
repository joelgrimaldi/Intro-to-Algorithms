import random
import time
 
# code pretty much does the same thing
# as the method quickSorted but with
# random pivots
def r_selector(arr,low,high,k):
 
    if (k > 0 and k <= high - low + 1):
 
        x = arr[high]
        i = (low-1)
        for j in range(low, high): 
            if arr[j] <= x:                         # checks if current value
                i = i+1                             #  <= pivot and adjusts
                arr[i], arr[j] = arr[j], arr[i]     #  arr accordingly

        arr[i+1], arr[high] = arr[high], arr[i+1]
        index = i+1

        if (index - low == k - 1):
            return arr[index]
 
        if (index - low > k - 1):
            return r_selector(arr, low, index - 1, k)
        return r_selector(arr, index + 1, high, k - index + low - 1)

def r_select(arr, k):
    return r_selector(arr,0,len(arr)-1,k)

def d_select(arr, k):

    # following code will execute when an array
    # of short enough length occurs because
    # it'll have minimal impact on runtime 
    if len(arr) <= 10:
        arr.sort()
        return arr[k]
    
    # following code will create an array of
    # subarrays from arr of length 5
    S = []                              # split array init
    sIndex = 0                              # split index
    while sIndex+5 < len(arr)-1:
        S.append(arr[sIndex:sIndex+5])  # appends array
        sIndex += 5                     #   and increments index
    S.append(arr[sIndex:])

    # following code will create an array to hold
    # the medians of all of the subarrays
    Meds = []
    for subList in S:
        # recurse will go into len(arr) <= 10
        # and return the median of the subList
        Meds.append(d_select(subList, int((len(subList)-1)/2)))

    med = d_select(Meds, int((len(Meds)-1)/2))
    # med will hold the median of the medians

    # following code will split our array
    # by the pivot, pivot being med
    L1 = []         # elements < median
    L2 = []         # elements == median
    L3 = []         # elements > median
    for i in arr:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if k < len(L1):
        return d_select(L1, k)
    elif k < len(L2) + len(L1):
        return L2[0]
    else:
        return d_select(L3, k-len(L1)-len(L2))
  
def quickSorted(arr, low, high): 
    if len(arr) == 1: 
        return arr
    if low < high: 
  
        # following code is finding the partitioning
        # index and saving the value
        x = arr[high]
        i = (low-1)
        for j in range(low, high): 
            if arr[j] <= x:                     # checks if current value
                i = i+1                             #  <= pivot and adjusts
                arr[i], arr[j] = arr[j], arr[i]     #  arr accordingly
        arr[i+1], arr[high] = arr[high], arr[i+1]
        index = i+1
        # index will hold the partitioning index

        # sort before and after partition
        quickSorted(arr, low, index-1) 
        quickSorted(arr, index+1, high) 

def quickSort(arr,k):
    quickSorted(arr,0,len(arr)-1)
    return arr[k]


# array = list(range(100))
# random.shuffle(array)
# kay = int(len(array)/2)

array = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
kay = 10

# array = []
# kay = int(10**7/2)
# for i in range(0,10**7):
#     n = random.randint(0,10**7/100)
#     array.append(n)

#print("Array:", array)
#print("k:", kay)
#print()

t0 = time.time()
print("Randomized:", r_select(array,kay))
print("Run time:",time.time()-t0)

random.shuffle(array)
t1 = time.time()
print("Deterministic:",d_select(array,kay))
print("Run time:",time.time()-t1)

random.shuffle(array)
t2 = time.time()
print("QuickSorted:",quickSort(array,kay))
print("Run time:",time.time()-t2)