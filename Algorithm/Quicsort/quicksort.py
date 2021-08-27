from random import randrange
def qsort(array):
    if len(array)<2:
        return array
    else:
        # pivot = array.pop(0)
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i<=pivot]
        katta = [i for i in array if i>pivot]
        print(f"{kichik}+[{pivot}]+{katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

