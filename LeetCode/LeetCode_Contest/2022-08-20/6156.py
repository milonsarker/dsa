class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        for i in range(len(blocks)):
            print(i)


if __name__=="__main__":
    input = "WBBWWBBWBW"
    k = 7

    solObj = Solution()
    solObj.minimumRecolors(input, k)