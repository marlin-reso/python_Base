'''
29️⃣ Find the largest element in a list.
30️⃣ Remove duplicates from a list.
31️⃣ Find the second largest number.
32️⃣ Sort a list without using sort().
33️⃣ Find common elements between two lists.
def sortList():
    # don’t shadow the built‑in name `list`
    lst = [1, 3, 6, 101, 3, 12, 65, 19, 99]

    # brute‑force pairwise swap until the list is in order
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

    print(lst)

sortList()   # prints [1, 3, 3, 6, 12, 19, 65, 99, 101]

# …existing code…

def findCommonElements():
    lst1 = [1, 3, 6, 101, 3, 12, 65, 19, 99]
    lst2 = [3, 19, 42, 65, 101]

    # easiest – convert to sets and intersect; result is a set of the shared items
    common = set(lst1) & set(lst2)
    print(common)          # {3, 19, 65, 101}

    # if you need a list (and/or want to preserve the order of lst1)
    seen = set()
    ordered = []
    for x in lst1:
        if x in lst2 and x not in seen:
            seen.add(x)
            ordered.append(x)
    print(ordered)         # e.g. [3, 101, 65, 19] – order follows lst1

#findCommonElements()


'''
def sortedList():
    lst = [6,7,3,9,2,10,3]

    for i in range (len(lst)-1):
        for j in range (i+1, len(lst)):
            if lst[j]< lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
        print(lst)
sortedList()

def findCommonElement():
    lst_one = [1,3,5,7,8]
    lst_two = [1,5,9,10]

    common = set(lst_one) & set(lst_two)
    print(common)
#findCommonElement()



def sortList():
     lst = [1,3,6,101,3,12,65,19,99]
     for num in list:
         print(num)
#sortList()


def findSecondLargestNum():
    list = [1,3,6,101,3,12,65,19,99]
    list.sort()
    print(list[-2])
#findSecondLargestNum()

def findLargestInList():
    list = [1,3,6,101,3,12,65,19,99]
    list.sort()
    print(list[-1])
#findLargestInList()

def rmDuplicateFromList():
    list = [1,3,6,101,3,12,65,19,99]
    s = set()
    for num in list:
       s.add(num)
    print(s)
#rmDuplicateFromList()
    