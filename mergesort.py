def merge2(list1, list2, func):
    targetLen=len(list1)+len(list2)
    l1, l2=list1.copy(), list2.copy()
    final=[]
    while len(final)<targetLen:
        if [] in [l1, l2]:
            final.extend(l1)
            final.extend(l2)
        elif func(l1[0])<func(l2[0]):
            final.append(l1.pop(0))
        else:
            final.append(l2.pop(0))
    return final

def mergesort(arr, **kwargs):
    func=kwargs.get('func', lambda x:x)

    if len(arr)==1:
        return arr
    else:
        length1=len(arr)//2
        list1=arr[:length1]
        list2=arr[length1:]
        return merge2(mergesort(list1, func=func), mergesort(list2, func=func), func)