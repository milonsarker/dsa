
def insertion_sort(idata):
    for i in range(1, len(idata)):
        pointer_element = idata[i]
        for j in range(i - 1, -1, -1):
            print(idata)
            if pointer_element >= idata[j]:
                break
            else:
                idata[j + 1], idata[j] = idata[j], pointer_element
        print('------------------------------------------' + str(i))
    return idata
if __name__ == "__main__":
    data = [2, 1, 3, 88, 12, 0, -100, 89, 100, 101, -999]
    data_desc = [99, 98, 10, 9, 1, -100]
    sorted_data = insertion_sort(data)
    print(sorted_data)
    print('hello there')