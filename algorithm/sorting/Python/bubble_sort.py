
def bubble_sort(idata):
    for i in range(len(idata) - 1):
        for j in range(len(idata) - 1):
            if idata[j] > idata[j + 1]:
                idata[j], idata[j + 1] = idata[j + 1], idata[j]
    print(idata)

def bubble_sort_improved(idata):
    for i in range(len(idata)):
        swapped = False
        for j in range(len(idata) - 1):
            if idata[j] > idata[j + 1]:
                idata[j], idata[j + 1] = idata[j + 1], idata[j]
                swapped = True
            if  not swapped:
                break
    print(idata)

if __name__=="__main__":
    data = [2, 1, 3, 88, 12, 0, -100, 89, 100, 101, -999]
    data_desc = [99, 98, 10, 9, 1, -100]
    bubble_sort(data_desc)

    bubble_sort_improved(data_desc)