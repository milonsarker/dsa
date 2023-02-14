#https://leetcode.com/problems/add-binary/

class Solution:
    def return_data(self, num):
        if num == 2:
            return [0,1]
        if num == 3:
            return [1,1]
        if num == 1:
            return [1, 0]
    def addBinary(self, a: str, b: str) -> str:
        alist = list(a).reverse()
        blist = list(b).reverse()
        print(a)
        aLen = len(alist)
        bLen = len(blist) - 1
        aPtr = 0
        bPtr = 0
        result = []
        rem = 0
        while aLen > -1 or bLen > -1:
            if aLen > -1 and bLen > -1:
                res = int(alist[aPtr]) + int(blist[bPtr]) + rem
                out = self.return_data(res)
                result.append(out[0])
                rem = out[1]
            elif aLen > -1:
                res = int(alist[aPtr]) + rem
                out = self.return_data(res)
                result.append(out[0])
                rem = out[1]
            else:
                res = int(blist[bPtr]) + rem
                out = self.return_data(res)
                result.append(out[0])
                rem = out[1]
        return ''.join(result.reverse())
