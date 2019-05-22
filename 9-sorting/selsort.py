def findSmallest(sortlist):
    smallest = sortlist[0]
    smallest_index = 0
    for i in range(1, len(sortlist)):
        if sortlist[i] < smallest:
            smallest = sortlist[i]
            smallest_index = i
    return smallest_index

def selectionSort(sortlist):
    newsortlist = []
    for i in range(len(sortlist)):
        smallest = findSmallest(sortlist)
        newsortlist.append(sortlist.pop(smallest))
    return newsortlist
