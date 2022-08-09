
def insertion_sort(idata):
    for i in range(1, len(idata) - 1):
        pointer_element = idata[i]
        for j in range(i, -1, -1):
            if pointer_element >= idata[j - 1]:
                break
            else:
                idata[j], idata[j - 1] = idata[j - 1], pointer_element

    print(idata)

if __name__ == "__main__":
    data = [2, 1, 3, 88, 12, 0, -100, 89, 100, 101, -999]
    data_desc = [99, 98, 10, 9, 1, -100]
    insertion_sort(data)