#https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        cntr = 1
        while cntr <= n:
            if cntr % 3 == 0 and cntr % 5 == 0:
                answer.append("FizzBuzz")
            elif cntr % 3 == 0:
                answer.append("Fizz")
            elif cntr % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(cntr))
            cntr += 1
        return answer