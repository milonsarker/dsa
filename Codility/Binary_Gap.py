# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.8.10
    binary_num = bin(N)[2:]
    print(binary_num)
    max_gap = 0
    start = 0
    cnt = 0
    for i in binary_num:
        if start == 0 and i == '1':
            start = 1
        elif start == 1 and i == '1':
            start = 1
            if max_gap < cnt:
                max_gap = cnt
            cnt = 0
        if start == 1 and i == '0':
            cnt += 1
        print('i : ' + i +' ; cnt : ' + str(cnt))
    return max_gap

print(solution(74901729))