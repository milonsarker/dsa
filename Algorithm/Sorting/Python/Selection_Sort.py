def selection_sort(idata):
    sorted_data = []
    while len(idata) > 0:
        minimum = 0
        for i in range(len(idata)):
            if idata[i] < idata[minimum]:
                minimum = i
        sorted_data.append(idata.pop(minimum))
    print(sorted_data)

def selection_sort_in_place(idata):
    for i in range(len(idata)):
        minimum = i
        for j in range(i + 1, len(idata[i:])):
            if idata[j] < idata[minimum]:
                minimum = j
        idata[i], idata[minimum] = idata[minimum], idata[i]
    print(idata)

if __name__ == "__main__":
    data = [2, 1, 3, 88, 12, 0, -100, 89, 100, 101, -999]
    data_desc = [99, 98, 10, 9, 1, -100]
    selection_sort(data)
    selection_sort_in_place(data_desc)